from django.contrib import admin

from .models import Author, Series, Genre, Form, Book

admin.site.register(Author)
admin.site.register(Series)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Form)
