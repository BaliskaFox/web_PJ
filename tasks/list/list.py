filmsList = ["Мстители", "Титаник", "Всегда говори 'ДА'","Персонаж","Тихое место"]
print(f"Первый фильм: {filmsList[0]}; Последний фильм: {filmsList[-1]}; Все фильмы: {', '.join(filmsList)}")

user_input = input("Введите 5 чисел: ")
numberList = list(user_input)


def workListUser(numberList):
    for i in range(len(numberList)):
        numberList[i] = int(numberList[i])
    print(f"Список введенных чисел: {','.join(map(str,numberList))}")
    print(f"Суммируем: {sum(numberList)}")
    print(f"Удаляем последнее число : {numberList.pop()}; Выводим обновленный список: {','.join(map(str,numberList))}")

workListUser(numberList)

