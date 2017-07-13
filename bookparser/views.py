from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic
from django.http import JsonResponse

from bookparser.parsers.fantlab import FantlabParser

class IndexView(generic.ListView):
    template_name = 'books/index.djt'
    context_object_name = 'latest_books_list'

 
def parse_url(request):
    """Getting title, encoding, H1 after timeshift"""

#    url = "https://fantlab.ru/work2654" #Neuromancer
#    url = "https://fantlab.ru/work4065" #Роберт Асприн, Линда Эванс «Разведчики времени»

    url = "https://fantlab.ru/autor111" #Уильям Гибсон (William Gibson)

    # Getting main data from the page
    success, encoding, book = FantlabParser.fetch_author_data(url)


    
    args = {
        'success': success,
        'encoding': encoding,
        'book': book,
    }
    
    return JsonResponse(args)

