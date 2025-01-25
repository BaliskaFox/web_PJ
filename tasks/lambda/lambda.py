number_one = input("Число 1: ")
number_two = input("Число 2: ")
max_number = lambda number_one, number_two: number_one if number_one > number_two else number_two
print(max_number(number_one, number_two))
    