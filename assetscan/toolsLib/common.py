from .mongo import *
from datetime import datetime
import time
import base64
import socket


def format_rules(key, rule):
    result = []
    try:
        rule_lines = rule.split('\n')
        for rule_line in rule_lines:
            if key == 'discern_server':
                res = rule_line.split('|', 3)
                res[0] = res[0].lower()
                result.append(res)
            else:
                result.append(rule_line.split('|', 3))
    except Exception as e:
        print(e)
    return result


def getConfig():
    result = {}
    try:
        row_ini = Config.find_one({'type': 'assetscan'})
        if row_ini and 'config' in row_ini:
            for key in row_ini['config']:
                if key in ('discern_server', 'discern_cms', 'discern_lang', 'discern_con'):
                    result[key] = format_rules(key, row_ini['config'][key]['value'])
                else:
                    result[key] = row_ini['config'][key]['value']
    except Exception as e:
        print(e)
    return result


def getRecord():
    record = {}
    try:
        date = datetime.now().strftime("%Y-%m-%d")
        res = Record.find_one({'date': date})
        if res:
            record[date] = res['info']
        else:
            record[date] = {'add': 0, 'update': 0, 'delete': 0}
    except Exception as e:
        print(e)
    return record


def monitor(configIni, record, totalFlag):
    while True:
        try:
            date = datetime.now()
            date_ = date.strftime("%Y-%m-%d")
            Heartbeat.update_one({'type': 'assetscan'}, {'$set': {'up_time': date, 'value': totalFlag['progress']}})
            if date_ not in record:
                record[date_] = {'add': 0, 'update': 0, 'delete': 0}
            Record.find_one_and_update({'date': date_}, {'$set': {'info': record[date_]}}, upsert=True)
            new_config = getConfig()
            if base64.b64encode(new_config['scan_list'].encode()) != base64.b64encode(configIni['scan_list'].encode()):
                totalFlag['isScan'] = 1
            configIni.clear()
            configIni.update(new_config)
        except Exception as e:
            print(e)
        time.sleep(10)


def check(record, totalFlag):
    while True:
        try:
            hosts = Info.find().sort('time', 1)
            for host in hosts:
                while True:
                    if totalFlag['masscan']:
                        break
                    time.sleep(5)
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((host['ip'], int(host['port'])))
                    sock.close()
                except Exception as  e:
                    date = datetime.now()
                    Info.remove({'ip': host["ip"], 'port': host['port']})
                    record[date.strftime('%Y-%m-%d')]['delete'] += 1
                    del host["_id"]
                    host['del_time'] = date
                    host['type'] = 'delete'
                    History.insert(host)
                    print(e)
        except Exception as e:
            print(e)
        time.sleep(30)
