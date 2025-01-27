from flask import Flask, make_response, render_template, request, jsonify, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)

app.secret_key = 'your_secret_key_here'  # Используется для подписи данных в сессии

# Данные для аутентификации
users = {"admin": "password123"}

# Данные о студентах
students = [
    {"name": "Алиса", "age": 20, "scores": [85, 90, 78]},
    {"name": "Боб", "age": 22, "scores": [88, 92, 81]},
    {"name": "Чарли", "age": 19, "scores": [72, 85, 89]},
]

def get_db_connection():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row  # Позволяет работать с результатами как с dict
    return conn

@app.route('/')
def home():
    return render_template('home.html', title="Главная")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        return render_template('contact.html', name=name, message=message)
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Добавление маршрутов для аутентификации
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in users and users[username] == password:
            session['logged_in'] = True
            flash('Вы успешно вошли!', 'success')
            return redirect(url_for('protected'))
        else:
            flash('Неверное имя пользователя или пароль', 'danger')
    
    return render_template('login.html')

@app.route('/protected')
def protected():
    if not session.get('logged_in'):
        flash('Сначала войдите в систему.', 'warning')
        return redirect(url_for('login'))
    
    return render_template('protected.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Вы вышли из системы.', 'info')
    return redirect(url_for('home'))

@app.route('/students')
def list_students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('students.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        scores = request.form['scores']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO students (name, age, scores) VALUES (?, ?, ?)',
                     (name, age, scores))
        conn.commit()
        conn.close()
        return redirect(url_for('list_students'))
    
    return render_template('add_student.html')

@app.route('/delete_student/<int:student_id>')
def delete_student(student_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('list_students'))

@app.route('/edit_student/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?', (student_id,)).fetchone()
    
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        scores = request.form['scores']
        
        conn.execute('UPDATE students SET name = ?, age = ?, scores = ? WHERE id = ?',
                     (name, age, scores, student_id))
        conn.commit()
        conn.close()
        return redirect(url_for('list_students'))
    
    conn.close()
    return render_template('edit_student.html', student=student)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    response = make_response(render_template('500.html'), 500)
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    return response

if __name__ == "__main__":
    app.run(debug=True)
