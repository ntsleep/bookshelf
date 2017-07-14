from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic
from django.http import JsonResponse

from books.models import Author
from bookparser.parsers.fantlab import FantlabParser

class IndexView(generic.ListView):
    template_name = 'books/index.djt'
    context_object_name = 'latest_books_list'

class AuthorCreate(generic.edit.CreateView):
    model = Author
    template_name = 'bookparser/author_form.djt'
    fields = ['name', 'name_orig', 'surname', 'surname_orig', 'birth_date', 'biography']
    
    def get_initial(self):
        url = "https://fantlab.ru/autor3182"
        success, encoding, initial = FantlabParser().fetch_author_data(url)
        if(success):
            return initial
        else:
            return {}

 
def parse_url(request):
    """Getting title, encoding, H1 after timeshift"""

#    url = "https://fantlab.ru/work2654" #Neuromancer
#    url = "https://fantlab.ru/work4065" #Роберт Асприн, Линда Эванс «Разведчики времени»

#    url = "https://fantlab.ru/autor111" #Уильям Гибсон (William Gibson)
    url = "https://fantlab.ru/autor3182" #Chesterton

    # Getting main data from the page
    success, encoding, book = FantlabParser().fetch_author_data(url)


    
    args = {
        'success': success,
        'encoding': encoding,
        'book': book,
    }
    
    return JsonResponse(args)

