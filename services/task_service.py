from typing import List, Optional
from app import db
from models.task import Task, TaskStatus

def get_tasks_for_user(user_id: int, status_filter: Optional[str] = None) -> List[Task]:
    """
    Retorna a lista de tarefas, garantindo que pertencem apenas ao user_id informado.
    Pode aplicar um filtro opcional por status.
    """
    query = Task.query.filter_by(user_id=user_id)
    if status_filter:
        try:
            status_enum = TaskStatus[status_filter.upper()]
            query = query.filter_by(status=status_enum)
        except KeyError:
            # Ignora status inválidos
            pass
            
    return query.order_by(Task.created_at.desc()).all()

def get_task_by_id(task_id: int, user_id: int) -> Optional[Task]:
    """
    Busca uma tarefa específica, mas assegura que pertence ao user_id.
    Retorna None se não encontrar ou não pertencer ao usuário.
    """
    return Task.query.filter_by(id=task_id, user_id=user_id).first()

def create_task(title: str, description: str, status_name: str, user_id: int) -> Task:
    """
    Cria uma nova tarefa e persiste no banco de dados.
    """
    status_enum = TaskStatus[status_name.upper()]
    task = Task(
        title=title,
        description=description,
        status=status_enum,
        user_id=user_id
    )
    db.session.add(task)
    db.session.commit()
    return task

def update_task(task_id: int, user_id: int, title: str, description: str, status_name: str) -> Optional[Task]:
    """
    Atualiza uma tarefa existente, desde que pertença ao usuário logado.
    """
    task = get_task_by_id(task_id, user_id)
    if not task:
        return None
        
    task.title = title
    task.description = description
    task.status = TaskStatus[status_name.upper()]
    
    db.session.commit()
    return task

def delete_task(task_id: int, user_id: int) -> bool:
    """
    Deleta uma tarefa, assegurando que ela pertence ao usuário solicitante.
    Retorna True se deletou, False caso não encontre ou não tenha permissão.
    """
    task = get_task_by_id(task_id, user_id)
    if not task:
        return False
        
    db.session.delete(task)
    db.session.commit()
    return True
