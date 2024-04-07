from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import random
from typing import List

from app.schemas.post import ShowPost, PostCreate
from app.db.session import get_db
from app.db.repository.post import create_post, get_post

router = APIRouter()


@router.post("/create-post", response_model=ShowPost)
def create_new_post(post: PostCreate, db: Session = Depends(get_db)):
    author_id = random.randint(0,1000)
    post = create_post(db, post, author_id)
    return post


@router.get("/all", response_model=List[ShowPost])
def retrieve_all_posts(db: Session = Depends(get_db)):
    posts = get_post(db)
    return posts