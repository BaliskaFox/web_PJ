import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Создание таблицы студентов
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    scores TEXT NOT NULL
)
''')

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("База данных создана и таблица students успешно добавлена!")
