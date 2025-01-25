numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Ожидаемый результат: 5 (чётные числа: [2, 4, 6, 8, 10])
numbers_sort = list(filter(lambda x: (x % 2==0), numbers))
print(numbers_sort)