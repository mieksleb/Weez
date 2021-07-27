from Analysis_Tools.weez_awards import WeezAwards
from Analysis_Tools.weez_reader import Player
from dotenv import load_dotenv
import pyrebase
import os
load_dotenv()


class WeezDatabase:
    """
    Object that handles data storage into Firebase.
    """

    API_KEY = os.getenv('API_KEY')
    AUTH_DOMAIN = os.getenv('AUTH_DOMAIN')
    DATABASE_URL = os.getenv('DATABASE_URL')
    PROJECT_ID = os.getenv('PROJECT_ID')
    STORAGE_BUCKET = os.getenv('STORAGE_BUCKET')
    MESSAGING_SENDER_ID = os.getenv('MESSAGING_SENDER_ID')
    APP_ID = os.getenv('APP_ID')
    MEASUREMENT_ID = os.getenv('MEASUREMENT_ID')

    def __init__(self):
        self._initialize_app()
        self.db = self.firebase.database()

    def _initialize_app(self):
        """
        Load the environment variables and initialise the connection to Firebase.
        :return: None.
        """
        firebase_config = {
            'apiKey': self.API_KEY,
            'authDomain': self.AUTH_DOMAIN,
            'databaseURL': self.DATABASE_URL,
            'projectId': self.PROJECT_ID,
            'storageBucket': self.STORAGE_BUCKET,
            'messagingSenderId': self.MESSAGING_SENDER_ID,
            'appId': self.APP_ID,
            'measurementId': self.MEASUREMENT_ID,
        }
        self.firebase = pyrebase.initialize_app(firebase_config)

    def add_games(self, player_list: list[Player]):
        """
        Add a game session to the Firebase database under the `games` collection.
        :param player_list: a list containing player objects.
        :return: None.
        """
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

    def add_awards(self, awards: WeezAwards):
        """
        Add the awards generated from a session to the Firebase database under the`awards` collection in
        :param awards: an instance of the WeezAwards object.
        :return: None
        """
        data = {
            'bullet_bitch': awards.bullet_bitch,
            'medic': awards.medic,
            'head_master': awards.head_master,
            'top_assister': awards.head_master,
            'team_lover': awards.team_lover,
            'team_hater': awards.team_hater,
            'lethal_killer': awards.lethal_killer,
            'least_lethal_killer': awards.least_lethal_killer,
            'tank': awards.tank,
            'gummy_bear': awards.gummy_bear,
            'team_demolisher': awards.team_lover,
            'pussio': awards.pussio,
        }
        self.db.child('awards').child(awards.date).set(data)
