from Scraper.weez_scraper import WeezScraper

rumee = WeezScraper('RumeeAhmed', 'PS')
rumee.scrape()
print(rumee.overall_stats)
print(rumee.match_stats)
