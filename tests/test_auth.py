from models.user import User
from app import db

def test_register_user(client):
    response = client.post('/auth/register', data={
        'username': 'newuser',
        'password': 'password123',
        'password_confirm': 'password123'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Registro completo' in response.data
    
    with client.application.app_context():
        assert User.query.filter_by(username='newuser').first() is not None

def test_login_user(client, test_user):
    response = client.post('/auth/login', data={
        'username': 'testuser',
        'password': 'password123'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Bem-vindo, testuser' in response.data

def test_login_failure(client, test_user):
    response = client.post('/auth/login', data={
        'username': 'testuser',
        'password': 'wrongpassword'
    }, follow_redirects=True)
    
    assert b'incorretos' in response.data

def test_logout(client, test_user):
    client.post('/auth/login', data={'username': 'testuser', 'password': 'password123'})
    response = client.get('/auth/logout', follow_redirects=True)
    assert b'Voc\xc3\xa6 saiu da sua conta' in response.data or b'saiu' in response.data
