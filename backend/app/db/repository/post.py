from sqlalchemy.orm import Session

from app.schemas.post import PostCreate
from app.db.models.post import Post

def get_post(db: Session, skip: int = 0, limit: int = 100):
    posts = db.query(Post).offset(skip).limit(limit).all()
    return posts

def create_post(db: Session, post: PostCreate, user_id: int):
    db_post = Post(**post.model_dump(), user_id = user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

