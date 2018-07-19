from django.test import TestCase
from django.urls import reverse

from books.models import Book, Author


def create_book(title, title_orig):
    """
    Create a simple book with title and original title.
    """
    return Book.objects.create(title=title, title_orig=title_orig)


def create_author(name, name_orig, surname, surname_orig):
    """
    Create a simple book with title and original title.
    """
    return Author.objects.create(name=name, name_orig=name_orig, surname=surname, surname_orig=surname_orig)


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


class BooksDetailViewTests(TestCase):
    def test_not_existing_book(self):
        """
        If the book doesn't exist returns page 404
        """
        response = self.client.get(reverse('books:detail', args=(1,)))
        self.assertEqual(response.status_code, 404)

    def test_existing_book(self):
        """
        The detail view of the book
        """
        book = create_book(title="Test", title_orig="Test orig")
        response = self.client.get(reverse('books:detail', args=(book.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, book.title)


class AuthorsIndexViewTests(TestCase):
    def test_no_authors(self):
        """
        If no authors exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('books:authors_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No authors are available.")
        self.assertQuerysetEqual(response.context['authors_list'], [])

    def test_authors_exist(self):
        """
        List of authors.
        """
        create_author(name="A", name_orig="A", surname="Test", surname_orig="Test orig")
        response = self.client.get(reverse('books:authors_list'))
        self.assertQuerysetEqual(
            response.context['authors_list'],
            ['<Author: A Test>']
        )
