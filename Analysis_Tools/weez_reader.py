#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:11:23 2021

weez_reader.py is the reading module for weezstatz. 


MATCH class stroes the info from a particular match 

PLAYER class which contains many attributes.

@author: michaelselby
"""


class Player:
    def __init__(self, playername: str):
        self.playername = playername

    def add_dicts(self, overall_dict: dict, sum_dict: dict):
        self.games_played = int(overall_dict.get('Matches Played', 0))
        self.kills = int(overall_dict.get('Kills', 0))
        self.deaths = int(sum_dict.get('Deaths', 0))
        self.damage = int(overall_dict.get('Damage', 0).replace(',', ''))
        self.damage_taken = int(sum_dict.get('Damage Taken', 0))
        self.score = int(sum_dict.get('Score', 0))
        self.teams_wiped = int(sum_dict.get('Teams Wiped', 0))
        self.kd = float(overall_dict.get('K/D', 0))
        self.assists = int(sum_dict.get('Assists',0))
        self.headshots = int(sum_dict.get('Headshots', 0))
        self.revives = int(sum_dict.get('Revives', 0))
        self.laststandkills = int(overall_dict.get('Last Stand Kills', 0))

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

    def print_stats(self):
        print('Stats for ' + str(self.playername))
        print(str(self.games_played) + ' games played')
        print('Score: '+ str(self.score))
        print(str(self.kills)+' kills')
        print(str(self.deaths) + ' deaths')
        print(str(self.assists) + ' assists')
        print(str(self.damage) + ' damage')
        print(str(self.damage_taken) + ' damage received')
        print(str(self.kd) + ' KD')
        print(str(self.headshots) + ' headshots')
        print(str(self.revives) + ' revives')
        print(str(self.teams_wiped) + ' team wipes')
        if (self.judge==True):
            print(self.playername+' has hit his gn')
        else:
            print(self.playername + ' has not hit his gn')


