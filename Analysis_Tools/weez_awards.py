class WeezAwards:
    """
    Object that calculates various award metrics for a Player.
    """

    def __init__(self, player_list: list):
        """

        :param player_list: a list object containing Player objects.
        """
        self.player_list = player_list
        self.pussio = 'Cheen'

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

    def _get_serial_killer(self):
        """
        Calculate the Player with the most last stand kills in the session.
        :return: None.
        """
        self.serial_killer = None
        max_last_stand_kills = 0

        for player in self.player_list:
            if player.last_stand_kills > max_last_stand_kills:
                self.serial_killer = player.player_name
                max_last_stand_kills = player.last_stand_kills

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
        self._get_serial_killer()

    def show_results(self) -> str:
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
                  f'{self.serial_killer} is the serial killer\n' \
                  f'{self.pussio} is the pussi o\n'

        return results
