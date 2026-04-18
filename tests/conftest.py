import pytest
from app import create_app, db
from models.user import User

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'test-key'
    WTF_CSRF_ENABLED = False # Simplifica testes POST

@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def test_user(app):
    from services.auth_service import register_user
    with app.app_context():
        user = register_user('testuser', 'password123')
        return user
