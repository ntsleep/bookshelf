from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /books/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /books/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /books/author/5/
    url(r'^author/(?P<pk>[0-9]+)/$', views.AuthorView.as_view(), name='author_detail'),
    # ex: /books/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /books/5/vote/
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
