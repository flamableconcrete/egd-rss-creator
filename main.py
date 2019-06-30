import json

from datetime import datetime, timezone

import pytz

from feedgen.feed import FeedGenerator


def main():
    fg = FeedGenerator()
    fg.load_extension('podcast')

    fg.title('Engaging Gospel Doctrine')
    fg.link( href='https://engaginggospeldoctrine.org', rel='alternate' )
    fg.description('Engaging Gospel Doctrine provides supplementary resources for Latter-Day Saint Sunday School.')
    fg.podcast.itunes_category('Religion & Spirituality', 'Christianity')

    episodes = []
    with open('output.json') as json_file:
        data = json.load(json_file)
        for entry in data:
            url = entry['link']
            url_date = url[35:45]

            entry['pubDate'] = datetime.strptime(url_date, '%Y/%m/%d').replace(tzinfo=timezone.utc)

            episodes.append(entry)

        episodes = sorted(data, key=lambda k: (k['pubDate'], k['title'] ))

        for episode in episodes:

            fe = fg.add_entry()
            fe.id(episode['link'])
            fe.title(episode['title'])
            fe.description(episode['description'])
            fe.enclosure(episode['audio_url'], 0, 'audio/mpeg')
            fe.link(href=episode['link'])
            fe.published(episode['pubDate'])

    fg.rss_str(pretty=True)
    fg.rss_file('podcast.xml')

if __name__ == "__main__":
    main()

