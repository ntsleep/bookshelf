from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
#from django.urls import reverse
from django.views import generic

from .models import Book


class IndexView(generic.ListView):
    template_name = 'books/index.djt'
    context_object_name = 'latest_books_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Book.objects.order_by('-created_at')[:5]
