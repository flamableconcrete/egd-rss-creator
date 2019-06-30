import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from  engaging_gospel_doctrine_scraper.items import EpisodeItem 


class ExampleSpider(CrawlSpider):
    name = 'egd'
    allowed_domains = ['engaginggospeldoctrine.org']
    start_urls = [
        'https://engaginggospeldoctrine.org/',
        #'https://engaginggospeldoctrine.org/2019/04/19/329-atoning-human-nature-bonus-episode/'
    ]

    rules = (
        # Extract links matching 'page/<pagenumber>/'
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=r'page/\d*/')),
        #Rule(LinkExtractor(allow=r'page/2/')),

        # Extract links matching 'YYYY/MM/DD' and parse them with the spider's method parse_episode
        Rule(LinkExtractor(allow=(r'(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})', )), callback='parse_episode'),
    )

    def foo():
        pass


    def parse_episode(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        #audio_url = response.css('article div div div figure audio::attr(src)').get()
        #audio_url = response.css('audio::attr(src)').get()

        episode = EpisodeItem(
            title=extract_with_css('.entry-title::text'),
            link=response.url,
	    audio_url=extract_with_css('figure audio::attr(src)'),
	    description=extract_with_css('div.entry-content p::text')

        )

        if (not episode.get('title', None)) or \
           (not episode.get('audio_url', None)):
            print('No title or audio URL. return??')
            return

        yield episode

