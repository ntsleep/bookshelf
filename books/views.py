from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Book, Author


class IndexView(generic.ListView):
    template_name = 'books/index.djt'
    context_object_name = 'latest_books_list'

    def get_queryset(self):
        """Return the last five published books."""
        return Book.objects.order_by('-created_at')[:5]
    

class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.djt'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Book.objects
    
class AuthorView(generic.DetailView):
    model = Author
    template_name = 'books/author_detail.djt'
    
    def get_queryset(self):
        return Author.objects
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AuthorView, self).get_context_data(**kwargs)
        author = super(AuthorView, self).get_object()
        
        context['books'] = Book.objects.filter(authors__id=author.id)
        return context

