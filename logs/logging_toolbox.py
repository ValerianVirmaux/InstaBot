import logging


logging.basicConfig(
    filename="logs/logs.log",
    filemode='w',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO)

log_metrics = logging.getLogger('metrics')
log_process = logging.getLogger('process')
