from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^parse_url', views.parse_url, name='parse_url'),
    
]
