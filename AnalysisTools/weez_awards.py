from AnalysisTools.weez_reader import Player


class WeezAwards:
    """
    Object that calculates various award metrics for a Player.
    """

    def __init__(self, player_list: list[Player]):
        """

        :param player_list: a list object containing Player objects.
        """
        self.player_list = player_list
        self.pussio = 'Cheen'
        self.date = player_list[0].date

    def _get_bullet_bitch(self):
        """
        Calculate the Player who has absorbed the most damage in the session.
        :return: None.
        """
        self.bullet_bitch = None
        max_damage = 0

        for player in self.player_list:
            if player.damage_taken > max_damage:
                self.bullet_bitch = player.player_name
                max_damage = player.damage_taken

    def _get_medic(self):
        """
        Calculate the Player with the most revives in the session.
        :return: None.
        """
        self.medic = None
        max_revives = 0

        for player in self.player_list:
            if player.revives > max_revives:
                self.medic = player.player_name
                max_revives = player.revives

    def _get_head_master(self):
        """
        Calculate the Player with the most headshots in the session.
        :return: None.
        """
        self.head_master = None
        max_headshots = 0

        for player in self.player_list:
            if player.headshots > max_headshots:
                self.head_master = player.player_name
                max_headshots = player.headshots

    def _get_assister(self):
        """
        Calculate the Player with the most assists in the session.
        :return: None.
        """
        self.top_assister = None
        max_assists = 0

        for player in self.player_list:
            if player.assists > max_assists:
                self.top_assister = player.player_name
                max_assists = player.assists

    def _get_team_lover_and_hater(self):
        """
        Calculate the Player that loves the teams and the Player that hates the team.
        :return: None.
        """
        self.team_lover = None
        self.team_hater = None
        max_score = 0
        min_score = 100000

        for player in self.player_list:
            if player.score > max_score:
                self.team_lover = player.player_name
                max_score = player.score
            if player.score < min_score:
                self.team_hater = player.player_name
                min_score = player.score

    def _get_lethality(self):
        """
        Calculate the most and least lethal Player
        :return:None.
        """
        self.lethal_killer = None
        self.least_lethal_killer = None
        max_lethality = 0
        min_lethality = 100000

        for player in self.player_list:
            ratio = player.damage / player.kills
            if ratio > max_lethality:
                self.least_lethal_killer = player.player_name
                max_lethality = ratio
            if ratio < min_lethality:
                self.lethal_killer = player.player_name
                min_lethality = ratio

    def _get_tank(self):
        """
        Calculate the Player who requires the most damage for a death and the Player that takes the least damage per
        death.
        :return: None.
        """
        self.tank = None
        self.gummy_bear = None
        max_value = 0
        min_value = 100000

        for player in self.player_list:
            ratio = player.damage_taken / player.deaths
            if ratio > max_value:
                self.tank = player.player_name
                max_value = ratio
            if ratio < min_value:
                self.gummy_bear = player.player_name
                min_value = ratio

    def _get_team_demolisher(self):
        """
        Calculate the Player with the most team wipes in the session.
        :return: None.
        """
        self.team_demolisher = None
        max_team_wipes = 0

        for player in self.player_list:
            if player.teams_wiped > max_team_wipes:
                self.team_demolisher = player.player_name
                max_team_wipes = player.teams_wiped

    def process_player_stats(self):
        """
        Method that calls all the private methods to produce the awards.
        :return: None.
        """
        self._get_bullet_bitch()
        self._get_medic()
        self._get_head_master()
        self._get_assister()
        self._get_team_lover_and_hater()
        self._get_lethality()
        self._get_tank()
        self._get_team_demolisher()

    def show_player_results(self) -> str:
        """
        Produce a string that shows the entire results of the awards.
        :return: String object that contains the awards.
        """
        results = f'{self.bullet_bitch} is the bullet bitch\n' \
                  f'{self.medic} is the medic\n' \
                  f'{self.head_master} is the headmaster\n' \
                  f'{self.top_assister} is the top assister\n' \
                  f'{self.team_lover} loves the team\n' \
                  f'{self.team_hater} hates the team\n' \
                  f'{self.lethal_killer} is the lethal killer\n' \
                  f'{self.least_lethal_killer} is the least lethal killer\n' \
                  f'{self.tank} is the tank\n' \
                  f'{self.gummy_bear} is the gummy bear\n' \
                  f'{self.team_demolisher} is the team demolisher\n' \
                  f'{self.pussio} is the pussi o\n'

        return results

    def get_team_stats(self):
        self._get_total_team_stats()
        self._get_team_average_match_stats()

    def _get_total_team_stats(self):
        """
        Get the total team stats for the current session.
        :return: None.
        """
        self.team_score = 0
        self.team_kills = 0
        self.team_deaths = 0
        self.team_assists = 0
        self.team_damage = 0
        self.team_damage_taken = 0
        self.team_headshots = 0
        self.team_revives = 0
        self.team_teams_wiped = 0

        _average_team_kd = 0
        self.average_team_kd = _average_team_kd / len(self.player_list)

        for player in self.player_list:
            self.team_score += player.score
            self.team_kills += player.kills
            self.team_deaths += player.deaths
            self.team_assists += player.assists
            self.team_damage += player.damage
            self.team_damage_taken += player.damage_taken
            self.team_headshots += player.headshots
            self.team_revives += player.revives
            self.team_teams_wiped += player.teams_wiped
            _average_team_kd += player.kd

    def _get_team_average_match_stats(self):
        """
        Get the average stats for the entire team per games played.
        :return: None.
        """
        games_played = self.player_list[0].games_played
        self.team_score_per_game = self.team_score / games_played
        self.team_kills_per_game = self.team_kills / games_played
        self.team_deaths_per_game = self.team_deaths / games_played
        self.team_assists_per_game = self.team_assists / games_played
        self.team_damage_per_game = self.team_damage / games_played
        self.team_damage_taken_per_game = self.team_damage_per_game / games_played
        self.team_headshots_per_game = self.team_headshots / games_played
        self.team_revives_per_game = self.team_revives / games_played
        self.team_wiped_per_game = self.team_teams_wiped / games_played

    def _show_team_results(self) -> str:
        """
        Produce a string that shows the entire results the total team stats.
        :return: String object that contains the total team stats.
        """
        results = f'{self.bullet_bitch} is the bullet bitch\n' \
                  f'{self.medic} is the medic\n' \
                  f'{self.head_master} is the headmaster\n' \
                  f'{self.top_assister} is the top assister\n' \
                  f'{self.team_lover} loves the team\n' \
                  f'{self.team_hater} hates the team\n' \
                  f'{self.lethal_killer} is the lethal killer\n' \
                  f'{self.least_lethal_killer} is the least lethal killer\n' \
                  f'{self.tank} is the tank\n' \
                  f'{self.gummy_bear} is the gummy bear\n' \
                  f'{self.team_demolisher} is the team demolisher\n' \
                  f'{self.pussio} is the pussi o\n'

        return results
