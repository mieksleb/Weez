#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:11:23 2021

weez_reader.py is the reading module for weezstatz. 


MATCH class stroes the info from a particular match 

PLAYER class which contains many attributes.

@author: michaelselby
"""

class Match:
    def __init__(self, playername):
        self.kills

class Player:
    def __init__(self, playername,games_played,kills,damage,kd):
        self.playername = playername
        self.games_played = games_played
        self.kills = kills
        self.damage = damage
        self.kd = kd
        
    def new_name(playername):
        return 'gary'+playername
        
    
x = Player('RumeeAhmed',4,10,3500,0.7)