from pymongo import MongoClient


class MongoDB(object):
    def __init__(self, host='localhost', port=27017, database='xunfeng', username='', password=''):
        self.host = host
        self.port = port
        self.database = database
        self.client = MongoClient(host, port)
        self.liuxin = getattr(self.client, self.database)
        self.liuxin.authenticate(username, password)
