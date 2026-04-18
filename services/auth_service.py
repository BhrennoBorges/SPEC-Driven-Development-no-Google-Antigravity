from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from models.user import User

def register_user(username: str, password: str) -> User:
    """
    Registra um novo usuário no sistema. Realiza o hash da senha de forma segura.
    """
    hashed_password = generate_password_hash(password)
    user = User(username=username, password_hash=hashed_password)
    db.session.add(user)
    db.session.commit()
    return user

def authenticate_user(username: str, password: str) -> User | None:
    """
    Verifica se as credenciais do usuário são válidas. Notifica falhas retornando None.
    """
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        return user
    return None
