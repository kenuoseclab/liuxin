import os, sys

sys.path.append(
    os.path.join(os.path.join(os.path.split(os.path.realpath(__file__))[0], os.path.pardir), os.path.pardir))
from mongo.mongo import MongoDB
from config import Ini

con = MongoDB(Ini.MONGODBHOST, Ini.MONGODBPORT, Ini.MONGODBNAME, Ini.MONGODBUSER, Ini.MONGODBPASS)
Config = con.liuxin.Config
Info = con.liuxin.Info
Heartbeat = con.liuxin.Heartbeat
Record = con.liuxin.Record
