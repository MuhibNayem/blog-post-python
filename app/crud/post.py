from sqlalchemy.orm import Session
from uuid import uuid4
from app.models.post import Post
from app.schemas.post import PostCreate, PostUpdate

def get_post(db: Session, post_id: str):
    return db.query(Post).filter(Post.id == post_id).first()

def create_post(db: Session, post: PostCreate, owner_id: str):
    db_post = Post(id=str(uuid4()), owner_id=owner_id, **post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_post(db: Session, db_post: Post, post: PostUpdate):
    for key, value in post.dict(exclude_unset=True).items():
        setattr(db_post, key, value)
    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db: Session, db_post: Post):
    db.delete(db_post)
    db.commit()
