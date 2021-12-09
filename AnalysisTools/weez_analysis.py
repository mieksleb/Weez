import numpy as np
from AnalysisTools.weez_reader import Player


class GNCalculator:
    """
    Object that handles the GN for a given Player.
    """

    def __init__(self, player: Player):
        """

        :param player: an instance of a Player object.
        """
        self.player = player

    def get_damage_gn(self) -> float:
        """
        Function that generates the aspirational damage GN for any given Player.
        There is an extra penalty for players that hoard damage.
        :return: An int object that represents the aspirational GN.
        """
        n = self.player.games_played
        rand = np.random.normal(1, 0.1)
        if self.player.player_name == 'The Golden God':
            return 900 * n * rand
        else:
            return 750 * n * rand

    def gn_judgement(self) -> bool:
        """
        Function that checks whether a Players damage is greater than the
        aspirational GN set by the damage GN.
        :return: A bool value that indicates whether the said player has
        reached their GN.
        """
        if self.player.damage < self.player.gn:
            return False
        if self.player.damage > self.player.gn:
            return True
