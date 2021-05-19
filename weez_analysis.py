#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:09:23 2021

weez_analysis.py is a python3 script which processes a weez players' peformance across a time-period and
deliver judgement.


@author: michaelselby
"""

import weez_reader
import numpy as np

# load in the players data

Rumee = weez_reader.Player('RumeeAhmed',4,10,3500,0.7)


# generates the damage gn for a given player. There is a extra penalty for superior players.
def damage_gn(player):
    n = player.games_played
    rand = np.random.normal(1,0.1)
    if (player.playername=='ButtPunch69'):
        return 1500*n*rand
    else:
        return 1000*n*rand
    
Rumee.gn = damage_gn(Rumee)


def gn_judgement(player):
    if (player.damage < player.gn):
        return False
    if (player.damage > player.gn):
        return True
    
judge = gn_judgement(Rumee)