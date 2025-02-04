
students = {
    'Алена': ["Математика"],
    'Иван': ['Алгебра'],
    'Зарина': ["Биология"]
}

def add_or_update_student(student_name,subject):
        
    if student_name in students:
        students[student_name].append(subject)  # Добавляем предмет в список
    else:
        students[student_name] = [subject]  # Создаём новый список предметов

def remove_student(student_name):

    if student_name in students:
         del students[student_name]
    else:
        print(f"❌ Ошибка: Студент {student_name} не найден!")

def show_all_students():
    
    for student, subjects in students.items():
        subject_list = ", ".join(subjects)  # Объединяем предметы через запятую
        print(f'📚 {student} изучает: {subject_list}')

# ✅ Тестирование
add_or_update_student('Алена', "Физика")
add_or_update_student('Ольга', "Физика")
remove_student('Зарина')
add_or_update_student('Лиза', 'Биология')

# ✅ Вывод всех студентов
show_all_students()

