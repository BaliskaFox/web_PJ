number = input("Введите число: ")

if int(number) % 3 == 0 and int(number) % 5 == 0:
    print("Число делиться на 3 и 5")
elif int(number) % 3 == 0:
    print("Число делиться на 3")
elif int(number) % 5 == 0:
    print("Число делиться на 5")
else:
    print("Число не делиться на 3 и 5")