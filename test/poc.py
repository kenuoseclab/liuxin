from pocsuite3.api import init_pocsuite
from pocsuite3.api import start_pocsuite
from pocsuite3.api import get_results
from pocsuite3.api import paths
from pocsuite3.api import get_poc_options, load_file_to_module, init_options
import os

if __name__ == '__main__':
    pocs = []
    init_pocsuite({})
    poc_dir = os.path.join(paths['POCSUITE_POCS_PATH'])
    poc_files = os.listdir(poc_dir)
    for poc_file in poc_files:
        flag = poc_file.find('.')
        if flag == 0 or flag == -1:
            continue
        try:
            poc = load_file_to_module(paths['POCSUITE_POCS_PATH'] + '/' + poc_file)
            pocs.append(poc.get_infos())
        except:
            pass
    print(len(pocs))
    for x in pocs:
        print(x)
    # config = {
    #     'url': 'http://192.168.253.186:22',
    #     'poc': 'ssh_burst'
    # }
    # init_pocsuite(config)
    # start_pocsuite()
    # result = get_results()
    # print(result[0]['status'])
