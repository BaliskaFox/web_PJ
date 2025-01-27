from flask import Blueprint, request,session,flash,render_template,redirect,url_for

authentication_br = Blueprint('login', __name__, url_prefix="/login")

# Данные для аутентификации
users = {"admin": "password123"}

@authentication_br.route('/login', methods=['GET', 'POST'])
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

@authentication_br.route('/protected')
def protected():
    if not session.get('logged_in'):
        flash('Сначала войдите в систему.', 'warning')
        return redirect(url_for('login'))
    
    return render_template('protected.html')

@authentication_br.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Вы вышли из системы.', 'info')
    return redirect(url_for('home'))