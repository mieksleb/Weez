from Scraper.weez_scraper import WeezScraper
from Analysis_Tools.weez_reader import Player
from Analysis_Tools.weez_analysis import *


rumee_dict = {'name': 'Captain Ahmed', 'game_name': 'RumeeAhmed', 'platform': 'PSN'}
mike_dict = {'name': 'The Golden God', 'game_name': 'Buttpunch69#5164309', 'platform': 'activision'}
neen_dict = {'name': 'Cheen', 'game_name': 'mininick green#5504512', 'platform': 'activision'}

dict_list = [rumee_dict, mike_dict, neen_dict]
# dict_list = [rumee_dict]

# chumby = WeezScraper('RumeeAhmed','PSN')
# chumby.scrape()


# This loop is over all players and

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

    player_list.append(player1)
    player1.print_stats()

bullet_bitch(player_list)
dam_eff(player_list)
tank(player_list)
medic(player_list)
team_lover(player_list)



