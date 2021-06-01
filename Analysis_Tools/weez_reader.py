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


class player:
    def __init__(self,playername):
        self.playername = playername

    def add_dicts(self,overall_dict,sum_dict):
        self.games_played = int(overall_dict['Matches Played'])
        self.kills = int(overall_dict['Kills'])
        self.damage = int(overall_dict['Damage'].replace(',', ''))
        self.kd = float(overall_dict['K/D'])
        self.assists = int(sum_dict['Assists'])
        self.headshots = int(sum_dict['Headshots'])
        self.revives = int(sum_dict['Revives'])
        # self.laststandkills = int(overall_dict['Last Stand Kills'])

    def reset(self):
        self.playername = ''
        self.games_played = 0
        self.kills = 0
        self.damage = 0
        self.kd = 0
        self.assists = 0
        self.headshots = 0
        self.revives = 0
        
    def new_name(self):
        return 'gary'+self.playername


        
    
