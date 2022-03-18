import logging
import sys

sys.tracebacklimit = 0

logging.basicConfig(
    filename="logs.log",
    filemode='w',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO)

log_process = logging.getLogger('process')
log_user_fail = logging.getLogger('failed_username')