from scrapy import Field, Item


class EpisodeItem(Item):
    title = Field()
    link = Field()
    audio_url = Field()
    description = Field()

