from Scraper.weez_scraper import WeezScraper
<<<<<<< HEAD
from Analysis_Tools.weez_reader import player
from Analysis_Tools.weez_analysis import get_sum_dict
from Analysis_Tools.weez_analysis import damage_gn
from Analysis_Tools.weez_analysis import gn_judgement
from Analysis_Tools.weez_analysis import bullet_bitch
=======
from Analysis_Tools.weez_reader import Player
from Analysis_Tools.weez_analysis import get_sum_dict, damage_gn, gn_judgement
>>>>>>> 31bde6d9539b19018c84db3bde17d5bd62a01998

rumee_dict = {'name': 'Captain Ahmed', 'game_name': 'RumeeAhmed', 'platform': 'PSN'}
mike_dict = {'name': 'The Golden God', 'game_name': 'Buttpunch69#5164309', 'platform': 'activision'}
neen_dict = {'name': 'Cheen', 'game_name': 'mininick green#5504512', 'platform': 'activision'}

dict_list = [rumee_dict, mike_dict, neen_dict]

# chumby = WeezScraper('RumeeAhmed','PSN')
# chumby.scrape()

<<<<<<< HEAD
# This loop is over all players and
=======
>>>>>>> 31bde6d9539b19018c84db3bde17d5bd62a01998
player_list = []
for dicto in dict_list:
    player1 = Player(dicto['name'])
    scrape = WeezScraper(dicto['game_name'], dicto['platform'])
    scrape.scrape()

    overall_dict = scrape.overall_stats
    matches_dict = scrape.match_stats
    sum_dict = get_sum_dict(player1,matches_dict)
    player1.add_dicts(overall_dict, sum_dict)

    player1.gn = damage_gn(player1)
    player1.judge = gn_judgement(player1)
<<<<<<< HEAD
    player_list.append(player1)
    player1.print_stats()

    player1.reset()



bullet_bitch(player_list)
=======
    player1.print_stats()
    player1.reset()

# for player in player_list:
#     player.print_stats()
>>>>>>> 31bde6d9539b19018c84db3bde17d5bd62a01998
