# importing module
import os

from src.utils.decorators import sleep
from src.utils.load_data import get_message, get_usernames, load_selenium_path, get_errors
from src.seleniumlauncher import SeleniumManager
from src.utils.logging_toolbox import log_metrics


class InstaBot(SeleniumManager):

    PATH_USERS = "data/usernames/usernames.txt"
    PATH_FAIL = "data/usernames/errors.txt"
    PATH_MSG = "data/messages/text_1.txt"
    PATH_SELENIUM = 'data/selenium_path.json'

    def __init__(self, type):
        self.base_url = 'https://www.instagram.com/'
        self.users = get_usernames(self.PATH_USERS)
        self.message = get_message(self.PATH_MSG)
        self.path = load_selenium_path(self.PATH_SELENIUM)
        self.flyer = "data/flyers/photo.PNG"
        self.setup()
        self.run(type)

    def run(self, type):
        self._access()
        self._process(type)

    def _access(self):
        self._login_access()
        self._login_username()
        self._login_password()
        self._login_validation()
        self._popup_1()
        self._popup_2()
        self._direct_button()

    def _process(self, type):
        for n, user in self._user_iteration():
            try:
                self._click_pencil()
                self._enter_username(user)
                self._click_username()
                self._next_button()
                self._click_msg_box()
                if 'flyer' in type:
                    self._insert_flyer()
                if 'message' in type:
                    self._type_msg()
                    self._send_msg()
                print(n, user)
            except:
                self._append_to_list(user)
                self._launch_url()
                self._direct_button()
        self._print_statistics()

    def _print_statistics(self):
        PATH_FAIL = self.PATH_FAIL
        fail_usernames = get_errors(PATH_FAIL)

        PATH_USERS = self.PATH_USERS
        all_usernames = get_usernames(PATH_USERS)

        metrics = round(len(fail_usernames) / len(all_usernames), 3)

        log_metrics.info(f"Success at {1 - metrics} : {fail_usernames}")

    def _user_iteration(self):
        users = self.users
        for n, user in enumerate(users):
            yield n, user

    def _append_to_list(self, user):
        print(f"FAIL {user}")
        with open('data/user_fail.txt', 'a') as fd:
            fd.write(f'\n{user}')

    def _click_msg_box(self):
        path = self.path['click_msg_box']
        self.click_by_xpath(path)

    @sleep(3)
    def _login_access(self):
        path = self.path['login_access']
        self.click_by_xpath(path)

    def _login_username(self):
        username = os.environ['USERNAME']
        user = self.find_by_name('username')
        user.send_keys(username)

    @sleep(3)
    def _login_password(self):
        password = os.environ['PASSWORD']
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
    def _direct_button(self):
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

    @sleep(1)
    def _next_button(self):
        path = self.path['next_button']
        self.click_by_xpath(path)

    def _type_msg(self):
        message = self.message
        path = self.path['type_msg']
        chat = self.find_by_xpath(path)
        chat.send_keys(message)

    def _insert_flyer(self):
        flyer = self.flyer
        path = self.path['insert_flyer']
        msg_box = self.find_by_xpath(path)
        msg_box.send_keys(flyer)
