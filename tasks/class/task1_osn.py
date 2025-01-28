class Book:
    def __init__(self, book_name,avtor_name,book_page):
        self.book_name = book_name
        self.avtor_name = avtor_name
        self.pages = book_page
        self.page_reads = 0
        self.is_read = 0
        self.raiting = None
    
    def read_book(self, page_reads_user):
        if self.page_reads + page_reads_user >= self.page_reads:
            self.page_reads = self.pages
            print(f"Вы закончили читать книгу '{self.book_name}'!")
        else:
            self.page_reads += page_reads_user
            print(f"Вы прочитали {page_reads_user} страниц. Всего прочитано: {self.page_reads} / {self.pages}. ")
    
    def get_info(self):
        status = "Прочитана" if self.is_read == self.pages else "Не прочитана"
        print(f"Название -- {self.book_name}, Автор -- {self.avtor_name}, Количество страниц -- {self.pages}, Статус: {status}")

    def set_rating(self, rating):

        if 1 <= rating <= 5:
            self.raiting = rating
            print(f"Рейтинг книги -- {self.book_name}, установлен на {rating}")
        else:
            print(f"Рейтинг должен быть от 1 до 5")

my_book = Book("Мастер и маргарита", "Михаил Булгаков", 500)
my_book.read_book(100)
my_book.read_book(400)
my_book.get_info()
my_book.set_rating(5)

