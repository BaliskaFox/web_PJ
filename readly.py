with open("data.txt", "w") as file:
    file.write('Это новый текст')
with open("data.txt", "r") as file:
    print(file.read())