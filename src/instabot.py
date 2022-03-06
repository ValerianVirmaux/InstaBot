# importing module

import os

from src.utils.decorators import sleep
from src.utils.load_data import get_message, get_usernames, load_selenium_path, get_file, get_video
from src.seleniumlauncher import SeleniumManager
from logs.logging_toolbox import log_process, log_user_fail


class InstaBot(SeleniumManager):

    def __init__(self, args):
        self.users = get_usernames()
        self.path = load_selenium_path()
        self.parse_arguments(args)
        self.setup()
        self._access()

    def run_video(self):
        log_process.info('Processing Video...')
        self._access_video_page()
        self._send_videos()

    def run_message(self):
        log_process.info('Processing messages...')
        self._access_message_page()
        self._process_messages()

    # Private
    def _access(self):
        self._launch_url('https://www.instagram.com/')
        self._login_access()
        self._login_username()
        self._login_password()
        self._login_validation()
        self._popup_1()
        self._popup_2()

    def _process_messages(self):
        for user in self._user_iteration():
            try:
                self._click_pencil()
                self._select_username(user)
                self._click_next()
                self._click_msg_box()
                self._send_info()
            except:
                self._append_to_error_list('messages', user)
                self._access_message_page()

    def _send_videos(self):
        for user in self._user_iteration():
            try:
                self._click_video_msg()
                self._select_username(user)
                self._send_video()
            except:
                self._append_to_error_list('video', user)
                self._access_video_page()

    def _select_username(self, user):
        self._enter_username(user)
        self._click_username()

    def _access_video_page(self):
        video_path = self._get_video_path()
        self._launch_url(video_path)

    def _access_message_page(self):
        url = 'https://www.instagram.com/direct/inbox/'
        self._launch_url(url)

    def parse_arguments(self, args):
        if 'video' in args:
            self.videoId = get_video()
        if 'file' in args:
            self.file = get_file('data/file/')
        if 'message' in args:
            self.message = get_message('data/messages/')

    def _get_video_path(self):
        videoId = self.videoId
        video_path = f"https://www.instagram.com/reel/{videoId}/"
        return video_path

    def _send_video(self):
        path = self.path['send_video']
        self.click_by_xpath(path)

    def _send_info(self):
        if self.file:
            file = self.file
            self._insert_file(file)
            print('     file sent')
        if self.message:
            self._type_msg()
            self._send_msg()
            print('     message sent')

    def _user_iteration(self):
        users = self.users
        for n, user in enumerate(users):
            print(n, user)
            yield user

    def _launch_url(self, url):
        self.driver.get(url)

    def _append_to_error_list(self, type, user):
        msg = f"{type} - {user}"
        log_user_fail.info(msg)

    @sleep(2)
    def _click_msg_box(self):
        path = self.path['click_msg_box']
        self.click_by_xpath(path)

    @sleep(3)
    def _login_access(self):
        path = self.path['login_access']
        self.click_by_xpath(path)

    @sleep(3)
    def _login_username(self):
        username = os.environ['INSTAGRAM_USERNAME']
        user = self.find_by_name('username')
        user.send_keys(username)

    def _login_password(self):
        password = os.environ['INSTAGRAM_PASSWORD']
        passw = self.find_by_name('password')
        passw.send_keys(password)

    def _login_validation(self):
        selector = "button[type='submit']"
        self.click_by_css(selector)

    @sleep(4)
    def _popup_1(self):
        path = self.path['popup_1']
        self.click_by_xpath(path)

    @sleep(4)
    def _popup_2(self):
        paths = self.path['popup_2']
        try:
            self.click_by_xpath(paths[0])
        except:
            self.click_by_xpath(paths[1])

    @sleep(2)
    def _click_pencil(self):
        path = self.path['click_pencil']
        self.click_by_xpath(path)

    @sleep(2)
    def _enter_username(self, user):
        path = self.path['enter_username']
        username = self.find_by_xpath(path)
        username.send_keys(user)

    @sleep(2)
    def _click_username(self):
        path = self.path['click_username']
        self.click_by_xpath(path)

    @sleep(2)
    def _click_video_msg(self):
        path = self.path['video_msg']
        self.click_by_xpath(path)

    @sleep(1)
    def _click_next(self):
        path = self.path['next_button']
        self.click_by_xpath(path)

    def _type_msg(self):
        message = self.message
        path = self.path['type_msg']
        chat = self.find_by_xpath(path)
        chat.send_keys(message)

    def _insert_file(self, file):
        path = self.path['insert_file']
        msg_box = self.find_by_xpath(path)
        msg_box.send_keys(file)

    def _send_msg(self):
        path = self.path['send_message']
        self.click_by_xpath(path)
