# WeezingtonSilva
Welcome to WeezToolz. If you have found this, you are almost certainly lost. Please turn back now otherwise
go straight to the Gulag. Do not collect 200.

![Weez](Assets/doesanyoneneedthis.jpg)


---

## Usage

### WeezScraper
WeezScraper is the object responsible for scraping a players stats for their most recent session. This class is a 
subclass of the driver.Chrome object from the Selenium library. The first two parameters required when the class is 
instantiated are the players' username, and the gaming platform the player belongs to. For now only PlayStation and 
Activision is supported. Acceptable strings for the `platform` parameter are `PS` and `activision`. Whilst the 
usernames need to be the one associated to said gaming platform.

```python
rumee = WeezScraper('RumeeAhmed', 'PS')
```

To run the program use the scrape method. This is designed to scrape all the daily data from the Warzone tracker website 
and return the raw data with minimal user input. Simply execute the scrape method and let the boys drop in and claim the
**GN**.
```python
rumee.scrape()
```

The scrape method will create two attributes containing the players' data. `overall_stats` is a dictionary object that 
contains the collated data for all the games played in the current session. `match_stats` is a list object containing 
a dictionary for each match played. The dictionaries contain detailed breakdowns of individual match statistics.

---

### get_sum_dict
This function takes the `match_stats` dictionary returned by `WeezScraper` and adds the individual match stats together.
It then returns a dictionary that contains the totals for each match stat for later analysis.

### GNCalculator

This object is responsible for calculating and then setting a Player objects GN. The `damage_gn` method calculates the
damage GN for the Player and ensures that damage hoarders will be subject to a higher standard. The `gn_judgement` will
check whether the Players total damage is greater than their assigned GN to ultimately decide whether a given player has
hit their GN.

### Player

The player object is responsible for processing the dictionaries returned from `WeezScraper` and `get_sum_dict` and
then represents the Player and their statistics which is then used for analysis against other Player objects.

### WeezAwards

The WeezAwards object is responsible for calculating the awards based on the stats for all the players. The object
requires a list object containing any number of `Player` objects. The awards are calculated and inserted into the
following attributes:
* ```self.bullet_bitch``` the Player that has received the most damage.
* ```self.medic``` the Player with the most revives.
* ```self.head_master``` the Player with the most headshots.
* ```self.to_assister``` the Player with the most assists.
* ```self.team_lover``` the Player with the most points.
* ```self.team_hater``` the Player with the least points.
* ```self.least_lethal_killer``` the Player that is the least effective. They require the most damage to kill another 
  player.
* ```self.lethal_killer``` the Player that is the most effective. They require the least damage per kill.
* ```self.tank``` the Player that requires the most damage to kill.
* ```self.gummy_bear``` the Player that requires the least damage to kill.
* ```self.team_demolisher``` the Player that has the most team wipes.
* ```self.pussio``` the Player that is the pussio.

---

### GNBot

This object is an extension of the Discord library. The primary function this serves is to deliver
judgment into the voice channel.


---