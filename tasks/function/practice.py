user_input = input("Введите строку: ")

def chekUserInput(user_input):
    if not user_input:
        print("Пустая строка")
    elif user_input.isdigit():
        total = sum(int(char) for char in user_input)
        print(f"Сумма цифр: {total}")
    else:
        print("Это текст")

chekUserInput(user_input)