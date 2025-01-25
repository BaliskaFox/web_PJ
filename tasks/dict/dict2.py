def color_info():
    count = 3
    color_info_dict = {}
    while count >0:
        name = input("Введите имя: ")
        color = input("Введите его любимый цвет: ")
        color_info_dict[name] = {color}
        count -= 1
        print(count)
    print(color_info_dict)


color_info()        

