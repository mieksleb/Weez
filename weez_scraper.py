from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time


class WeezScraper(webdriver.Chrome):

    _driver_path = '/Users/rumeeahmed/Documents/Weez/chromedriver'

    def __init__(self, username: str, platform: str):
        super().__init__(self._driver_path)
        self.username = username
        self.platform = platform
        self.executable_path = self._driver_path


scraper = WeezScraper('RumeeAhmed', 'PS4')
