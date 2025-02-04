student_tuple = (('Иван', 23, "Алгебра"),('Алина', 20, "Биология"),('Ольга', 19, "Физика"))
def show_students(student_tuple):
    print('📋Список студентов:')
    for student in student_tuple:
        name, age, subject = student 
        print(f"{name}, {age} года, изучает {subject}")

def find_student(student_tuple, name):

    for student in student_tuple:
        if student[0] == name:
            return(f'✅ Студент {name} найден')
        
    return f"❌ Ошибка: Студент {name} не найден!"

show_students(student_tuple)
print(find_student(student_tuple,'Иван'))
print(find_student(student_tuple,'Вася'))