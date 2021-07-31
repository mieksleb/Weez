from AnalysisTools.weez_awards import WeezAwards
from AnalysisTools.weez_reader import Player, Team
from firebase_admin import credentials, firestore
import firebase_admin


class WeezDatabase:
    """
    Object that handles data storage into Firebase.
    """

    def __init__(self):
        self._initialize_app()

    def _initialize_app(self) -> None:
        """
        Get the credentials, initialise the app and create a connection to the Firestore database.
        :return: None.
        """
        if not firebase_admin._apps:
            cred = credentials.Certificate('/Users/rumeeahmed/Documents/Weez/DataTools/service_key.json')
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def add_games(self, player_list: list[Player]) -> None:
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
                'gn': player.judge,
            }
            self.db.collection('games').document(player.date).collection(player.player_name).document('stats').set(game)

    def add_awards(self, awards: WeezAwards) -> None:
        """
        Add the awards generated from a session to the Firebase database under the`awards` collection in
        :param awards: an instance of the WeezAwards object.
        :return: None
        """
        data = {
            'bullet_bitch': awards.bullet_bitch,
            'medic': awards.medic,
            'head_master': awards.head_master,
            'top_assister': awards.top_assister,
            'team_lover': awards.team_lover,
            'team_hater': awards.team_hater,
            'lethal_killer': awards.lethal_killer,
            'least_lethal_killer': awards.least_lethal_killer,
            'tank': awards.tank,
            'gummy_bear': awards.gummy_bear,
            'team_demolisher': awards.team_demolisher,
            'pussio': awards.pussio,
        }
        self.db.collection('awards').document(awards.date).set(data)

    def add_team(self, team: Team) -> None:
        """
        Add the team stats generated from a session to the Firebase database under the`awards` collection in
        :param team: an instance of the Team object.
        :return: None
        """
        self._add_total_team_stats(team)
        self._add_team_stats_per_game(team)

    def _add_total_team_stats(self, team: Team) -> None:
        """
        Add the total team stats per session into the Firebase database under the `total_team_stats` Collection.
        :param team: an instance of the Team object.
        :return: None.
        """
        data = {
            'team_score': team.team_score,
            'team_kills': team.team_kills,
            'team_deaths': team.team_deaths,
            'team_assists': team.team_assists,
            'team_damage': team.team_damage,
            'team_damage_taken': team.team_damage_taken,
            'team_headshots': team.team_headshots,
            'team_revives': team.team_revives,
            'team_teams_wiped': team.team_teams_wiped,
            'team_kd_average': team.average_team_kd,
        }
        self.db.collection('total_team_stats').document(team.date).set(data)

    def _add_team_stats_per_game(self, team: Team) -> None:
        """
        Add the average team stats per game into the Firebase database under the `team_stats_per_game` collection.
        :param team: an instance of the WeezAwards object.
        :return: None.
        """
        data = {
            'team_score_per_game': round(team.team_score_per_game, 2),
            'team_kills_per_game': round(team.team_kills_per_game, 2),
            'team_deaths_per_game': round(team.team_deaths_per_game, 2),
            'team_assists_per_game': round(team.team_assists_per_game, 2),
            'team_damage_per_game': round(team.team_damage_per_game, 2),
            'team_damage_taken_per_game': round(team.team_damage_taken_per_game, 2),
            'team_headshots_per_game': round(team.team_headshots_per_game, 2),
            'team_revives_per_game': round(team.team_revives_per_game, 2),
            'teams_wiped_per_game': round(team.teams_wiped_per_game, 2),
            'team_kd_average_per_game': round(team.average_team_kd_per_game, 2),
        }
        self.db.collection('team_stats_per_game').document(team.date).set(data)
