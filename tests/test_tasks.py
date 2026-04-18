from app import db
from models.task import Task, TaskStatus

def test_create_task(client, test_user):
    client.post('/auth/login', data={'username': 'testuser', 'password': 'password123'})
    
    response = client.post('/task/new', data={
        'title': 'Test Task',
        'description': 'Description',
        'status': 'PENDING'
    }, follow_redirects=True)
    
    assert b'Tarefa criada' in response.data
    
    with client.application.app_context():
        task = Task.query.filter_by(title='Test Task').first()
        assert task is not None
        assert task.user_id == test_user.id
        assert task.status == TaskStatus.PENDING

def test_list_tasks(client, test_user):
    client.post('/auth/login', data={'username': 'testuser', 'password': 'password123'})
    client.post('/task/new', data={'title': 'My Title', 'status': 'PENDING'})
    
    response = client.get('/')
    assert b'My Title' in response.data

def test_delete_task(client, test_user):
    client.post('/auth/login', data={'username': 'testuser', 'password': 'password123'})
    client.post('/task/new', data={'title': 'ToDelete', 'status': 'PENDING'})
    
    with client.application.app_context():
        task = Task.query.filter_by(title='ToDelete').first()
        task_id = task.id
        
    response = client.post(f'/task/{task_id}/delete', follow_redirects=True)
    assert b'exclu\xc3\xadda' in response.data or b'exclu' in response.data
    
    with client.application.app_context():
        assert Task.query.get(task_id) is None
