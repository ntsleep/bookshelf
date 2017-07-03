from django.contrib import admin

from .models import Author, Translator, Series, Genre, Form, Book

admin.site.register(Author)
admin.site.register(Translator)
admin.site.register(Series)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Form)
