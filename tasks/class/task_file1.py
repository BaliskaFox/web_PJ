
def book_list():

    with open("books.txt", "r", encoding="utf-8") as file:
        books = file.readlines()
        print('\n📚 Список книг:')
        for i, book in enumerate(books, start=1):
            print(f'{i}. {book.strip()}')

def add_books():

    title_book = input("Введите название книги: ").strip()
    author_book = input("Введите автора книги: ").strip()

    with open("books.txt", 'a',encoding="utf-8") as file:
        if file.tell() > 0:  # Проверяем, не пуст ли файл
            file.write("\n")  
        file.write(f"{title_book} -- {author_book}")
    print('✅ Книга добавлена!')

def find_book():
    """Ищет книгу в файле и выводит её автора"""
    search_title = input("Введите название книги: ").strip().lower()

    try:
        with open("books.txt", "r", encoding="utf-8") as file:
            for line in file:
                try:
                    title, author = line.strip().split(" -- ")  # Разделяем строку
                    if title.lower() == search_title:
                        print(f"Автор: {author}")
                        return
                except ValueError:
                    print("⚠ Ошибка в формате данных в файле!")
                    return
    except FileNotFoundError:
        print("⚠ Файл books.txt не найден!")
        return

    print("Книга не найдена")

find_book()
    