from Scraper.weez_scraper import WeezScraper
from GNBot.gn_bot import GNBot

rumee = WeezScraper('RumeeAhmed', 'PS')
rumee.scrape()
print(rumee.overall_stats)
print(rumee.match_stats)
