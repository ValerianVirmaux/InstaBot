import re

def open_txt_file(path):
    with open(path, "r") as f:
        text = f.read()
        return text

def clean(username):
    clean = re.sub(' +', ' ', username)
    clean = clean.replace('\n', '')
    return clean

