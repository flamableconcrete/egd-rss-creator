# Engaging Gospel Doctrine RSS Creator

This project is a web scraper for https://engaginggospeldoctrine.org in order to take the correct URLs from the website for older podcast episodes.
Everything prior to 1/18/2018's episode: [273.3: The Fall of Humanity (OT Gospel Doctrine Lesson 4, Study Notes)](https://engaginggospeldoctrine.org/2018/01/18/273-3-the-fall-of-humanity-ot-gospel-doctrine-lesson-4-study-notes/) doesn't show up on the official podcast feed (as of 6/30/2019).
The workaround presented in this code is to scrape the current contents of the whole site (currently it gets everything available, not just older episodes), save important information as a JSON file, then parse the JSON file into a readable podcast feed.
Here's the breakdown of how to run the code.

```
# installs python3 dependencies in the Pipfile
pipenv install
pipenv shell

# scrapes the full website, with default settings to autothrottle the traffic
scrapy crawl egd -o output.json

# generates/overwrites the podcast.xml podcast feed
python main.py
```
