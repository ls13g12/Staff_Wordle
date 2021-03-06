from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager
from config import Config
from whitenoise import WhiteNoise

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = "auth.login"
login.login_message = "Please log in to access this page."


def create_app(config_class=Config):
    app = Flask(__name__, static_url_path="")
    app.config.from_object(config_class)
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from app.main import bp as main_bp

    app.register_blueprint(main_bp)

    from app.api import bp as api_bp

    app.register_blueprint(api_bp)

    from app.auth import bp as auth_bp

    app.register_blueprint(auth_bp)
    app.wsgi_app = WhiteNoise(app.wsgi_app, root="")

    return app


from app import models
