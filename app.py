import os
from flask import Flask
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

login_manager.login_view = 'auth.login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'
login_manager.login_message_category = 'warning'

@login_manager.user_loader
def load_user(user_id):
    from models.user import User
    return User.query.get(int(user_id))

def create_app(config_class=Config):
    """Factory function for creating the Flask application instance."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Register blueprints
    from auth.routes import auth_bp
    from tasks.routes import tasks_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    # Add template globals or context processors if needed
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
