celsius = [0, 20, 37, 100]
# Ожидаемый результат: [32.0, 68.0, 98.6, 212.0]
faringate = list(map(lambda x: (x * 1.8) + 32, celsius))
print(faringate)