from Scraper.weez_scraper import WeezScraper
import pickle

# rumee = WeezScraper('RumeeAhmed', 'PS')
# rumee.scrape()
# print(rumee.overall_stats)
# print(rumee.match_stats)

# with open('overall_stats', 'wb') as overall_file:
#     pickle.dump(rumee.overall_stats, overall_file)
#
# with open('match_stats', 'wb') as match_file:
#     pickle.dump(rumee.match_stats, match_file)


with open('overall_stats', 'rb') as overall_file:
    file = pickle.load(overall_file)
    print(file)

with open('match_stats', 'rb') as match_file:
    file = pickle.load(match_file)
    for i in file:
        print(i)
        print()
