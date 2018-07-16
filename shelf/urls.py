from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /api/mark-read/1
    url(r'^api/mark-read/(?P<book_id>[0-9]+)$', views.mark_read, name='mark_read'),
    # ex: /api/mark/
    url(r'^api/mark$', views.mark, name='mark'),
]
