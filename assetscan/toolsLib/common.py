from .mongo import *
from datetime import datetime


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
    records = {}
    try:
        date = datetime.now().strftime("%Y-%m-%d")
        res = Record.find_one({'date': date})
        if res:
            records[date] = res['info']
        else:
            records[date] = {'active': 0, 'vulscan': 0}
    except Exception as e:
        print(e)
    return records


def monitor(configIni):
    while True:
        date = datetime.now().strftime("%Y-%m-%d")
        new_config = Config.find_one({'type': 'assetscan'})
