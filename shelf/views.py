import datetime

from django.http import JsonResponse

from books.models import Book
from shelf.forms import MarkBookForm
from shelf.models import Shelf


def mark_read(request, book_id):
    book = Book.objects.get(pk=book_id)
    current_user = request.user

    shelf, created = Shelf.objects.get_or_create(
        user=current_user,
        book=book,
        action='read',
        defaults={'date': datetime.date.today()}
    )

    data = {
        'shelf': shelf.id,
        'new': created,
        'user': "{}".format(current_user.username),
        'success': 1
    }

    return JsonResponse(data)


def mark(request):
    form = MarkBookForm(request.POST)

    if not form.is_valid():
        return JsonResponse({'error': 1, 'message': dict(form.errors.items())})

    book = Book.objects.get(pk=request.POST['book_id'])
    current_user = request.user

    action_date = request.POST['date'] if request.POST['date'] else datetime.date.today()

    if request.POST['current_status'] == 'off':
        shelf, created = Shelf.objects.get_or_create(
            user=current_user,
            book=book,
            action=request.POST['action'],
            defaults={'date': action_date}
        )
    else:
        Shelf.objects.filter(
            user=current_user,
            book=book,
            action=request.POST['action'],
        ).delete()

    data = {
        'user': "{}".format(current_user.username),
        'success': 1
    }

    return JsonResponse(data)
