class Player:
    """
    Object that represents a player and their stats for the session.
    """
    def __init__(self, player_name: str):
        """

        :param player_name: The name of the player.
        """
        self.player_name = player_name
        self.gn = None
        self.judge = False

    def add_dicts(self, overall_dict: dict, sum_dict: dict) -> None:
        """
        Add the dictionary data as the player attributes.
        :param overall_dict: The dictionary object that contains the overall data for the session.
        :param sum_dict: The dictionary object that contains the sum of all the match data for the session.
        :return: None
        """
        self._process_overall_dict(overall_dict)
        self._process_sum_dict(sum_dict)

    def _process_overall_dict(self, overall_dict: dict) -> None:
        """
        Process the overall_dict data into class attributes.
        :param overall_dict: The dictionary object that contains the overall data for the session.
        :return: None
        """
        self.games_played = int(overall_dict.get('Matches Played', 0))
        self.kills = int(overall_dict.get('Kills', 0))
        self.damage = int(overall_dict.get('Damage', 0).replace(',', ''))
        self.kd = float(overall_dict.get('K/D', 0))
        self.date = overall_dict['Date']

    def _process_sum_dict(self, sum_dict: dict) -> None:
        """
        Process the sum_dict data into class attributes.
        :param sum_dict: The dictionary object that contains the sum of all the match data for the session.
        :return: None
        """
        self.deaths = int(sum_dict.get('Deaths', 0))
        self.damage_taken = int(sum_dict.get('Damage Taken', 0))
        self.score = int(sum_dict.get('Score', 0))
        self.teams_wiped = int(sum_dict.get('Teams Wiped', 0))
        self.assists = int(sum_dict.get('Assists', 0))
        self.headshots = int(sum_dict.get('Headshots', 0))
        self.revives = int(sum_dict.get('Revives', 0))

    def get_stats(self) -> str:
        """
        Get all the Player's stats and put it into an object.
        :return: A string object containing all of the Player's stats.
        """
        if self.judge:
            gn = f'{self.player_name} has hit his GN!'
        else:
            gn = f'{self.player_name} has failed to hit his GN!'

        stats = f'Stats for {self.player_name}\n' \
                f'{self.games_played} games played\n' \
                f'Score: {self.score}\n' \
                f'{self.kills} Kills\n' \
                f'{self.deaths} Deaths\n' \
                f'{self.assists} Assists\n' \
                f'{self.damage} Damage\n' \
                f'{self.damage_taken} Damage Received\n' \
                f'{self.kd} KD\n'\
                f'{self.headshots} Headshots\n'\
                f'{self.revives} Revives\n'\
                f'{self.teams_wiped} Teams Wiped\n'\
                f'{gn}'
        return stats


class Team:
    """
    Object that represents and handles the stats for the team.
    """
    def __init__(self, player_list: list[Player]):
        """

        :param player_list: a list object containing Player objects which then make up a Team.
        """
        self.player_list = player_list
        self.date = player_list[0].date

    def process_team_stats(self) -> None:
        """
        Process the total team stats and the average stats per game.
        :return: None
        """
        self._get_total_team_stats()
        self._get_team_average_match_stats()

    def _get_total_team_stats(self) -> None:
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

        self.average_team_kd = self.team_kills / self.team_deaths

    def _get_team_average_match_stats(self) -> None:
        """
        Get the average stats for the entire team per games played.
        :return: None.
        """
        games_played = self.player_list[0].games_played
        self.team_score_per_game = round(self.team_score / games_played, 2)
        self.team_kills_per_game = round(self.team_kills / games_played, 2)
        self.team_deaths_per_game = round(self.team_deaths / games_played, 2)
        self.team_assists_per_game = round(self.team_assists / games_played, 2)
        self.team_damage_per_game = round(self.team_damage / games_played, 2)
        self.team_damage_taken_per_game = round(self.team_damage_taken / games_played, 2)
        self.team_headshots_per_game = round(self.team_headshots / games_played, 2)
        self.team_revives_per_game = round(self.team_revives / games_played, 2)
        self.teams_wiped_per_game = round(self.team_teams_wiped / games_played, 2)
        self.average_team_kd_per_game = self.average_team_kd
