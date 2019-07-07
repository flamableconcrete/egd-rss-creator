import json

from datetime import datetime
import xml.dom.minidom

from feedgen.feed import FeedGenerator
from pytz import timezone

PODCAST_FEED_FILE = 'feed.xml'


def make_xml_pretty():
    dom = xml.dom.minidom.parse(PODCAST_FEED_FILE)
    pretty_xml_as_string = dom.toprettyxml()

    with open(PODCAST_FEED_FILE, "w") as myfile:
        myfile.write(pretty_xml_as_string)


def main():
    fg = FeedGenerator()
    fg.load_extension('podcast')

    fg.title('Engaging Gospel Doctrine: Older episodes')
    fg.link( href='https://engaginggospeldoctrine.org', rel='alternate' )
    fg.description('Engaging Gospel Doctrine provides supplementary resources for Latter-Day Saint Sunday School.')
    fg.podcast.itunes_category('Religion & Spirituality', 'Christianity')

    episodes = []
    eastern = timezone('US/Mountain')
    date_cutoff = eastern.localize(datetime(2018, 1, 18))
    with open('output.json') as json_file:
        data = json.load(json_file)
        for entry in data:
            url = entry['link']
            url_date = url[35:45]
            entry['pubDate'] = eastern.localize(datetime.strptime(url_date, '%Y/%m/%d'))

            episodes.append(entry)

        episodes = sorted(data, key=lambda k: (k['pubDate'], k['title'] ))

        for episode in episodes:
            episode_num = episode['title'].split(':')[0]

            if episode['pubDate'].date() > date_cutoff.date():
                continue
            if episode_num == 'Gospel Doctrine Lesson 1':
                continue

            print(f"{episode_num} - {episode['pubDate'].strftime('%m/%d/%Y')} (audio) {episode['audio_url']} --- (link) {episode['link']} --- {episode['title']}")
            # print(f"* {episode['pubDate'].strftime('%m/%d/%Y')} [{episode['title']}]({episode['link']})")
            fe = fg.add_entry()
            fe.id(episode['link'])
            fe.title(episode['title'])
            fe.description(episode['description'])
            fe.enclosure(episode['audio_url'], 0, 'audio/mpeg')
            fe.link(href=episode['link'])
            fe.published(episode['pubDate'])

    fg.rss_str(pretty=True)
    fg.rss_file(PODCAST_FEED_FILE)

    make_xml_pretty()


if __name__ == "__main__":
    main()

