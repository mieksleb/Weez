from AnalysisTools.weez_awards import WeezAwards
from AnalysisTools.weez_reader import Player
from firebase_admin import credentials, firestore
import firebase_admin


class WeezDatabase:
    """
    Object that handles data storage into Firebase.
    """

    def __init__(self):

        self._initialize_app()

    def _initialize_app(self):
        """
        Get the credentials, initialise the app and create a connection to the Firestore database.
        :return: None.
        """
        if not firebase_admin._apps:
            cred = credentials.Certificate('/Users/rumeeahmed/Documents/Weez/DataTools/service_key.json')
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def add_games(self, player_list: list[Player]):
        """
        Add a game session to the Firebase database under the `games` collection.
        :param player_list: a list containing player objects.
        :return: None.
        """
        for player in player_list:
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
                'gn': player.gn,
            }
            self.db.collection('games').document(player.date).collection(player.player_name).document('stats').set(game)

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
        self.db.collection('awards').document(awards.date).set(data)
