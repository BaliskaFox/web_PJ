#Вводные данные
students = {
    "Алиса": {"age": 20, "scores": (85, 90, 78)},
    "Боб": {"age": 22, "scores": (88, 92, 81)},
}
#Функция для добавления студента
def create_new_student():
    
    #Запрос данных о студенте
    new_student_name = input("Введите имя студента: ")
    new_student_age = int(input("Введите возраст студента: "))
    new_student_score = tuple(map(int,input("Введите баллы студента: ").split(",")))
        
    #создание словоря для записи новых студентов
    students[new_student_name] = {"age": new_student_age, "scores": new_student_score}
    
    #объединение с основным словарем
    print("Студент добавлен")
    
    #Завершение функции и вызов основной "меню"
    return menu()

def medium_score():
    total_scores = 0
    total_subjects = 0

    for data in students.values():
        total_scores += sum(data["scores"])
        total_subjects += len(data["scores"])

    avg_score = total_scores / total_subjects
    print(f"Средний балл всех студентов: {avg_score:.2f}")
    menu()

#Вывод списка
def inference_student():
    for name, info in students.items():
        age = info["age"]
        scores = ", ".join(map(str, info["scores"]))  # Преобразуем кортеж в строку
        print(f"Имя: {name} - Возраст: {age}, Баллы: {scores}")
        
    return menu()

#Поиск лучшего студента
def find_best_student():
    best_student = max(students.items(), key=lambda x: sum(x[1]["scores"]) / len(x[1]["scores"]))
    name, data = best_student
    avg_score = sum(data["scores"]) / len(data["scores"])
    print(f"Лучший студент: {name}, Средний балл: {avg_score:.2f}")
    menu()
    
#Формула ср числа сумма числе разделенная на количество чисел
def menu():
    
    #Текстовое меню
    print("1. Добавить студента")
    print("2. Вывести список студентов")
    print("3. Показать студента с лучшим баллом")
    print("4. Вывести средний балл всех студентов")
    print("5. Выход")
    
    #Запрос команды у пользователя
    cmd = input("Введите команду: ")
    
    if cmd == "1":
        create_new_student()
    elif cmd == "2":
        inference_student()
    elif cmd == "3":
        find_best_student()
    elif cmd == "4":
        medium_score()
    elif cmd == "5":
        print("Выход из программы")
    else:
        print("Введите корректную команду")
        menu()
menu()
