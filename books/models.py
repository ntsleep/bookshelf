from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    name_orig = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    surname_orig = models.CharField(max_length=200)
    birth_date = models.DateField()
    biography = models.TextField()
    created_at = models.DateTimeField('date published')
    
    def __str__(self):
        return "{} {}".format(self.name, self.surname)

class Series(models.Model):
    title = models.CharField(max_length=255)
    title_orig = models.CharField(max_length=255)
    teaser = models.CharField(max_length=500)
    description = models.TextField()
    pub_date = models.DateField()
    created_at = models.DateTimeField('date published')
    
    def __str__(self):
        return self.title

class Book(models.Model):
    authors = models.ManyToManyField(Author)
    series = models.ManyToManyField(Series)
    title = models.CharField(max_length=255)
    title_orig = models.CharField(max_length=255)
    teaser = models.CharField(max_length=500)
    description = models.TextField()
    pub_date = models.DateField()
    isbn = models.CharField(max_length=20)
    created_at = models.DateTimeField('date published')
    
    def __str__(self):
        return self.title

