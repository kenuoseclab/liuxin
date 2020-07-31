from .mongo import *
from datetime import datetime
import time
import base64


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
            date = datetime.now().strftime("%Y-%m-%d")
            Heartbeat.update_one({'type': 'assetscan'}, {'$set': {'up_time': date}})
            if date not in record:
                record[date] = {'add': 0, 'update': 0, 'delete': 0}
            Record.find_one_and_update({'date': date}, {'$set': {'info': record[date]}}, upsert=True)
            new_config = getConfig()
            if base64.b64encode(new_config['scan_list']) != base64.b64encode(configIni['scan_list']):
                totalFlag['isScan'] = 1
            configIni.clear()
            configIni.update(new_config)
        except Exception as e:
            print(e)
        time.sleep(10)


def cursor():
    pass
