from django.db import models

LANGUAGES = {
    'en': 'English',
    'ru': 'Русский',
    'de': 'German',
    'pl': 'Polish',
    'fr': 'French',  
}

class Author(models.Model):
    name = models.CharField(max_length=200)
    name_orig = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    surname_orig = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    biography = models.TextField(blank=True)
    created_at = models.DateTimeField('date published', auto_now_add=True)
    photo = models.ImageField(upload_to='authors', null=True, blank=True)
    pass

    def __str__(self):
        return "{} {}".format(self.name, self.surname)
    
class Translator(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    biography = models.TextField(blank=True)
    created_at = models.DateTimeField('date published', auto_now_add=True)
    photo = models.ImageField(upload_to='authors', null=True, blank=True)
    
    def __str__(self):
        return "{} {}".format(self.name, self.surname)

class Series(models.Model):
    title = models.CharField(max_length=255)
    title_orig = models.CharField(max_length=255)
    teaser = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    pub_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField('date published', auto_now_add=True)
    pass

    def __str__(self):
        return self.title
    
class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
class Form(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    authors = models.ManyToManyField(Author, blank=True, related_name='books')
    translators = models.ManyToManyField(Translator, blank=True, related_name='books')
    series = models.ManyToManyField(Series, blank=True, related_name='books')
    genres = models.ManyToManyField(Genre, blank=True, related_name='books')
    form = models.ForeignKey(Form, null=True, unique=False)
    title = models.CharField(max_length=255)
    title_orig = models.CharField(max_length=255)
    teaser = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    language = models.CharField(max_length=2, default='en', choices=LANGUAGES.items())
    pub_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField('date published', auto_now_add=True)
    image = models.ImageField(upload_to='books', default='/media/books/default.jpeg')
    
    def __str__(self):
        return self.title
    
