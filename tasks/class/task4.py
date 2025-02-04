class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Привет, меня зовут {self.name}, мне {self.age} лет."

class Student(Person):

    def greet(self):
        return super().greet() + " Я студент."

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject
        self._students = [] 
    def get_subject(self):
        return self.__subject

    def set_subject(self, new_subject):
        self.__subject = new_subject
        print(f"Теперь {self.name} преподаёт {self.__subject}.")

    def greet(self):
        return super().greet() + f" Я преподаю {self.__subject}"
    
    def add_student(self,student):

        if isinstance(student, Student):  # Проверяем, что переданный объект — студент
            self._students.append(student)
        else:
            print("Можно добавлять только студентов!")
    
    def info(self):
        student_names = ", ".join([s.name for s in self._students]) if self._students else "Нет студентов"
        return f"Преподаватель {self.name} ведёт предмет {self.__subject}. Количество студентов: {len(self._students)}. Ученики: {student_names}."

class GraduateStudent(Student):
    def greet(self):
        return super().greet() + ' Я аспирант и занимаюсь исследованиями'

p = Person('Анна', 26)
s1 = Student('Ваня', 20)
s2 = Student('Илья', 18)
t = Teacher('Мария', 40, 'Математика')
g1 = GraduateStudent('Олег', 25)

#Тест
print(t.greet())
print(g1.greet())

#Добавляем студента
t.add_student(s1)
t.add_student(s2)
t.add_student(g1)
t.info()

#Изменяем предмет через метод
t.set_subject('Физика')
print(t.get_subject())

#Вывод информации
print(t.info())

