# importing module
import os

from src.utils.decorators import sleep
from src.utils.load_data import get_message, get_usernames, load_selenium_path, get_errors
from src.seleniumlauncher import SeleniumManager
from logs.logging_toolbox import log_metrics
from src.utils.toolbox import get_file_path
import sys


class InstaBot(SeleniumManager):

    PATH_USERS = "data/usernames/test.txt"
    PATH_FAIL = "data/usernames/errors.txt"
    PATH_SELENIUM = 'data/selenium_path.json'

    def __init__(self):
        self.base_url = 'https://www.instagram.com/'
        self.users = get_usernames(self.PATH_USERS)
        self.path = load_selenium_path(self.PATH_SELENIUM)
        self.parse_arguments()
        self.setup()
        self._access()
        self._run()

    def _access(self):
        self._launch_url()
        self._login_access()
        self._login_username()
        self._login_password()
        self._login_validation()
        self._popup_1()
        self._popup_2()

    def _run(self):
        if self.videoId:
            self._process_for_videos()
        if self.message or self.file:
            self._process_for_file_or_message()

    def _process_for_file_or_message(self):
        self._click_direct_button()
        for n, user in self._user_iteration():
            try:
                self._click_pencil()
                self._select_username(user)
                self._click_next()
                self._click_msg_box()
                self._send_info()
                print('file', n, user)
            except:
                self._append_to_error_list(user)
                self._launch_url()
                self._click_direct_button()

    def _process_for_videos(self):
        self._access_video_page()
        for n, user in self._user_iteration():
            try:
                self._click_video_msg()
                self._select_username(user)
                self._send_video()
                print('video', n, user)
            except:
                self._append_to_error_list(user)
                self._access_video_page()

    def _select_username(self, user):
        self._enter_username(user)
        self._click_username()

    def _access_video_page(self):
        video_path = self._get_video_path()
        self._launch_url(video_path)
        return


    def parse_arguments(self):
        videoId, message, file = '', False, False
        args = [arg for arg in sys.argv if not arg.endswith('.py')]
        if set(args) - set(['message', 'file', 'video']):
            unknown = set(args) - set(['message', 'file', 'video'])
            raise Exception(f"\n\n\nUnknown arguments used: {list(unknown)} \n\n Available arguments : 'message', 'file', 'video' ") 
        if 'video' in args:
            videoId = input("Video ID: ")
            print(f"VIDEO: {videoId}")
        if 'file' in args:
            file = get_file_path('data/file/')
            print(f"FILE: {file}")
        if 'message' in args:
            message = get_message('data/messages/')
        self.videoId = videoId
        self.message = message
        self.file = file

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
            print("     file sent")
        if self.message:
            self._type_msg()
            self._send_msg()
            print("     message sent")
    def _user_iteration(self):
        users = self.users
        for n, user in enumerate(users):
            yield n, user

    def _launch_url(self, url=None):
        if url:
            self.driver.get(url)
        else:
            base_url = self.base_url
            self.driver.get(base_url)

    def _append_to_error_list(self, user):
        PATH_FAIL = self.PATH_FAIL
        with open(PATH_FAIL, 'a') as fd:
            fd.write(f'\n{user}')
        print(f"FAIL {user}")

    def _click_msg_box(self):
        path = self.path['click_msg_box']
        self.click_by_xpath(path)

    @sleep(3)
    def _login_access(self):
        path = self.path['login_access']
        self.click_by_xpath(path)

    def _login_username(self):
        username = os.environ['INSTAGRAM_USERNAME']
        user = self.find_by_name('username')
        user.send_keys(username)

    @sleep(3)
    def _login_password(self):
        password = os.environ['INSTAGRAM_PASSWORD']
        passw = self.find_by_name('password')
        passw.send_keys(password)

    @sleep(3)
    def _login_validation(self):
        selector = "button[type='submit']"
        self.click_by_css(selector)

    @sleep(4)
    def _popup_1(self):
        path = self.path['popup_1']
        self.click_by_xpath(path)

    @sleep(4)
    def _popup_2(self):
        path = self.path['popup_2']
        self.click_by_xpath(path)

    @sleep(3)
    def _click_direct_button(self):
        path = self.path['direct_button']
        self.click_by_xpath(path)

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
