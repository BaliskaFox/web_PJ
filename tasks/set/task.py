math_student = {'Алина','Виталий','Ирина','Олег','Иван','Владислав'}
physics_students = {'Ирина','Олег', 'Владислав', 'Богдан'}

def common_student(set1, set2):
    return f'Студенты изучающие оба предмета: {','.join(map(str,set1 & set2))}'
def unique_students(set1, set2):
    return f'Студенты изучающий один предмет: {','.join(map(str,set1 ^ set2))}'

print(common_student(math_student,physics_students))
print(unique_students(math_student,physics_students))
