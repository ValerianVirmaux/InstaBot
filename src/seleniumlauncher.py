from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.utils.decorators import retry
import os


env = os.environ['ENVIRONMENT']


class SeleniumManager:

    PATH_DRIVER = "config/driver/chromedriver"

    def setup(self):
        self._get_options()
        self._setup_driver()
        self._launch_url()


    def _get_options(self):
        options = webdriver.ChromeOptions()
        if env != 'LOCAL':
            options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument('--disable-dev-shm-usage')
        self._options = options

    def _setup_driver(self):
        PATH_DRIVER = self.PATH_DRIVER
        options = self._options
        if env != 'LOCAL':
            driver = webdriver.Chrome(chrome_options=options)
        else:
            driver = webdriver.Chrome(PATH_DRIVER, chrome_options=options)
        self.driver = driver

    def _launch_url(self):
        url = self.base_url
        self.driver.get(url)

    @retry(3)
    def click_by_xpath(self, path):
        driver = self.driver
        element = driver.find_element(By.XPATH, path)
        element.click()

    @retry(3)
    def click_by_css(self, css):
        driver = self.driver
        element = driver.find_element(By.CSS_SELECTOR, css)
        element.click()

    @retry(3)
    def find_by_name(self, name):
        driver = self.driver
        element = driver.find_element(By.NAME, name)
        return element

    @retry(3)
    def find_by_xpath(self, xpath):
        driver = self.driver
        element = driver.find_element(By.XPATH, xpath)
        return element

    @retry(3)
    def _send_msg(self):
        driver = self.driver
        driver.send_keys(Keys.RETURN)

