from selenium import webdriver
from selenium.webdriver.common.by import By
from src.utils.toolbox import get_file_path
from src.utils.decorators import retry
import os


env = os.environ.get('ENVIRONMENT')


class SeleniumManager:

    def setup(self):
        self._get_options()
        self._setup_driver()


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
        options = self._options
        if env == 'LOCAL':
            path_driver = get_file_path('config/driver/')
            driver = webdriver.Chrome(path_driver[0], chrome_options=options)
        else:
            driver = webdriver.Chrome(chrome_options=options)
        self.driver = driver


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




