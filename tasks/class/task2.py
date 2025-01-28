from task1_osn import Book

class EBook(Book):
    def download_book(self):
        print(f"Вы скачиваете книгу '{self.book_name}'")

e_book = EBook("Сияние", "Стивен кинг", 300)
e_book.get_info()
e_book.download_book()

