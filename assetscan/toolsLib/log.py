import logging
import datetime

logging.basicConfig(level=logging.DEBUG, format="[%(nowtime)s] %(message)s")


def logWrite(message):
    try:
        ext = {'nowtime': datetime.datetime.now().strftime('%X')}
        logging.info(message, extra=ext)
    except Exception as e:
        print(e)
