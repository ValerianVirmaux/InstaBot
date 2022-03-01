from src.utils.toolbox import open_txt_file, clean
import json


def get_usernames(path):
    usernames = open_txt_file(path)
    usernames_clean = clean(usernames)
    ls_usernames = usernames_clean.split(' ')
    return ls_usernames

def get_errors(path):
    import re
    errors = open_txt_file(path)
    errors = re.sub(' +', ' ', errors)
    errors = errors.replace('\n', ' ')
    errors = errors.split(' ')
    errors = [error for error in errors if error]
    return errors

def get_message(path):
    message = open_txt_file(path)
    message_clean = message.replace('\n', ' ')
    return message_clean


def load_selenium_path(path):
    with open(path, 'r') as f:
        data = json.loads(f.read())
        return data
