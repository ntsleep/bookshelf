from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^api/mark-read/(?P<book_id>[0-9]+)$', views.mark_read, name='mark_read'),
   # ex: /books/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /books/5/vote/
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
