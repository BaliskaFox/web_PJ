import math
#Вычесление длины окружности
radius_boll = 5
leng_boll = 2 * math.pi * radius_boll
print(f"Длина окружности -- {round(leng_boll, 2)}")
#Гипотенуза треугольника
triangle_leg1 = 3
triangle_leg2 = 4
hypotenuse_triangle = math.pow(triangle_leg1, 2) + math.pow(triangle_leg2,2)
print(f"Гипотенуза треугольника равна -- {math.sqrt(hypotenuse_triangle)}")