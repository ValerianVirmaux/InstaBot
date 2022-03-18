import re
import os
import sys
from src.logs.logging_toolbox import log_process

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
    if len(ls_file) > 1:
        msg = f'Muitos arquivos em {directory}'
        log_process.error(msg)
        raise Exception(msg)
    if len(ls_file) == 0:
        msg = f'Está faltando um arquivo em {directory}'
        log_process.error(msg)
        raise Exception(msg)
    return ls_file[0]


def check_parameters():
    log_process.info(f"ARGS RECEIVED : {sys.argv}")
    available_args = ['message', 'file', 'video']
    args = [arg for arg in sys.argv if not arg.endswith('.py')]
    if set(args) - set(available_args):
        unknown = set(args) - set(available_args)
        raise Exception(f"\n\n\nArgumentos desconhecidos: {list(unknown)}")
    log_process.info(f"ARGS KEPT : {args}")
    return args

