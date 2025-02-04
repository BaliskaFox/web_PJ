class Library:
    def __init__(self):
        self.books = []

    def add_book(self,title):
        self.books.append(title)
    
    def find_book(self, find_title):
        for title in self.books:
            if title == find_title:
                return title
        raise ValueError('❌ Ошибка: Книга не найдена!')

library = Library()
library.add_book('1984')
library.add_book("Гарри Поттер")
try:
    print(library.find_book("1984"))  # ✅ Выведет: "1984"
    print(library.find_book("Властелин колец"))  # ❌ Ошибка: "Книга не найдена!
except ValueError as e:
    print(f"Ошибка: {e}")