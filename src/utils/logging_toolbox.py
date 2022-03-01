import time
import logging


logging.basicConfig(
    filename=f"logs/instabot_{int(time.time())}.log",
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG)

log_metrics = logging.getLogger('metrics')
log_process = logging.getLogger('process')
