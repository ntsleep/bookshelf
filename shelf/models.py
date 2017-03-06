from django.db import models
from django.contrib.auth.models import User
from books.models import Book

ACTION_CHOICES = (
    ('liked', 'Liked'),
    ('added', 'Added'),
    ('read', 'Read'),
    ('have', 'Have'),
)

class Shelf(models.Model):
    user = models.ForeignKey(User, unique=False)
    book = models.ForeignKey(Book, unique=False)
    action = models.CharField(max_length=200, choices=ACTION_CHOICES)
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField('date published', auto_now_add=True)
    updated_at = models.DateTimeField('date updated', auto_now_add=True)
    
    class Meta:
        unique_together = ("user", "book", "action")
    
    def __str__(self):
        return "{} {} {}".format(self.user, self.action, self.book)
