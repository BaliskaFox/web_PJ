import random
#Случайное целое число
randon_number = random.randint(1,50)
print(f"Ваш номер -- {randon_number}")
#Случайное значение списка
base_list = ["камень", "ножницы", "бумага"]
random_element_list = random.choice(base_list)
print(f"Элемент -- {random_element_list}")