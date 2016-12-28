from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /books/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /books/5/
#    u<rl(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /books/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /books/5/vote/
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
