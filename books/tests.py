from django.test import TestCase
from django.urls import reverse

from books.models import Book


def create_book(title, title_orig):
    """
    Create a simple book with title and original title.
    """
    return Book.objects.create(title=title, title_orig=title_orig)


class BooksIndexViewTests(TestCase):
    def test_no_books(self):
        """
        If no books exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('books:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No books are available.")
        self.assertQuerysetEqual(response.context['latest_books_list'], [])

    def test_books_exist(self):
        """
        List of new added books is displayed on the index page.
        """
        create_book(title="Test", title_orig="Test orig")
        response = self.client.get(reverse('books:index'))
        self.assertQuerysetEqual(
            response.context['latest_books_list'],
            ['<Book: Test>']
        )
