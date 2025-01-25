import random
number = random.randrange(1, 10)  # значение в диапазоне 2, 4, 6, 8
print(number)

numberList =[]
for i in range(0,10):
    numberList.append(i+1)
print(f"Сгенерированный список: {','.join(map(str,numberList))}")

for i in range(len(numberList)):
    numberList[i] *=2
print(f"Новый сгенерированный список: {','.join(map(str,numberList))}")