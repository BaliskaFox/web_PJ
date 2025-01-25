names = ["Alice", "Bob", "Charlie", "Dina"]
# Ожидаемый результат: ["Bob", "Dina", "Alice", "Charlie"]
names_sort = sorted(names, key=len)
print(names_sort)