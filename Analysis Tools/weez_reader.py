#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:11:23 2021

weez_reader.py is the reading module for weezstatz. 


MATCH class stroes the info from a particular match 

PLAYER class which contains many attributes.

@author: michaelselby
"""

import numpy as np

class Match:
    def __init__(self, playername):
        self.kills

class player:
    def __init__(self, playername,overall_dict,sum_dict):
        self.playername = playername
        self.games_played = int(overall_dict['Matches Played'])
        self.kills = int(overall_dict['Kills'])
        self.damage = int(overall_dict['Damage'].replace(',', ''))
        self.kd = float(overall_dict['K/D'])
        self.assists = int(sum_dict['Assists'])
        self.headshots = int(sum_dict['Headshots'])
        self.revives = int(sum_dict['Revives'])
        self.laststandkills = int(sum_dict['Last Stand Kills'])
        
    def new_name(self):
        return 'gary'+self.playername

    # def damage_gn(self):
    #     n = self.games_played
    #     rand = np.random.normal(1, 0.1)
    #     if (self.playername == 'ButtPunch69'):
    #         self.gn = 1000 * n * rand
    #         return self.gn
    #     else:
    #         self.gn = 750 * n * rand
    #         return self.gn
    #
    # def gn_judgement(self):
    #     if (self.damage < player.gn):
    #         judge = False
    #         return self.judge
    #     if (self.damage >= player.gn):
    #         self.judge = True
    #         return self.judge
    #     else:
    #         0

        
    
