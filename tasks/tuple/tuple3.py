students_scores = [("Алиса", 85), ("Боб", 90), ("Чарли", 78), ("Дина", 92)]
score_student=[]
student_count = []
for stundent, score in students_scores:
    print(f"Имя студента: {stundent}; Балл: {score}")
    score_student.append(score)
    student_count.append(stundent)

print(f"Средний балл всех студентов: {sum(score_student) / len(student_count)}")

top_student = max(students_scores, key=lambda x: x[1])
print(f"Студент с наивысшим баллом: {top_student}")  