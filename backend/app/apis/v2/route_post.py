from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.post import ShowPost, PostCreate
from app.db.session import get_db
from app.db.models.user import User
from app.db.repository.post import create_post, get_post
from app.apis.v2.route_login import get_current_user_from_token

router = APIRouter()


@router.post("/create-post", response_model=ShowPost)
def create_new_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token)
):
    user_id = current_user.id
    post = create_post(db, post, user_id)
    return post


@router.get("/all", response_model=List[ShowPost])
def retrieve_all_posts(db: Session = Depends(get_db)):
    posts = get_post(db)
    return posts