from AnalysisTools.weez_analysis import GNCalculator
from AnalysisTools.weez_reader import Player, Team
from DataTools.weez_database import WeezDatabase
from AnalysisTools.weez_awards import WeezAwards
from Scraper.weez_scraper import WeezScraper
from DataTools.gn_bot import GNBot
from discord.ext import commands
import sys

#  Create the player dicts with game details
rumee_dict = {
    'name': 'Captain Ahmed', 'game_name': 'RumeeAhmed', 'platform': 'PSN'
}
neen_dict = {
    'name': 'Cheen', 'game_name': 'mininick green#5504512', 'platform': 'atvi'
}
tibbey_dict = {
    'name': 'Alex Ceferin', 'game_name': 'tibbey#5419185', 'platform': 'atvi'
}
mike_dict = {
    'name': 'The Golden God',
    'game_name': 'Buttpunch69#5164309',
    'platform': 'atvi'
}
dict_list = [rumee_dict, mike_dict, neen_dict]

message_list = []
player_list = []
for player_dict in dict_list:
    # Scrape the player stats.
    scraper = WeezScraper(player_dict['game_name'], player_dict['platform'])
    scraper.scrape()

    # Get the overall and match stats and process them.
    player = Player(player_dict['name'])
    player.process_stats(scraper.stats)

    # Calculate the GN for and judge each player.
    gn_calc = GNCalculator(player)
    player.gn = gn_calc.get_damage_gn()
    player.judge = gn_calc.gn_judgement()

    # Add each player to a list and get the stats and messages.
    player_list.append(player)
    stats = player.get_stats()
    message_list.append(stats)
    message_list.append('-' * 60)

# Process the awards and add them to the messages list.
awards = WeezAwards(player_list)
awards.process_player_stats()
message_list.append(awards.show_player_results())

# Initialise the team object and process the team stats.
team = Team(player_list)
team.process_team_stats()

# Initialise and upload the data to the Firebase database.
db = WeezDatabase()
db.add_games(player_list)
db.add_awards(awards)
db.add_team(team)

# Initialise the bot and then pass through the message list to be printed in
# the Discord channel.
bot = commands.Bot(command_prefix='!')
bot.add_cog(GNBot(bot, message_list))
bot.run(GNBot.token)
bot.close()

# Exit the program
sys.exit()
