from Scraper.weez_scraper import WeezScraper
from Analysis_Tools.weez_reader import player
from Analysis_Tools.weez_analysis import get_sum_dict
from Analysis_Tools.weez_analysis import damage_gn
from Analysis_Tools.weez_analysis import gn_judgement

import pickle

dict_list = []

rumee_dict = {}
rumee_dict['name'] = 'Captain Ahmed'
rumee_dict['game_name'] = 'RumeeAhmed'
rumee_dict['platform'] = 'PSN'

mike_dict = {}
mike_dict['name'] = 'The Golden God'
mike_dict['game_name'] = 'buttpunch69#516430'
mike_dict['platform'] = 'activision'

neen_dict = {}
neen_dict['name'] = 'Cheen'
neen_dict['game_name'] = 'buttpunch69#516430'
neen_dict['platform'] = 'activision'

dict_list.append(rumee_dict)
dict_list.append(mike_dict)
# dict_list.append(neen_dict)

chumby = WeezScraper('RumeeAhmed','PSN')
chumby.scrape()

player_list = []
# for dicto in dict_list:
#     print(dicto)
#     player = player(dicto['name'])
#     scrape = WeezScraper(dicto['game_name'], dicto['platform'])
#     scrape.scrape()
#
#     with open(player.playername+'overall_stats', 'wb') as overall_file:
#          pickle.dump(scrape.overall_stats, overall_file)
#
#     with open('match_stats', 'wb') as match_file:
#          pickle.dump(scrape.match_stats, match_file)
#
#     matches = open('match_stats', 'rb')
#     matches_dict = pickle.load(matches)
#     overall = open('overall_stats', 'rb')
#     overall_dict = pickle.load(overall)
#     print(matches_dict)
#     sum_dict = get_sum_dict(player,matches_dict)
#     player.add_dicts(overall_dict, sum_dict)
#
#     player.gn = damage_gn(player)
#     player.judge = gn_judgement(player)
#
#
#     matches.close()
#     overall.close()
#
#     player_list.append(player)
#     player.reset()
#
#     print(player_list[0])
#     print(player_list[1])