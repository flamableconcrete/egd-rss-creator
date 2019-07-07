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

The end result is that you can point your podcast app to this URL and it should work for all the older episodes! 
[https://raw.githubusercontent.com/flamableconcrete/egd-rss-creator/master/feed.xml](https://raw.githubusercontent.com/flamableconcrete/egd-rss-creator/master/feed.xml)

## Broken Episodes

### Incorrect Audio

* 07/04/2012 [002: Book of Mormon Lesson 25: Alma 17-22](https://engaginggospeldoctrine.org/2012/07/04/002-egd-25-alma-17-22/) - audio for episode 25. Should be `2012/07/egd-bom-025.mp3`
* 07/04/2012 [003: Book of Mormon Lesson 26: Alma 23-29](https://engaginggospeldoctrine.org/2012/07/04/003-egd-26-alma-23-29/) - audio for episode 26. Should be `2012/07/egd-bom-026.mp3`
* 06/05/2016 [195: Introspection and Atonement (BoM Gospel Doctrine Lesson 22)](https://engaginggospeldoctrine.org/2016/06/05/195_introspection_and_atonement_bom_gospel_doctrine_lesson_22/) - audio for episode 22. Should be `2019/02/egd-bom-022.mp3`

### No Audio

These episodes have no audio on their pages. All but the first and last are from 2014 (Old Testament)

* 03/01/2013 [036: Doctrine & Covenants Lesson 10: This Is My Voice unto All](https://engaginggospeldoctrine.org/2013/03/01/036-doctrine-covenants-lesson-10-this-is-my-voice-unto-all/) - Should be `2019/02/egd-dcch-010.mp3`
* **078a - 105.1**
    * 01/02/2014 [078a: This is My Work and My Glory; OT lesson 1(Full)](https://engaginggospeldoctrine.org/2014/01/02/078a-this-is-my-work-and-my-glory-ot-lesson-1full/)
    * 01/02/2014 [078b: This is My Work and My Glory; OT lesson 1(Core)](https://engaginggospeldoctrine.org/2014/01/02/078b-this-is-my-work-and-my-glory-ot-lesson-1core/)
    * 01/11/2014 [079a: Pre-Existence and Book of Abraham; OT Lesson 2 (Full)](https://engaginggospeldoctrine.org/2014/01/11/079a-pre-existence-and-book-of-abraham-ot-lesson-2-full/)
    * 01/11/2014 [079b: Pre-Existence and Book of Abraham; OT Lesson 2 (Core)](https://engaginggospeldoctrine.org/2014/01/11/079b-pre-existence-and-book-of-abraham-ot-lesson-2-core/)
    * 01/17/2014 [080.1: The Creation; OT Lesson 3 (Core)](https://engaginggospeldoctrine.org/2014/01/17/080-1-the-creation-ot-lesson-3-core/)
    * 01/17/2014 [080.2: The Creation; OT Lesson 3 (Study Notes)](https://engaginggospeldoctrine.org/2014/01/17/080-2-the-creation-ot-lesson-3-study-notes/)
    * 01/22/2014 [081.1: The Fall; OT Lesson 4 (Core)](https://engaginggospeldoctrine.org/2014/01/22/081-1-the-fall-ot-lesson-4-core/)
    * 01/22/2014 [081.2: The Fall; OT Lesson 4 (Study Notes)](https://engaginggospeldoctrine.org/2014/01/22/081-2-the-fall-ot-lesson-4-study-notes/)
    * 01/25/2014 [82.1: Cain vs. Enoch; OT Lesson 5 (Core)](https://engaginggospeldoctrine.org/2014/01/25/82-1-cain-vs-enoch-ot-lesson-5-core/)
    * 01/25/2014 [82.2: Cain vs. Enoch; OT Lesson 5 (Study Notes)](https://engaginggospeldoctrine.org/2014/01/25/82-2-cain-vs-enoch-ot-lesson-5-notes/)
    * 01/31/2014 [083.1: The Flood and Tower of Babel; OT Lesson 6 (Core)](https://engaginggospeldoctrine.org/2014/01/31/083-1-the-flood-and-tower-of-babel-ot-lesson-6-core/)
    * 01/31/2014 [083.2: The Flood and Tower of Babel; OT Lesson 6 (Study Notes)](https://engaginggospeldoctrine.org/2014/01/31/083-2-the-flood-and-tower-of-babel-ot-lesson-6-study-notes/)
    * 02/09/2014 [84.1: The Abrahamic Covenant; OT Lesson 7 (Core)](https://engaginggospeldoctrine.org/2014/02/09/84-1-the-abrahamic-covenant-ot-lesson-7-core/)
    * 02/09/2014 [84.2: The Abrahamic Covenant; OT Lesson 7 (Study Notes)](https://engaginggospeldoctrine.org/2014/02/09/84-2-the-abrahamic-covenant-ot-lesson-7-study-notes/)
    * 02/13/2014 [085.1: Living Righteously in a Wicked World; OT Lesson 8 (Core)](https://engaginggospeldoctrine.org/2014/02/13/085-1-living-righteously-in-a-wicked-world-ot-lesson-8-core/)
    * 02/13/2014 [085.2: Living Righteously in a Wicked World; OT Lesson 8 (Study Notes)](https://engaginggospeldoctrine.org/2014/02/13/085-2-living-righteously-in-a-wicked-world-ot-lesson-8-study-notes/)
    * 02/20/2014 [086:1: The Sacrifice of Isaac; OT Lesson 9 (Core)](https://engaginggospeldoctrine.org/2014/02/20/086-1-sacrifice-of-isaac-ot-lesson-9-core/)
    * 02/22/2014 [086.2: The Sacrifice of Isaac; OT Lesson 9 (Study Notes)](https://engaginggospeldoctrine.org/2014/02/22/086-2-the-sacrifice-of-isaac-ot-lesson-9-study-notes/)
    * 03/01/2014 [087.1: Birthright and Marriage in the Covenant; OT Lesson 10 (Core)](https://engaginggospeldoctrine.org/2014/03/01/087-1-birthright-and-marriage-in-the-covenant-ot-lesson-10-core/)
    * 03/02/2014 [087.2: Birthright and Marriage in the Covenant; OT Lesson 10 (Study Notes)](https://engaginggospeldoctrine.org/2014/03/02/087-2-birthright-and-marriage-in-the-covenant-ot-lesson-10-study-notes/)
    * 03/08/2014 [088.1: Sexual Morality; OT Lesson 11 (Core)](https://engaginggospeldoctrine.org/2014/03/08/088-1-sexual-morality-ot-lesson-11-core/)
    * 03/08/2014 [088.2: Sexual Morality; OT Lesson 11 (Study Notes)](https://engaginggospeldoctrine.org/2014/03/08/088-2-sexual-morality-ot-lesson-11-study-notes/)
    * 03/15/2014 [089.1: Joseph in Egypt; OT Lesson 12 (Core)](https://engaginggospeldoctrine.org/2014/03/15/089-1-joseph-in-egypt-ot-lesson-12-core/)
    * 03/18/2014 [089.2: Joseph in Egypt; OT Lesson 12 (Study Notes)](https://engaginggospeldoctrine.org/2014/03/18/089-2-joseph-in-egypt-ot-lesson-12-study-notes/)
    * 03/24/2014 [090.1: Passover and Exodus; OT Lesson 13 (Core)](https://engaginggospeldoctrine.org/2014/03/24/090-1-passover-and-exodus-ot-lesson-13-core/)
    * 03/26/2014 [090.2: Passover and Exodus; OT Lesson 13 (Study Notes)](https://engaginggospeldoctrine.org/2014/03/26/090-2-passover-and-exodus-ot-lesson-13-study-notes/)
    * 04/02/2014 [091.1: Law and Ritual; OT Lesson 14 (Core)](https://engaginggospeldoctrine.org/2014/04/02/091-1-ten-commandments-ot-lesson-14-core/)
    * 04/13/2014 [091.2: Law and Ritual; OT Lesson 14 (Study Notes)](https://engaginggospeldoctrine.org/2014/04/13/091-2-law-and-ritual-ot-lesson-14-study-notes/)
    * 04/17/2014 [092.1: Look to God and Live; OT Lesson 15 (Core)](https://engaginggospeldoctrine.org/2014/04/17/092-1-look-to-god-and-live-ot-lesson-15-core/)
    * 04/19/2014 [092.2: Look to God and Live; OT Lesson 15 (Study Notes)](https://engaginggospeldoctrine.org/2014/04/19/092-2-look-to-god-and-live-ot-lesson-15-study-notes/)
    * 04/20/2014 [093.1: I Cannot Go beyond the Word of the Lord; OT Lesson 16 (Core)](https://engaginggospeldoctrine.org/2014/04/20/093-1-i-cannot-go-beyond-the-word-of-the-lord-ot-lesson-16-core/)
    * 04/20/2014 [093.2: I Cannot Go beyond the Word of the Lord; OT Lesson 16 (Study Notes)](https://engaginggospeldoctrine.org/2014/04/20/093-2-i-cannot-go-beyond-the-word-of-the-lord-ot-lesson-16-study-notes/)
    * 05/03/2014 [094.1: Farewell of Moses; OT Lesson 17 (Core)](https://engaginggospeldoctrine.org/2014/05/03/094-1-farwell-of-moses-ot-lesson-17-core/)
    * 05/03/2014 [094.2: Farewell of Moses; OT Lesson 17 (Study Notes)](https://engaginggospeldoctrine.org/2014/05/03/094-2-farewell-of-moses-ot-lesson-17-study-notes/)
    * 05/11/2014 [095.1: Be Strong and of Good Courage; OT Lesson 18 (Core)](https://engaginggospeldoctrine.org/2014/05/11/095-1-be-strong-and-of-good-courage-ot-lesson-18-core/)
    * 05/11/2014 [095.2: Be Strong and of Good Courage; OT Lesson 18 (Study Notes)](https://engaginggospeldoctrine.org/2014/05/11/095-2-be-strong-and-of-good-courage-ot-lesson-18-study-notes/)
    * 05/14/2014 [096.1: Judges; OT Lesson 19 (Core)](https://engaginggospeldoctrine.org/2014/05/14/096-1-judges-ot-lesson-19-core/)
    * 05/14/2014 [096.2: Judges; OT Lesson 19 (Study Notes)](https://engaginggospeldoctrine.org/2014/05/14/096-2-judges-ot-lesson-19-study-notes/)
    * 05/22/2014 [097.1: Ruth, Woman of Valor; OT Lesson 20 (Core)](https://engaginggospeldoctrine.org/2014/05/22/097-1-ruth-woman-of-valor-ot-lesson-20-core/)
    * 05/22/2014 [097.2: Ruth, Woman of Valor; OT Lesson 20 (Study Notes)](https://engaginggospeldoctrine.org/2014/05/22/097-2-ruth-woman-of-valor-ot-lesson-20-study-notes/)
    * 05/27/2014 [098.1: Honoring God; OT Lesson 21 (Core)](https://engaginggospeldoctrine.org/2014/05/27/098-1-honoring-god-ot-lesson-21-core/)
    * 05/27/2014 [098.2: Honoring God; OT Lesson 21 (Study Notes)](https://engaginggospeldoctrine.org/2014/05/27/098-2-honoring-god-ot-lesson-21-study-notes/)
    * 06/10/2014 [099.1: The Rise of David; OT Lesson 22 (Core)](https://engaginggospeldoctrine.org/2014/06/10/099-1-the-rise-of-david-ot-lesson-22-core/)
    * 06/10/2014 [099.2: The Rise of David; OT Lesson 22 (Study Notes)](https://engaginggospeldoctrine.org/2014/06/10/099-2-the-rise-of-david-ot-lesson-22-study-notes/)
    * 06/14/2014 [100:1: Friendship; OT Lesson 23 (Core)](https://engaginggospeldoctrine.org/2014/06/14/1001-friendship-ot-lesson-23-core/)
    * 06/14/2014 [100:2: Friendship; OT Lesson 23 (Study Notes)](https://engaginggospeldoctrine.org/2014/06/14/1002-friendship-ot-lesson-23-study-notes/)
    * 06/17/2014 [101.1: David and Bathsheba; OT Lesson 24 (Core)](https://engaginggospeldoctrine.org/2014/06/17/101-1_david_and_bathsheba_ot_24/)
    * 06/17/2014 [101.2: David and Bathsheba; OT Lesson 24 (Study Notes)](https://engaginggospeldoctrine.org/2014/06/17/101-2-david-and-bathsheba-ot-lesson-24-study-notes/)
    * 07/02/2014 [102.1: Psalms and Gratitude; OT Lesson 25 (Core)](https://engaginggospeldoctrine.org/2014/07/02/102-1-psalms-and-gratitude-ot-lesson-25-core/)
    * 07/03/2014 [102.2: Psalms and Gratitude; OT Lesson 25 (Study Notes)](https://engaginggospeldoctrine.org/2014/07/03/102-2-psalms-and-gratitude-ot-lesson-25-study-notes/)
    * 07/13/2014 [103.1: The Wisdom and Foolishness of Solomon; OT Lesson 26 (Core)](https://engaginggospeldoctrine.org/2014/07/13/103-1-the-wisdom-and-foolishness-of-solomon-ot-lesson-26-core/)
    * 07/17/2014 [103.2: The Wisdom and Foolishness of Solomon; OT Lesson 26 (Study Notes)](https://engaginggospeldoctrine.org/2014/07/17/103-2-the-wisdom-and-foolishness-of-solomon-ot-lesson-26-study-notes/)
    * 07/18/2014 [104.1: Wicked and Righteous Leaders; OT Lesson 27 (Core)](https://engaginggospeldoctrine.org/2014/07/18/104-1-wicked-and-righteous-leaders-ot-lesson-27-core/)
    * 07/18/2014 [104.2: Wicked and Righteous Leaders; OT Lesson 27 (Study Notes)](https://engaginggospeldoctrine.org/2014/07/18/104-2-wicked-and-righteous-leaders-ot-lesson-27-study-notes/)
    * 07/25/2014 [105.1: Elijah and the Still Small Voice; OT Lesson 28 (Core)](https://engaginggospeldoctrine.org/2014/07/25/105-1-elijah-and-the-still-small-voice-ot-lesson-28-core/)
* **109.1 - 113.2**
    * 08/14/2014 [109.1: Job; OT Lesson 32 (Core)](https://engaginggospeldoctrine.org/2014/08/14/109-1-job-ot-lesson-32-core/)
    * 08/15/2014 [109.2: Job; OT Lesson 32 (Study Notes)](https://engaginggospeldoctrine.org/2014/08/15/109-2-job-ot-lesson-32-study-notes/)
    * 08/23/2014 [110.1: Jonah and Micah; OT Lesson 33 (Core)](https://engaginggospeldoctrine.org/2014/08/23/110-1-jonah-micah-ot-lesson-33-core/)
    * 08/24/2014 [110.2: Jonah and Micah; OT Lesson 33 (Study Notes)](https://engaginggospeldoctrine.org/2014/08/24/110-2-jonah-and-micah-ot-lesson-33-study-notes/)
    * 09/01/2014 [111.1: Hosea: Fidelity to God and Each Other; OT Lesson 34 (Core)](https://engaginggospeldoctrine.org/2014/09/01/111-1-hosea-fidelity-to-god-and-each-other-ot-lesson-34-core/)
    * 09/01/2014 [111.2: Hosea: Fidelity to God and Each Other; OT Lesson 34 (Study Notes)](https://engaginggospeldoctrine.org/2014/09/01/111-2-hosea-fidelity-to-god-and-each-other-ot-lesson-34-study-notes/)
    * 09/05/2014 [112.1: Prophets and Social Justice. Amos and Joel; OT Lesson 35 (Core)](https://engaginggospeldoctrine.org/2014/09/05/prophets-and-social-justice-amos-and-joel-ot-lesson-35-core/)
    * 09/05/2014 [112.2: Prophets and Social Justice. Amos and Joel; OT Lesson 35 (Study Notes)](https://engaginggospeldoctrine.org/2014/09/05/112-2-prophets-and-social-justice-amos-and-joel-ot-lesson-35-study-notes/)
    * 09/15/2014 [113.1: Introduction to Isaiah; OT Lesson 36 (Core)](https://engaginggospeldoctrine.org/2014/09/15/113-1-introduction-to-isaiah-ot-lesson-36-core/)
    * 09/16/2014 [113.2: Introduction to Isaiah; OT Lesson 36 (Study Notes)](https://engaginggospeldoctrine.org/2014/09/16/113-2-introduction-to-isaiah-ot-lesson-36-study-notes/)
* 10/01/2014 [115.2: Beside Me There Is No Savior; OT Lesson 38 (Study Notes)](https://engaginggospeldoctrine.org/2014/10/01/115-2-beside-me-there-is-no-savior-ot-lesson-38-study-notes/)
* 10/10/2014 [116.2: Redemptive Suffering; OT Lesson 39 (Study Notes)](https://engaginggospeldoctrine.org/2014/10/10/116-2-redemptive-suffering-ot-lesson-39-study-notes/)
* 11/07/2014 [118.2: Jeremiah; OT Lesson 41 (Study Notes)](https://engaginggospeldoctrine.org/2014/11/07/118-2-jeremiah-ot-lesson-41-study-notes/)
* 11/08/2014 [119.1: Jeremiah and New Covenant; OT Lesson 42 (Core)](https://engaginggospeldoctrine.org/2014/11/08/119-1-jeremiah-and-new-covenant-ot-lesson-42-core/)
* 11/15/2014 [120.1: Ezekiel and Shepherds; OT Lesson 43 (Core)](https://engaginggospeldoctrine.org/2014/11/15/120-1-ezekiel-and-shepherds-ot-lesson-43-core/)
* 11/21/2016 [221: Remembered and Nourished (BoM Gospel Doctrine Lesson 47)](https://engaginggospeldoctrine.org/2016/11/21/221-remembered-and-nourished-bom-gospel-doctrine-lesson-47/) - doesn't have an audio player embedded in webpage either
