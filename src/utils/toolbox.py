import re
from os import listdir
from os.path import isfile, join
import os

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
        raise Exception(f'Too many files in folder {directory}')
    if len(ls_file) == 0:
        raise Exception(f'There is no file in {directory}')
    return ls_file[0]

