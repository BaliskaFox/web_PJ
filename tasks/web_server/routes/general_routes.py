from flask import Blueprint, render_template, request

general_bp = Blueprint('general', __name__)

@general_bp.route('/')
def home():
    return render_template('home.html', title="Главная")

@general_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        return render_template('contact.html', name=name, message=message)
    return render_template('contact.html')

@general_bp.route('/about')
def about():
    return render_template('about.html')