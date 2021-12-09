class Player:
    """
    Object that represents a player and their stats for the session.
    """
    def __init__(self, player_name: str):
        """

        :param player_name: a string object that represents the name of the
        player.
        """
        self.player_name = player_name
        self.gn = None
        self.judge = False

    def process_stats(self, stats: dict) -> None:
        """
        Process all the raw stats and then sum them all up for the player.
        :param stats: a dictionary object that contains all the players
        individual match data.
        :return: None.
        """
        sum = {
            'Assists': 0,
            'Crates Opened': 0,
            'Damage': 0,
            'Damage Taken': 0,
            'Date': stats[0].get('datePlayed', None),
            'Deaths': 0,
            'Distance Travelled': 0,
            'Headshots': 0,
            'Kills': 0,
            'Matches Played': len(stats),
            'Name': self.player_name,
            'Revives': 0,
            'Shop Buys': 0,
            'Score': 0,
            'Teams Wiped': 0,
            'Time Spent Moving': 0,
        }

        for stat in stats:
            sum['Assists'] += float(stat.get('assists', 0))
            sum['Crates Opened'] += float(stat.get('objectiveBrCacheOpen', 0))
            sum['Damage'] += float(stat.get('damageDone', 0))
            sum['Damage Taken'] += float(stat.get('damageTaken', 0))
            sum['Deaths'] += float(stat.get('deaths', 0))
            sum['Distance Travelled'] += float(stat.get('distanceTraveled', 0))
            sum['Headshots'] += float(stat.get('headshots', 0))
            sum['Kills'] += float(stat.get('kills', 0))
            sum['Revives'] += float(stat.get('objectiveReviver', 0))
            sum['Shop Buys'] += float(stat.get('objectiveBrKioskBuy', 0))
            sum['Score'] += float(stat.get('score', 0))
            sum['Teams Wiped'] += float(stat.get('objectiveTeamWiped', 0))
            sum['Time Spent Moving'] += float(stat.get('percentTimeMoving', 0))

        self._process_attributes(sum)

    def _process_attributes(self, summed_stats: dict) -> None:
        """
        Process the summed dictionary and convert them into attributes.
        :param summed_stats: a dictionary object containing all the summed up
        stats for the player.
        :return: None
        """
        self.games_played = summed_stats.get('Matches Played', 0)
        self.assists = round(summed_stats.get('Assists', 0))
        self.crates_opened = round(summed_stats.get('Crates Opened', 0))
        self.damage = round(summed_stats.get('Damage', 0))
        self.damage_taken = round(summed_stats.get('Damage Taken', 0))
        self.date = summed_stats.get('Date', None)
        self.deaths = round(summed_stats.get('Deaths', 0))
        self.distance_travelled = round(summed_stats.get('Distance Travelled', 0))
        self.headshots = round(summed_stats.get('Headshots', 0))
        self.kills = round(summed_stats.get('Kills', 0))
        self.kd = round(self.kills / self.deaths, 2)
        self.revives = round(summed_stats.get('Revives', 0))
        self.shop_buys = round(summed_stats.get('Shop Buys', 0))
        self.score = round(summed_stats.get('Score', 0))
        self.teams_wiped = round(summed_stats.get('Teams Wiped', 0))
        self.time_moving = round(summed_stats.get('Time Spent Moving', 0))

    def get_stats(self) -> str:
        """
        Get all the Player's stats and put it into a string object.
        :return: A string object containing all the Player's stats.
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
                f'{self.distance_travelled} Distance Travelled\n'\
                f'{self.time_moving} Time Moving Percent\n'\
                f'{self.crates_opened} Crates Opened\n'\
                f'{self.shop_buys} Shop Buys\n'\
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

        self.average_team_kd = round(self.team_kills / self.team_deaths, 2)

    def _get_team_average_match_stats(self) -> None:
        """
        Get the average stats for the entire team per games played.
        :return: None.
        """
        games = self.player_list[0].games_played
        self.team_score_per_game = round(self.team_score / games, 2)
        self.team_kills_per_game = round(self.team_kills / games, 2)
        self.team_deaths_per_game = round(self.team_deaths / games, 2)
        self.team_assists_per_game = round(self.team_assists / games, 2)
        self.team_damage_per_game = round(self.team_damage / games, 2)
        self.team_damage_taken_per_game = round(self.team_damage_taken / games, 2)
        self.team_headshots_per_game = round(self.team_headshots / games, 2)
        self.team_revives_per_game = round(self.team_revives / games, 2)
        self.teams_wiped_per_game = round(self.team_teams_wiped / games, 2)
        self.average_team_kd_per_game = self.average_team_kd
