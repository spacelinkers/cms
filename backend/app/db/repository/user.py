from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.db.models.user import User
from app.core.hashUtil import HashUtil

def create_user(db: Session, user: UserCreate):
    user = User(
            username = user.username,
            email = user.email,
            hashed_password = HashUtil.get_password_hash(user.password),
            is_active = True,
            is_superuser = False
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
