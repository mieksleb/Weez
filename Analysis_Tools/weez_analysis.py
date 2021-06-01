#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:09:23 2021

weez_analysis.py is a python3 script which processes a weez players' peformance across a time-period and
deliver judgement.


@author: michaelselby
"""
from Analysis_Tools.weez_reader import player
import numpy as np
import pickle

# match = open('match_stats', 'rb')
# match_dict = pickle.load(match)
# overall = open('overall_stats', 'rb')
# overall_dict = pickle.load(overall)
# rumee = player('Rumee')


def get_sum_dict(player,match_stats):
    """
    Function which takes a player class and a list of match dictionaries and returns the a dictionary of the sum, with an extra key for matches played
    Note that for things like KD, the sum is a useless_quantity and should be sourced from the player_stats
    :return: a player dictionary of totals
    """
    nmatches = len(match_stats)
    total_dict = {}
    total_dict['Name'] = player.playername

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
                value = match_stats[0][keyname].replace(',', '')
                value = float(match_stats[0][keyname])
            except:
                0
            sum_value += value
        total_dict[keyname] = sum_value

    return total_dict


# rumee_sum_dict = get_sum_dict(rumee,match_dict)
# print(rumee_sum_dict)
# print(overall_dict)
#
#
# match.close()
# overall.close()

'''
Now we want to convert the total_dict and summary_dict into a player_class
'''

# rumee.add_dicts(overall_dict,rumee_sum_dict)


# generates the damage gn for a given player. There is a extra penalty for superior players.
def damage_gn(player):
    n = player.games_played
    rand = np.random.normal(1,0.1)
    if (player.playername=='ButtPunch69'):
        return 900*n*rand
    else:
        return 750*n*rand

# rumee.gn = damage_gn(rumee)

def gn_judgement(player):
    if (player.damage < player.gn):
        return False
    if (player.damage > player.gn):
        return True

# rumee.judge = gn_judgement(rumee)

