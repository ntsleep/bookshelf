from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime

import re
import locale

class FantlabParser():
    
    def fetch_author_data(url):
        """Loads author data by URL;
        Returns success, encoding, parsed elements"""


        try:
            resource = urlopen(url)
            encoding = resource.headers.get_content_charset()

            soup = BeautifulSoup(resource,'html.parser')

            name, middle, surname = soup.title.string.partition(" ")

            name_raw = soup.find("h1", {"itemprop" : "name"}).string
            name_orig_raw = name_raw[name_raw.find("(")+1 : name_raw.find(")")]
            name_orig, middle, surname_orig = name_orig_raw.partition(" ")

            birth_date = soup.find("meta", {"itemprop" : "birthDate"}).findParent("td").text.strip()

            locale.setlocale(locale.LC_TIME, "ru_RU.utf8") #17 марта 1948 г.
            d = {'января': 'январь', 'марта': 'март', 'декабря': 'декабрь'}
            for k, v in d.items():
                birth_date = birth_date.replace(k, v)
            birth_date_obj = datetime.strptime(birth_date , '%d %B %Y г.')

            raw_biography = soup.find("div", {"class" : "person-info-bio"})
            biography = ("".join(bio.text for bio in raw_biography.findChildren()))

            img = raw_biography.find("img")
            photo = img['src']

            elements = {
                'name': name,
                'surname': surname,
                'name_orig': name_orig,
                'surname_orig': surname_orig,
                'birth_date': birth_date_obj,
                'biography': biography,
                'photo':photo,

            }

            success = True
            return success, encoding, elements
        except Exception as e:
            print ("ERROR: can`t open URL: %s with error %s" % (url, e))
            return False, "", [e]
        
    def fetch_book_data(url):
        """Loads HTML data by URL;
        Returns success, encoding, parsed elements"""


        try:
            resource = urlopen(url)
            encoding = resource.headers.get_content_charset()

            soup = BeautifulSoup(resource,'html.parser')

            raw_description = soup.find("span", {"itemprop" : "description"})
            description = ("".join(desc.string for desc in raw_description.findChildren()))

            author_tag = soup.find("span", {"itemprop" : "author"})
            authors = [author.string for author in author_tag.findChildren()]

            title_tag = soup.find("span", {"itemprop" : "name"})
            title = title_tag.string
            title_orig = title_tag.parent.findNext('p').string

            genre_box = soup.find(text = re.compile('Жанры')).parent
            genres = [genre.string for genre in genre_box.findAll("a",recursive=False)]

            translator = soup.find("a", {"href" : re.compile('translator')}).text

            publication_date = soup.find("span", {"itemprop" : "datePublished"}).text

            series_box = soup.find(text = re.compile('Входит в')).parent.findNext('div')
            seriess = [series.string for series in series_box.findAll('a')]

            elements = {
                'title': title,
                'title_orig': title_orig,
                'authors': authors,
                'translator': translator,
                'genre': genres,
                'publication_date': publication_date,
                'seriess': seriess,
                'description': description,

            }

            success = True
            return success, encoding, elements
        except Exception as e:
            print ("ERROR: can`t open URL: %s with error %s" % (url, e))
            return False, "", [e]
    