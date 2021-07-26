from Analysis_Tools.weez_reader import Player
import numpy as np


def get_sum_dict(player: Player, match_stats: list) -> dict:
    """
    Function which takes a player class and a list of match dictionaries and returns the a dictionary of the sum, with
    an extra key for matches played. Note that for things like KD, the sum is a useless_quantity and should be sourced
    from the player_stats.

    :param player: Player object.
    :param match_stats: List containing the Player's associated match_stats that is returned from the scraper.
    :return: a dictionary object containing the totals of all the main stats.
    """
    total_dict = {
        'Name': player.player_name,
        'Deaths': 0,
        'Assists': 0,
        'Damage Taken': 0,
        'Headshots': 0,
        'Score': 0,
        'Teams Wiped': 0,
        'Revives': 0,
    }

    for stat in match_stats:
        total_dict['Deaths'] += float(stat.get('Deaths', 0))
        total_dict['Assists'] += float(stat.get('Assists', 0))
        total_dict['Damage Taken'] += float(stat.get('Damage Taken', 0).replace(',', ''))
        total_dict['Headshots'] += float(stat.get('Headshots', 0))
        total_dict['Score'] += float(stat.get('Score', 0).replace(',', ''))
        total_dict['Teams Wiped'] += float(stat.get('Teams Wiped', 0))
        total_dict['Revives'] += float(stat.get('Revives', 0))

    return total_dict


class GNCalculator:
    """
    Object that handles the GN for a given Player.
    """

    def __init__(self, player: Player):
        """

        :param player: a Player object.
        """
        self.player = player

    def get_damage_gn(self) -> float:
        """
        Function that generates the aspirational damage GN for any given Player. There is an extra penalty for players
        that hoard damage.
        :return: An int object that represents the aspirational GN.
        """
        n = self.player.games_played
        rand = np.random.normal(1, 0.1)
        if self.player.player_name == 'ButtPunch69':
            return 900 * n * rand
        else:
            return 750 * n * rand

    def gn_judgement(self) -> bool:
        """
        Function that checks whether a Players damage is greater than the aspirational GN set by the damage GN.
        :return: A bool value that indicates whether the said player has reached their GN.
        """
        if self.player.damage < self.player.gn:
            return False
        if self.player.damage > self.player.gn:
            return True
