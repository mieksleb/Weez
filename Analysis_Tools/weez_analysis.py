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
import pickle

# match = open('match_stats', 'rb')
# match_dict = pickle.load(match)
# overall = open('overall_stats', 'rb')
# overall_dict = pickle.load(overall)
# rumee = player('Rumee')


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
            value = float(match_stats[0][keyname])
            sum_keys.append(keyname)
        except:
            0

    for keyname in sum_keys:
        sum_value = 0
        for i in range(0,nmatches-1):
            try:
                value = match_stats[i][keyname].replace(',', '')
                value = float(match_stats[i][keyname])
            except:
                value = 0
            sum_value += value
        total_dict[keyname] = sum_value

    return total_dict


# generates the damage gn for a given player. There is a extra penalty for superior players.
def damage_gn(player: Player) -> float:
    n = player.games_played
<<<<<<< HEAD
    rand = np.random.normal(1,0.1)
=======
    rand = np.random.normal(1, 0.1)
>>>>>>> 31bde6d9539b19018c84db3bde17d5bd62a01998
    if player.playername == 'ButtPunch69':
        return 900*n*rand
    else:
        return 750*n*rand


<<<<<<< HEAD
def gn_judgement(player):
=======

def gn_judgement(player: Player) -> bool:
>>>>>>> 31bde6d9539b19018c84db3bde17d5bd62a01998
    if player.damage < player.gn:
        return False
    if player.damage > player.gn:
        return True

<<<<<<< HEAD

def bullet_bitch(player_list):
    max = 0
    for player in player_list:
        d = player.damage_taken
        if d > max:
            bitch = player.playername
            max = d
        else:
            0
    print(bitch + " is the bullet bitch")




=======
# rumee.judge = gn_judgement(rumee)
>>>>>>> 31bde6d9539b19018c84db3bde17d5bd62a01998
