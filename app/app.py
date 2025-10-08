# from flask import Flask, render_template, redirect, url_for, session
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager, login_required
# from config import Config
# from models import db
# from auth import auth_bp
# from weather import weather_bp

# app = Flask(__name__)
# app.config.from_object(Config)

# db.init_app(app)
# bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'auth.login'

# @login_manager.user_loader
# def load_user(user_id):
#     from models import User
#     return User.query.get(int(user_id))

# app.register_blueprint(auth_bp)
# app.register_blueprint(weather_bp)

# @app.route('/')
# @login_required
# def dashboard():
#     return render_template('dashboard.html')

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_required
from config import Config
from models import db
from auth import auth_bp
from weather import weather_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    from models import User
    return User.query.get(int(user_id))

app.register_blueprint(auth_bp)
app.register_blueprint(weather_bp)

@app.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
