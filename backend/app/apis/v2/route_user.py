from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import ShowUser, UserCreate
from app.db.session import get_db
from app.db.repository.user import create_user


router = APIRouter()


@router.post("/create-user", response_model=ShowUser)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user)
    return user
