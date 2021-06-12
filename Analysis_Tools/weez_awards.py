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
            damage = player.damage_taken
            if damage > max_damage:
                self.bullet_bitch = player.playername
                max_damage = damage

    def _get_medic(self):
        """
        Calculate the Player with the most revives in the session.
        :return: None.
        """
        self.medic = None
        max_revives = 0

        for player in self.player_list:
            revives = player.revives
            if revives > max_revives:
                self.medic = player.playername
                max_revives = revives

    def _get_head_master(self):
        """
        Calculate the Player with the most headshots in the session.
        :return: None.
        """
        self.head_master = None
        max_headshots = 0

        for player in self.player_list:
            headshots = player.headshots
            if headshots > max_headshots:
                self.head_splitter = player.playername
                max_headshots = headshots

    def _get_assister(self):
        """
        Calculate the Player with the most assists in the session.
        :return: None.
        """
        self.top_assister = None
        max_assists = 0

        for player in self.player_list:
            assists = player.assists
            if assists > max_assists:
                self.top_assister = player.playername
                max_assists = assists

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
            score = player.score
            if score > max_score:
                self.team_lover = player.playername
                max_score = score
            if score < min_score:
                self.team_hater = player.playername
                min_score = score

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
            damage = player.damage
            kills = player.kills
            ratio = damage / kills
            if ratio > max_lethality:
                self.least_lethal_killer = player.playername
                max_lethality = ratio
            if ratio < min_lethality:
                self.lethal_killer = player.playername
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
            damage = player.damage_taken
            deaths = player.deaths
            ratio = damage/deaths
            if ratio > max_value:
                self.tank = player.playername
                max_value = ratio
            if ratio < min_value:
                self.gummy_bear = player.playername
                min_value = ratio

    def process_player_stats(self):
        """
        Method that process all the private methods to produce the awards.
        :return: None.
        """
        self._get_bullet_bitch()
        self._get_medic()
        self._get_head_master()
        self._get_assister()
        self._get_team_lover_and_hater()
        self._get_lethality()
        self._get_tank()

    def show_results(self) -> str:
        """
        Produce a string that shows the entire results of the awards.
        :return: String object that contains the awards.
        """
        results = f"""
            {self.bullet_bitch} is the bullet bitch
            {self.medic} is the medic
            {self.head_master} is the headmaster
            {self.top_assister} is the top assister
            {self.team_lover} loves the team
            {self.lethal_killer} is the lethal killer
            {self.least_lethal_killer} is the least lethal killer
            {self.tank} is the tank
            {self.gummy_bear} is the gummy bear
            {self.pussio} is the pussio"""
        return results
