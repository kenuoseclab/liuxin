class Web:
    WEBNAMEUSER = 'liuxin'
    WEBPASSWORD = '12345'


class Mongodb:
    MONGODBHOST = "192.168.253.110"
    MONGODBPORT = 65500
    MONGODBNAME = "liuxin"
    MONGODBUSER = "liuxin"
    MONGODBPASS = "12345"


class Ini(Web, Mongodb):
    pass


