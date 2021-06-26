from Scraper.weez_scraper import WeezScraper
from Analysis_Tools.weez_awards import WeezAwards
from Analysis_Tools.weez_analysis import GNCalculator, get_sum_dict
from Analysis_Tools.weez_reader import Player
from CommunicationTools.weez_csv_processor import WeezCSV
from CommunicationTools.emailer import Emailer
from CommunicationTools.gn_bot import GNBot
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

rumee_dict = {'name': 'Captain Ahmed', 'game_name': 'RumeeAhmed', 'platform': 'PSN'}
mike_dict = {'name': 'The Golden God', 'game_name': 'Buttpunch69#5164309', 'platform': 'activision'}
neen_dict = {'name': 'Cheen', 'game_name': 'mininick green#5504512', 'platform': 'activision'}

dict_list = [rumee_dict, mike_dict, neen_dict]

message_list = []
player_list = []
for player_dict in dict_list:
    player = Player(player_dict['name'])
    scraper = WeezScraper(player_dict['game_name'], player_dict['platform'])
    scraper.scrape()

    overall_dict = scraper.overall_stats
    matches_dict = scraper.match_stats
    sum_dict = get_sum_dict(player, matches_dict)
    player.add_dicts(overall_dict, sum_dict)

    gn_calc = GNCalculator(player)
    player.gn = gn_calc.get_damage_gn()
    player.judge = gn_calc.gn_judgement()

    player_list.append(player)
    stats = player.get_stats()
    message_list.append(stats)

awards = WeezAwards(player_list)
awards.process_player_stats()
message_list.append(awards.show_results())

weez_csv = WeezCSV(player_list)
weez_csv.create_csv()

emailer = Emailer(EMAIL, PASSWORD, 'Nickgreen100@hotmail.co.uk', 'WeezingtonSilva', 'weez.csv')
emailer.send_email('smtp.gmail.com', 587)

bot = commands.Bot(command_prefix='!')
bot.add_cog(GNBot(bot, message_list))
bot.run(GNBot.token)
