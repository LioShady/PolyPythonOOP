BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not (isinstance(id_, int) and id_ > 0):
            raise TypeError("incorrect id value")
        self.id_ = id_

        if not (isinstance(name, str)):
            raise TypeError("incorrect name value")
        self.name = name

        if not (isinstance(pages, int) and pages > 0):
            raise TypeError("incorrect pages value")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:

        return f"""{self.__class__.__name__}(id_={self.id_}, name='{self.name}', pages={self.pages})"""


# TODO написать класс Library
class Library:
    def __init__(self, books: list[Book] = []):
        if not all([isinstance(book, Book) for book in books]):
            raise TypeError("incorrect books value")
        self.books = books

    def get_next_book_id(self) -> int:
        if len(self.books) == 0:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id: int) -> int:
        if not (isinstance(id, int)):
            raise TypeError("incorrect id value")
        for index, book in enumerate(self.books):
            if book.id_ == id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
