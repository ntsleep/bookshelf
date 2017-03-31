from shelf.models import Shelf
from shelf.models import ACTION_CHOICES
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
    
    if request.POST['action'] not in ACTION_CHOICES:
        return JsonResponse({'error' : 1, 'message' : 'Invalid action'})
    
    book = Book.objects.get(pk = request.POST['book_id'])
    current_user = request.user
    
    action_date = request.POST['date'] if request.POST['date'] else datetime.date.today()

    shelf, created = Shelf.objects.get_or_create(
        user = current_user,
        book = book,
        action = request.POST['action'],
        defaults={'date': action_date}
    )
    
    data = {
        'shelf' : shelf.id,
        'new' : created,
        'user' : "{}".format(current_user.username),
        'success' : 1 
    }
    
    return JsonResponse(data)
