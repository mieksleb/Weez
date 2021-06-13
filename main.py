from Scraper.weez_scraper import WeezScraper
from Analysis_Tools.weez_awards import WeezAwards
from Analysis_Tools.weez_analysis import GNCalculator, get_sum_dict
from Analysis_Tools.weez_reader import Player

rumee_dict = {'name': 'Captain Ahmed', 'game_name': 'RumeeAhmed', 'platform': 'PSN'}
mike_dict = {'name': 'The Golden God', 'game_name': 'Buttpunch69#5164309', 'platform': 'activision'}
neen_dict = {'name': 'Cheen', 'game_name': 'mininick green#5504512', 'platform': 'activision'}

dict_list = [rumee_dict, mike_dict, neen_dict]
# dict_list = [rumee_dict]

player_list = []
for player_dict in dict_list:
    player1 = Player(player_dict['name'])
    scraper = WeezScraper(player_dict['game_name'], player_dict['platform'])
    scraper.scrape()

    overall_dict = scraper.overall_stats
    matches_dict = scraper.match_stats
    sum_dict = get_sum_dict(player1, matches_dict)
    player1.add_dicts(overall_dict, sum_dict)

    gn_calc = GNCalculator(player1)

    player1.gn = gn_calc.get_damage_gn()
    player1.judge = gn_calc.gn_judgement()

    player_list.append(player1)
    player1.print_stats()

awards = WeezAwards(player_list)
awards.process_player_stats()
awards_message = awards.show_results()
print(awards_message)
