# WeezingtonSilva
Welcome to WeezToolz. If you have found this, you are almost certainly lost. Please turn back now otherwise
go straight to the Gulag. Do not collect 200.

---

## Usage

### WeezScraper
WeezScraper is the object responsible for scraping a players stats for their most recent session. This class
is a subclass of the driver.Chrome object from the Selenium library. The first two parameters required when
the class is instantiated are the players' username, and the gaming platform the player belongs to. For now
only PlayStation and Activision is supported. Acceptable strings for the `platform` parameter are `PS` and
`activision`.

```python
rumee = WeezScraper('RumeeAhmed', 'PS')
```

To run the program use the scrape method. This is designed to scrape all the daily data from the Warzone
tracker website and return the raw data with minimal user input. Simply execute the scrape method and let
the boys drop in and claim the GN.
```python
rumee.scrape()
```

---
