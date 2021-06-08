from Scraper.weez_scraper import WeezScraper
from Analysis_Tools.weez_reader import player
from Analysis_Tools.weez_analysis import get_sum_dict
from Analysis_Tools.weez_analysis import damage_gn
from Analysis_Tools.weez_analysis import gn_judgement
from Analysis_Tools.weez_analysis import bullet_bitch

import pickle

dict_list = []

rumee_dict = {}
rumee_dict['name'] = 'Captain Ahmed'
rumee_dict['game_name'] = 'RumeeAhmed'
rumee_dict['platform'] = 'PSN'

mike_dict = {}
mike_dict['name'] = 'The Golden God'
mike_dict['game_name'] = 'Buttpunch69#5164309'
mike_dict['platform'] = 'activision'

neen_dict = {}
neen_dict['name'] = 'Cheen'
neen_dict['game_name'] = 'mininick green#5504512'
neen_dict['platform'] = 'activision'

dict_list.append(rumee_dict)
dict_list.append(mike_dict)
dict_list.append(neen_dict)

# chumby = WeezScraper('RumeeAhmed','PSN')
# chumby.scrape()

# This loop is over all players and
player_list = []
for dicto in dict_list:
    player1 = player(dicto['name'])
    scrape = WeezScraper(dicto['game_name'], dicto['platform'])
    scrape.scrape()

    overall_dict = scrape.overall_stats
    matches_dict = scrape.match_stats
    sum_dict = get_sum_dict(player1,matches_dict)
    player1.add_dicts(overall_dict, sum_dict)

    player1.gn = damage_gn(player1)
    player1.judge = gn_judgement(player1)
    player_list.append(player1)
    player1.print_stats()

    player1.reset()



bullet_bitch(player_list)