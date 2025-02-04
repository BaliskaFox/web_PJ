# Напиши класс "Книга", который содержит:

# название, автора, год издания (атрибуты)
# метод show_info(), который выводит информацию о книге
# создайте два объекта этого класса и вызовите show_info()

# Добавь в класс Book метод is_old(), который будет возвращать True, если книге больше 50 лет, иначе False.
from datetime import datetime

class Book:
    
    
    def __init__(self,title,author,year):

        self.title = title
        self.author = author
        self.year = year

    def show_info(self):
        print(f"\nИнформация о книге :\nНазвание книги -- {self.title}\nАвтор книги -- {self.author}\nГод издания -- {self.year} год.")
    
    def is_old(self):
        return (datetime.now().year - self.year) >= 50
    
    def get_age(self):
        return datetime.now().year - self.year
    
    def short_info(self):
        return f'{self.title}({self.author},{self.year})'
    
    def compare_age(self, other_book):
        # Вычисляем разницу в возрасте
        age_difference = abs(self.get_age() - other_book.get_age())
        # Определяем, какая книга старше
        if self.get_age() > other_book.get_age():
            return f'"{self.title}" старше, чем "{other_book.title}" на {age_difference} лет'
        elif self.get_age() < other_book.get_age():
            return f'"{other_book.title}" старше, чем "{self.title}" на {age_difference} лет'
        else:
            return f'"{self.title}" и "{other_book.title}" ровесники'
        

my_book1 = Book('Мастер и Маргарита', 'Булгаков', 1900)
my_book1.show_info()

if my_book1.is_old():
    print(f'Книга старше 50 лет')


my_book2 = Book('Мерседес', 'Стивен Кинг', 2007)
my_book2.show_info()
print(f"Книге {my_book2.get_age()} лет")

my_book3 = Book('Мертвые души','Гоголь', 1842)
print(my_book3.short_info())
print(my_book1.compare_age(my_book2))


