from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time


class WeezScraper(webdriver.Chrome):
    """
    Object that will scrape daily Warzone data for a given player.
    """
    # options = Options()
    # options.headless = True
    _driver_path = '/Users/rumeeahmed/Documents/Weez/chromedriver'
    _url = 'https://cod.tracker.gg/warzone'

    def __init__(self, username: str, platform: str):
        """

        :param username: The username for the player in question.
        :param platform: The platform the username is associated with. For now only use use usernames that belong to
        the PlayStation Network or the Activision Network.
        """
        super().__init__(self._driver_path)
        self.username = username
        self.platform = platform
        self.make_request()
        self.search_warzone()

    def make_request(self):
        """
        Perform a get request on self._url.
        :return: None
        """
        self.get(self._url)
        self._bypass_gpdr()

    def _bypass_gpdr(self):
        """
        The first page is often a GDPR policy page, this method will click and then suppress the page.
        :return: None
        """

        try:
            button = WebDriverWait(self, 10).until(
                EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler'))
            )
            button.click()

        except NoSuchElementException:
            pass

    def search_warzone(self):
        """
        Perform a search on the Warzone website with self.username and self.platform correct gaming platform to go to
        the users stats page.
        :return: None
        """

        self.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div[1]/div/div[2]'
        ).click()

        if self.platform == 'PS':
            self.find_element_by_xpath(
                '//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div[1]/div/div[2]/ul/'
                'li[1]/span'
            ).click()

        elif self.platform == 'activision':

            self.find_element_by_xpath(
                '//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div[1]/div/div[2]/ul/'
                'li[2]/span'
            ).click()

        self.implicitly_wait(5)

        search = self.find_element_by_tag_name('input')
        search.clear()
        search.send_keys(self.username)
        search.send_keys(Keys.RETURN)


scraper = WeezScraper('RumeeAhmed', 'PS')
