from flask import Blueprint, render_template, request, redirect, url_for
from models import get_db_connection

students_bp = Blueprint('students', __name__, url_prefix='/students')

@students_bp.route('/')
def list_students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('students.html', students=students)

@students_bp.route('/add', methods=['GET', 'POST'])
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
        return redirect(url_for('students.list_students'))
    
    return render_template('add_student.html')

@students_bp.route('/delete_student/<int:student_id>')
def delete_student(student_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('students.list_students'))

@students_bp.route('/edit_student/<int:student_id>', methods=['GET', 'POST'])
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

        return redirect(url_for('students.list_students'))
    
    conn.close()
    return render_template('edit_student.html', student=student)
    

