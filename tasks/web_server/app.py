from flask import Flask
from models import get_db_connection
from routes.students_routes import students_bp
from routes.general_routes import general_bp
from routes.authentication import authentication_br

app = Flask(__name__)

app.secret_key = 'your_secret_key_here'  # Используется для подписи данных в сессии

# Регистрация блюпринтов (Blueprints)
app.register_blueprint(students_bp)
app.register_blueprint(general_bp)
app.register_blueprint(authentication_br)

if __name__ == "__main__":
    app.run(debug=True,use_reloader=True)
