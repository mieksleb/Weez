#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:09:23 2021

weez_analysis.py is a python3 script which processes a weez players' performance across a time-period and
deliver judgement.


@author: michaelselby
"""
from Analysis_Tools.weez_reader import Player
import numpy as np


def get_sum_dict(player: Player, match_stats: dict) -> dict:
    """
    Function which takes a player class and a list of match dictionaries and returns the a dictionary of the sum, with
    an extra key for matches played. Note that for things like KD, the sum is a useless_quantity and should be sourced
    from the player_stats.
    :return: a player dictionary of totals.
    """
    nmatches = len(match_stats)
    total_dict = {'Name': player.playername}
    dict_keys = list(match_stats[0].keys())

    # retain only the fields which can be converted into floats and hence summed
    sum_keys = []
    for keyname in dict_keys:
        try:
            value = match_stats[0][keyname].replace(',', '')
            value = float(value)
            sum_keys.append(keyname)
        except:
            0

    for keyname in sum_keys:
        sum_value = 0
        for i in range(0, nmatches-1):
            try:
                value = match_stats[i][keyname].replace(',', '')
                value = float(match_stats[i][keyname])
            except:
                value = 0
            sum_value += value
        total_dict[keyname] = sum_value

    return total_dict


class GNCalculator:
    """
    Object that handles the GN for a given Player.
    """

    def __init__(self, player: Player):
        self.player = player

    def damage_gn(self) -> float:
        """
        Function that generates the aspirational damage GN for any given Player. There is an extra penalty for superior
        players.
        :return: An int object that represents the aspirational GN.
        """
        n = self.player.games_played
        rand = np.random.normal(1, 0.1)
        if self.player.playername == 'ButtPunch69':
            return 900 * n * rand
        else:
            return 750 * n * rand

    def gn_judgement(self) -> bool:
        """
        Function that checks whether a Players damage is greater than the aspirational GN set by the damage GN.
        :return: A bool that indicates whether the said player has reached their GN.
        """
        if self.player.damage < self.player.gn:
            return False
        if self.player.damage > self.player.gn:
            return True
