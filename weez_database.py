import sqlite3

from Analysis_Tools.weez_reader import Player


class WeezDatabaseX:

    def __init__(self, db: str):
        """

        :param db: string object that represents the location of the database.
        """
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.create_games_table()

    def create_games_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS games "
            "(id INTEGER PRIMARY KEY, player TEXT, date TEXT, kills INTEGER, deaths INTEGER, assists INTEGER, "
            "damage INTEGER, damage_taken INTEGER, kd REAL, headshots INTEGER, revives INTEGER, teams_wiped INTEGER,"
            "gn INTEGER)"
        )
        self.commit_and_close(self.connection)

    def add_entry_to_games(
            self, player: str, date: str, kills: int, deaths: int, assists: int, damage: int, damage_taken: int,
            kd: float, headshots: int, revives: int, teams_wiped: int, gn: int
    ):
        self.cursor.execute(
            "INSERT INTO games VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?)",
            (player, date, kills, deaths, assists, damage, damage_taken, kd, headshots, revives, teams_wiped, gn)
        )
        self.commit_and_close(self.connection)

    @staticmethod
    def commit_and_close(connection):
        connection.commit()

    def __del__(self):
        self.connection.close()


db = WeezDatabaseX('weez.db')


import pyrebase




class WeezDatabase:

    def __init__(self, firebase_config: dict):
        self.firebase = pyrebase.initialize_app(firebase_config)
        self.db = self.firebase.database()

    def add_games(self, player_list: list[Player]):
        for player in player_list:
            if player.gn:
                gn = 'TRUE'
            else:
                gn = 'FALSE'

            game = {
                'games_played': player.games_played,
                'score': player.score,
                'kills': player.kills,
                'deaths': player.deaths,
                'assists': player.assists,
                'damage': player.damage,
                'damage_taken': player.damage_taken,
                'kd': player.kd,
                'headshots': player.headshots,
                'revives': player.revives,
                'teams_wiped': player.teams_wiped,
                'gn': gn,
            }
            self.db.child('games').child(player.date).child(player.player_name).set(game)
