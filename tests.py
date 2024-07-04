import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize(
        'name',
        [
            'Гордость и предубеждение и зомби',
            'Что делать, если ваш кот хочет вас убить',
            'Три богатыря'
        ]
    )
    def test_add_new_book_add_one_books(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert len(collector.books_genre) == 1

    def test_set_book_genre_add_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        assert len(collector.books_genre) == 1

    def test_set_book_genre_not_add_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантэзи')

        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

    def test_get_book_genre_not_empty_genry(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_books_with_specific_genre_two_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

    def test_get_books_genre_not_empty_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')

        assert collector.get_books_genre() != {}

    def test_get_books_for_children_list_of_children_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Три богатыря')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Три богатыря', 'Мультфильмы')

        assert collector.get_books_for_children() == ['Три богатыря']

    def test_add_book_in_favorites_one_book_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_list_empty(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_list_two_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Три богатыря')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Три богатыря')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Три богатыря']