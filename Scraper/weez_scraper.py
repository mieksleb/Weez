from datetime import datetime
import requests


class WeezScraper:
    """
    Object that will scrape daily Warzone data for a given player.
    """
    _base_url = f'https://api.tracker.gg/api/v2/warzone/standard/matches'

    def __init__(self, username: str, platform: str):
        """

        :param username: The username of the player in question.
        :param platform: The gaming platform the username is associated with.
        For now only use usernames that belong to the PlayStation Network or
        the Activision Network. Acceptable strings for this parameter are `psn`
         and `atvi`.
        """
        self.username = username
        self.platform = platform.lower()
        self.stats = []

    def _construct_timestamp(self) -> None:
        """
        Get the current timestamp in milliseconds.
        :return: None.
        """
        current_timestamp = datetime.now().timestamp()
        timestamp = round(current_timestamp) * 1000
        self._timestamp = timestamp

    def _build_url(self) -> None:
        """
        Build the url to perform a GET request against and retrieve game data
        for the specified user and the platform they belong to.
        :return: None.
        """
        formatted_user = self.username.replace('#', '%23')
        self._url = f'{self._base_url}/{self.platform}/{formatted_user}'

    def _get_matches(self) -> list:
        """
        Build the url and timestamp and then perform a GET request to retrieve
        all the matches played by the user at the given date.
        :return: a list object containing the players game data.
        """
        self._build_url()
        self._construct_timestamp()
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/74.0.3729.169 Safari/537.36",
            'referer': 'https://www.google.com/'
        }
        params = {'type': 'wz', 'next': self._timestamp}
        response = requests.get(self._url, headers=headers, params=params)
        response.raise_for_status()
        matches = response.json()['data']['matches']
        return matches

    def _get_current_matches(self) -> list:
        """
        Return the matches only played in the last session/date.
        :return: a list object containing dictionaries of match stats.
        """
        matches = self._get_matches()
        self.date_played = matches[0]['metadata']['timestamp'].split('T')[0]

        current_matches = []
        for match in matches:
            match_timestamp = match['metadata']['timestamp'].split('T')[0]
            if match_timestamp == self.date_played:
                current_matches.append(match)

        return current_matches

    def _extract_match_stats(self) -> list:
        """
        Extract and return all the match stats from the stat object.
        :return: a list object containing all the match stats.
        """
        current_matches = self._get_current_matches()
        match_stats = []
        for match in current_matches:
            stats = match['segments'][0]['stats']
            match_stats.append(stats)
        return match_stats

    def scrape(self) -> None:
        """
        Process the raw stats into key value pairs only.
        :return: None.
        """
        stats = self._extract_match_stats()

        for stat in stats:
            cleaned_stat = {}
            self.stats.append(cleaned_stat)

            for key, value in stat.items():
                cleaned_stat[key] = value['value']
                cleaned_stat['datePlayed'] = self.date_played
