from AnalysisTools.weez_reader import Player
import csv


class WeezCSV:
    """
    Object that takes a Player's data and creates a csv file for recording long term data.
    """

    def __init__(self, player_list: list[Player]):
        """

        :param player_list: A list object that contains other player objects.
        """
        self.player_list = player_list

    def create_csv(self):
        """
        Create a csv based on the player data.
        :return: None
        """
        player_data = []
        for player in self.player_list:
            if player.gn:
                gn = 'TRUE'
            else:
                gn = 'FALSE'
            row = [
                player.player_name, player.date, player.games_played, player.score, player.kills, player.deaths,
                player.assists, player.kd, player.damage, player.damage_taken, player.headshots, player.revives,
                player.teams_wiped, gn
            ]
            player_data.append(row)

        with open('weez.csv', 'a', newline='') as weez_csv:
            csv_writer = csv.writer(weez_csv, delimiter=',')
            csv_writer.writerows(player_data)
