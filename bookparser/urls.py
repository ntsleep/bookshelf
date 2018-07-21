from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add_author', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^add_source', views.AddSource.as_view(), name='add_source'),
]
