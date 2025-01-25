def enumeration():
    print("Выводим число от 1 до 20: ")
    for i in range(20):
        print(i + 1)

enumeration()

user_input = input("Введите число: ")

while int(user_input) > 0:
    print("ты меня не остановишь")
    user_input = input("Попробуй снова, введи число: ")