#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:11:23 2021

weez_reader.py is the reading module for weezstatz. 


MATCH class stores the info from a particular match

PLAYER class which contains many attributes.

@author: michaelselby
"""


class Player:
    """
    Object that represents a player and their stats for the session.
    """
    def __init__(self, player_name: str):
        """

        :param player_name: The name of the player.
        """
        self.player_name = player_name
        self.gn = None

    def add_dicts(self, overall_dict: dict, sum_dict: dict):
        """
        Add the dictionary data as the player attributes.
        :param overall_dict: The dictionary object that contains the overall data for the session.
        :param sum_dict: The dictionary object that contains the sum of all the match data for the session.
        :return: None
        """
        self.games_played = int(overall_dict.get('Matches Played', 0))
        self.kills = int(overall_dict.get('Kills', 0))
        self.damage = int(overall_dict.get('Damage', 0).replace(',', ''))
        self.kd = float(overall_dict.get('K/D', 0))

        self.deaths = int(sum_dict.get('Deaths', 0))
        self.damage_taken = int(sum_dict.get('Damage Taken', 0))
        self.score = int(sum_dict.get('Score', 0))
        self.teams_wiped = int(sum_dict.get('Teams Wiped', 0))
        self.assists = int(sum_dict.get('Assists', 0))
        self.headshots = int(sum_dict.get('Headshots', 0))
        self.revives = int(sum_dict.get('Revives', 0))
        self.last_stand_kills = int(sum_dict.get('Last Stand Kills', 0))

    def new_name(self) -> str:
        return 'Gary' + self.player_name

    def get_stats(self) -> str:
        """
        Get all the Player's stats and put it into an object.
        :return: A string object containing all of the Player's stats.
        """
        if self.judge:
            gn = f'{self.player_name} has hit his GN!'
        else:
            gn = f'{self.player_name} has not hit his GN!'

        stats = f'Stats for {self.player_name}\n' \
                f'{self.games_played} games played\n' \
                f'Score: {self.score}\n' \
                f'{self.kills} Kills\n' \
                f'{self.deaths} Deaths\n' \
                f'{self.assists} Assists\n' \
                f'{self.damage} Damage\n' \
                f'{self.damage_taken} Damage Received\n' \
                f'{self.kd} KD\n'\
                f'{self.headshots} Headshots\n'\
                f'{self.revives} Revives\n'\
                f'{self.teams_wiped} Teams Wiped\n'\
                f'{self.last_stand_kills} Last Stand Kills\n'\
                f'{gn}'

        return stats
