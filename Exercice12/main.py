class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []
	self.borrow_books = []
		
    # Ajouter les méthodes ici
    def add_book(self, book):
        """
        Ajoute un livre à la bibliothèque.
        """
        self.books.append(book)

    def remove_book(self, book_title):
        """
        Supprime un livre de la bibliothèque par son titre.
        """
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return

    def borrow_book(self, book_title):
        """
        Emprunte un livre disponible.
        """
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_books_list.append(book)
                return

    def return_book(self, book_title):
        """
        Rend un livre emprunté.
        """
        for book in self.borrowed_books_list:
            if book.title == book_title:
                self.borrowed_books_list.remove(book)
                self.books.append(book)
                return

    def available_books(self):
        """
        Retourne la liste des titres disponibles.
        """
        return [book.title for book in self.books]

    def borrowed_books(self):
        """
        Retourne la liste des titres empruntés.
        """
        return [book.title for book in self.borrowed_books_list]
