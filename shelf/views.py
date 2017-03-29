from shelf.models import Shelf
from books.models import Book
from django.http import JsonResponse
import datetime

def mark_read(request, book_id):
    
    book = Book.objects.get(pk=book_id)
    current_user = request.user

    shelf, created = Shelf.objects.get_or_create(
        user = current_user,
        book = book,
        action = 'read',
        defaults={'date': datetime.date.today()}
    )
    
    data = {
        'shelf' : shelf.id,
        'new' : created,
        'user' : "{}".format(current_user.username),
        'success' : 1 
    }
    
    return JsonResponse(data)

def mark(request):
    
    book = Book.objects.get(pk = request.POST['book_id'])
    current_user = request.user

    shelf, created = Shelf.objects.get_or_create(
        user = current_user,
        book = book,
        action = request.POST['action'],
        defaults={'date': request.POST['date']}
    )
    
    data = {
        'shelf' : shelf.id,
        'new' : created,
        'user' : "{}".format(current_user.username),
        'success' : 1 
    }
    
    return JsonResponse(data)
