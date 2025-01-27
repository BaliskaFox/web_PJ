class Book:
    def __init__(self, book_name,avtor_name):
        self.book_name = book_name
        self.avtor_name = avtor_name
        self.is_read = False
    
    def read_book(self):
        self.is_read = True
        print(f"Вы читаете книгу -- {self.book_name} от автора -- {self.avtor_name}")
    
    def get_info(self):
        status = "Прочитана" if self.is_read else "Не прочитана"
        print(f"Название -- {self.book_name}, Автор -- {self.avtor_name}, Статус: {status}")

my_book = Book("Мастер и маргарита", "Михаил Булгаков")
my_book.read_book()

information = my_book.get_info()
print(information)