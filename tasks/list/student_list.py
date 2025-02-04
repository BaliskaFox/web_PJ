class Student:
    def __init__(self):
        self.students = []
        self.show_students()
    
    def add_student(self, name):
        self.students.append(name)    

    def remove_student(self,name):
         
         if name in self.students:
            self.students.remove(name)
         else:
            print(f"❌ Ошибка: Студент {name} не найден!")

    def show_students(self):
        return f' 📋 Список студентов: {','.join(map(str, self.students))}'
    
    def filter_short_name(self):
        short_name = [student for student in self.students if len(student) <= 5]
        return short_name 
    
student = Student()
student.add_student('Вася')
student.add_student('Анна')
student.add_student('Яна')
student.add_student('Артемий')
student.add_student('Иван')
student.add_student('Богдан')
print(student.show_students())
student.remove_student('Анна')
print(student.show_students())
short_name_student = student.filter_short_name()
print(short_name_student)

