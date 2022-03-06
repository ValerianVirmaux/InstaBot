import re
import os
import sys
from logs.logging_toolbox import log_process

def open_txt_file(path):
    with open(path, "r") as f:
        text = f.read()
        return text

def clean(username):
    clean = re.sub(' +', ' ', username)
    clean = clean.replace('\n', '')
    return clean

def get_file_path(directory):
    ls_file = []
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            file = os.path.abspath(os.path.join(dirpath, f))
            ls_file.append(file)
    return ls_file


def check_parameters():
    log_process.info(f"ARGS RECEIVED : {sys.argv}")
    available_args = ['message', 'file', 'video']
    args = [arg for arg in sys.argv if not arg.endswith('.py')]
    if set(args) - set(available_args):
        unknown = set(args) - set(available_args)
        raise Exception(f"\n\n\nUnknown arguments used: {list(unknown)} \n\n Available arguments : 'message', 'file', 'video' ")
    log_process.info(f"ARGS KEPT : {args}")
    return args

