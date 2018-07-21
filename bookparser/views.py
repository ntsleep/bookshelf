from django.http import JsonResponse
from django.urls import reverse
from django.views.generic import FormView, CreateView

from bookparser.forms import SourceLinkForm
from bookparser.parsers.fantlab import FantlabParser
from books.models import Author


class AuthorCreate(CreateView):
    model = Author
    template_name = 'bookparser/author_form.djt'
    fields = ['name', 'name_orig', 'surname', 'surname_orig', 'birth_date', 'biography']

    def get_initial(self):
        url = self.request.GET.get("url")
        success, encoding, initial = FantlabParser().fetch_author_data(url)

        if success:
            return initial
        else:
            return {}

    def get_success_url(self):
        return reverse('books:authors_list')


class AddSource(FormView):
    template_name = 'bookparser/add_source.djt'
    form_class = SourceLinkForm


def parse_url(request):
    """Getting title, encoding, H1 after timeshift"""

    #    url = "https://fantlab.ru/work2654" #Neuromancer
    #    url = "https://fantlab.ru/work4065" #Роберт Асприн, Линда Эванс «Разведчики времени»

    #    url = "https://fantlab.ru/autor111" #Уильям Гибсон (William Gibson)
    url = "https://fantlab.ru/autor3182"  # Chesterton

    # Getting main data from the page
    success, encoding, book = FantlabParser().fetch_author_data(url)

    args = {
        'success': success,
        'encoding': encoding,
        'book': book,
    }

    return JsonResponse(args)
