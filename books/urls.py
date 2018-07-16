from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /books/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /books/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /books/author/5/
    url(r'^author/(?P<pk>[0-9]+)/$', views.AuthorView.as_view(), name='author_detail'),
    # ex: /books/authors/
    url(r'^authors/$', views.AuthorsListView.as_view(), name='authors_list'),
]
