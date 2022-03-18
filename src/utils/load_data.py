from src.utils.toolbox import open_txt_file, clean, get_file_path
import json
from src.logs.logging_toolbox import log_process


def get_usernames():
    path = get_file('data/usernames/')
    usernames = open_txt_file(path)
    usernames_clean = clean(usernames)
    ls_usernames = usernames_clean.split(' ')
    log_process.info(f'Processing {len(ls_usernames)} usernames')
    return ls_usernames


def get_file(directory):
    path = get_file_path(directory)
    log_process.info(f"FILE >  {path}")
    return path


def get_video():
    videoId = input("Video ID: ")
    log_process.info(f"VIDEO >  {videoId}")
    return videoId


def get_message(directory):
    path = get_file_path(directory)
    message = open_txt_file(path)
    message_clean = message.replace('\n', ' ')
    log_process.info(f"MESAGE >  {path}")
    return message_clean


def load_selenium_path():
    path = get_file('config/path/')
    with open(path, 'r') as f:
        data = json.loads(f.read())
        return data
