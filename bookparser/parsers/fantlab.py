import locale
import re
from datetime import datetime
from urllib.request import urlopen

from bs4 import BeautifulSoup


class FantlabParser:
    def fetch_author_data(self, url):
        """Loads author data by URL;
        Returns success, encoding, parsed elements"""

        try:
            resource = urlopen(url)
            encoding = resource.headers.get_content_charset()

            soup = BeautifulSoup(resource, 'html.parser')

            name, middle, surname = soup.title.string.partition(" ")

            name_raw = soup.find("h1", {"itemprop": "name"}).string
            name_orig_raw = name_raw[name_raw.find("(") + 1: name_raw.find(")")]
            name_orig, middle, surname_orig = name_orig_raw.partition(" ")

            birth_date_raw = soup.find("meta", {"itemprop": "birthDate"}).findParent("td").text.strip()
            birth_date = self.convert_birth_date(birth_date_raw)

            raw_biography = soup.find("div", {"class": "person-info-bio"})
            biography = ("".join(bio.text for bio in raw_biography.findChildren()))

            img = raw_biography.find("img")

            photo = img.get('img') if img else None

            elements = {
                'name': name,
                'surname': surname,
                'name_orig': name_orig,
                'surname_orig': surname_orig,
                'birth_date': birth_date,
                'biography': biography,
                'photo': photo,

            }

            success = True
            return success, encoding, elements
        except Exception as e:
            print("ERROR: can`t open URL: %s with error %s" % (url, e))
            return False, "", [e]

    @staticmethod
    def fetch_book_data(url):
        """Loads HTML data by URL;
        Returns success, encoding, parsed elements"""

        try:
            resource = urlopen(url)
            encoding = resource.headers.get_content_charset()

            soup = BeautifulSoup(resource, 'html.parser')

            raw_description = soup.find("span", {"itemprop": "description"})
            description = ("".join(desc.string for desc in raw_description.findChildren()))

            author_tag = soup.find("span", {"itemprop": "author"})
            authors = [author.string for author in author_tag.findChildren()]

            title_tag = soup.find("span", {"itemprop": "name"})
            title = title_tag.string
            title_orig = title_tag.parent.findNext('p').string

            genre_box = soup.find(text=re.compile('Жанры')).parent
            genres = [genre.string for genre in genre_box.findAll("a", recursive=False)]

            translator = soup.find("a", {"href": re.compile('translator')}).text

            publication_date = soup.find("span", {"itemprop": "datePublished"}).text

            series_box = soup.find(text=re.compile('Входит в')).parent.findNext('div')
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
            print("ERROR: can`t open URL: %s with error %s" % (url, e))
            return False, "", [e]

    @staticmethod
    def convert_birth_date(birth_date_raw):
        locale.setlocale(locale.LC_TIME, "ru_RU.utf8")

        try:
            return datetime.strptime(birth_date_raw, '%d %B %Y г.')
        except ValueError:
            return ""
