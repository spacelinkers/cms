from sqlalchemy.orm import Session
from app.db.models.user import User


def get_user(username:str, db:Session):
    user = db.query(User).filter(User.email == username).first()
    return user
