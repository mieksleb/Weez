from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os


class WeezScraper(webdriver.Chrome):
    """
    Object that will scrape daily Warzone data for a given player.
    """

    _path = os.getcwd()
    _driver_path = f'{_path}/Assets/chromedriver'
    _url = 'https://cod.tracker.gg/warzone'

    options = Options()
    options.headless = False

    def __init__(self, username: str, platform: str):
        """

        :param username: The username of the player in question.
        :param platform: The gaming platform the username is associated with. For now only use use usernames that belong
        to the PlayStation Network or the Activision Network. Acceptable strings for this parameters are `PS` and
        `Activision`
        """
        super().__init__(self._driver_path, options=self.options)
        self.username = username
        self.platform = platform.lower()

    def _make_request(self):
        """
        Perform a get request on self._url.
        :return: Open Chrome browser and navigate to self._url.
        """
        self.get(self._url)
        self._bypass_personal_data_request()
        self._bypass_gdpr()

    def _bypass_gdpr(self):
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

    def _bypass_personal_data_request(self):
        """
        The first page is often a GDPR policy page, this method will click and then suppress the page.
        :return: None
        """

        try:
            button = WebDriverWait(self, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Continue to Site'))
            )
            button.click()

        except Exception:
            pass

    def _search_warzone(self):
        """
        Perform a search on the Warzone website with self.username and self.platform which then takes the browser to
        that users stats page.
        :return: None
        """

        self.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div[1]/div/div[2]'
        ).click()

        if self.platform == 'ps':
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

    def _scrape_stats(self):
        """
        Scrape the stats from the first page for the current gaming session.
        :return: Selenium object containing the HTML data for the current sessions stats.
        """
        stats = self.find_element_by_class_name('trn-gamereport-list__group')
        title_stats = stats.find_element_by_class_name('session-header')
        date_matches = title_stats.find_element_by_class_name('session-header__title').text

        date, matches_played = date_matches.split('\n')
        matches_played = int(matches_played)

        generic_rankings = title_stats.find_element_by_class_name('session-header__summary').text
        wins, top_5 = generic_rankings.split('\n')

        wins = wins[0]
        top_5 = top_5[0]

        self.overall_stats = {'Date': date, 'Matches Played': matches_played, 'Wins': wins, 'Top 5': top_5}

        self.implicitly_wait(5)
        overall_stats_raw = stats.find_elements_by_class_name('session-header__stats-stat')
        for stat in overall_stats_raw:
            try:
                label = stat.find_element_by_class_name('session-header__label').text
                value = stat.find_element_by_class_name('session-header__value').text
                self.overall_stats[label] = value
            except NoSuchElementException:
                pass

        self.match_stats = []
        for i in range(matches_played):
            self.implicitly_wait(5)
            match = self.find_element_by_class_name('trn-gamereport-list__group-entries')

            match_id = f'{date}-{i + 1}'
            stat_dict = {'Match ID': match_id}
            self.match_stats.append(stat_dict)

            buttons = match.find_elements_by_class_name('match-row__link')
            buttons[i].click()
            extra_stats = self._scrape_individual_match_stats()
            self.match_stats[i].update(extra_stats)

    def _scrape_individual_match_stats(self):
        """
        This will scrape the individual match stats per entry from the matches played.
        :return: Dictionary containing the detailed match stats
        """
        self.implicitly_wait(5)

        active_team_table = self.find_element_by_class_name('team--highlight')

        position_raw = active_team_table.find_element_by_class_name('placement').text
        position, time_played = position_raw.split('\n')

        detailed_match_stats = {'Position': position, 'Time Played': time_played}

        active_player = active_team_table.find_element_by_class_name('player-header--selected')
        active_player.find_element_by_class_name('button').click()
        left_stat_pane = active_team_table.find_element_by_class_name('left')
        player_stats = left_stat_pane.find_elements_by_class_name('stat')

        for stat in player_stats:
            raw_stat = stat.text
            label, value = raw_stat.split('\n')
            detailed_match_stats[label] = value

        self.back()
        return detailed_match_stats

    def scrape(self):
        """
        Public method to execute all the protected methods and then scrape the stats.
        :return: Players' Warzone stats.
        """
        self._make_request()
        self._search_warzone()
        self._scrape_stats()
        self.quit()
