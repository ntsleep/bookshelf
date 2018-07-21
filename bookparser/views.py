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
