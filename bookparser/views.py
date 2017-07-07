from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic
from django.http import JsonResponse
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen


class IndexView(generic.ListView):
    template_name = 'books/index.djt'
    context_object_name = 'latest_books_list'

 
def parse_url(request):
    """Getting title, encoding, H1 after timeshift"""

#    url = "https://fantlab.ru/work2654" #Neuromancer
    url = "https://fantlab.ru/work4065" #Роберт Асприн, Линда Эванс «Разведчики времени»

    # Getting main data from the page
    success, encoding, book = fetch_data(url)


    
    args = {
        'success': success,
        'encoding': encoding,
        'book': book,
    }
    
    return JsonResponse(args)

def fetch_data(url):
    """Loads HTML data by URL;
    Returns success, title, encoding, H1"""
    
    
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
        
        genre = soup.find(text = re.compile('Жанры')) #.parent

        
        elements = {
            'title': title,
            'title_orig': title_orig,
            'authors': authors,
            'genre': genre,
            'description': description,
            
        }

        success = True
        return success, encoding, elements
    except Exception as e:
        print ("ERROR: can`t open URL: %s with error %s" % (url, e))
        return False, "", [e]
