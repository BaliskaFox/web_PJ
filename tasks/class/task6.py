import os

class LibraryFile:
    def __init__(self):
        self.books = []
        self.load_books()
    
    def load_books(self):
        if not os.path.exists("library.txt"):
            open("library.txt", "w", encoding="utf-8").close()  # Создаём файл, если его нет

        with open("library.txt", 'r', encoding="utf-8") as file:
            self.books = [line.strip() for line in file.readlines()]  # Загружаем книги в список

        print('\n📚 Список книг:')
        
        for i, book in enumerate(self.books, start=1):
            print(f'{i}. {book}')

    def add_book(self, title):

        if title in self.books:
            print("⚠️ Такая книга уже есть в библиотеке!")
            return
        self.books.append(title)

        try:
            with open("library.txt", 'a', encoding="utf-8") as file:
                if file.tell() > 0:
                    file.write("\n")
                file.write(title)
            print('✅ Книга добавлена!')

        except:
            print("❌ Ошибка при работе с файлом!")

    def find_book(self,find_title):

        if find_title in self.books:
            return find_title
        raise ValueError('❌ Ошибка: Книга не найдена!')


l = LibraryFile()
l.add_book("Мастер и маргарита")
l.add_book("Мертвые души")
l.add_book("Мерседес")
l.add_book("Мерседес")
l.load_books()

try:
    print(l.find_book('Мертвые души'))
    print(l.find_book('1984'))
except ValueError as e:
    print(f"Ошибка: {e}")
