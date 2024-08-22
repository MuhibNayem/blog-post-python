from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.post import Post, PostCreate, PostUpdate
from app.crud.post import get_post, create_post, update_post, delete_post
from app.api.deps import get_db, get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=List[Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = db.query(Post).offset(skip).limit(limit).all()
    return posts

@router.get("/{id}", response_model=Post)
def read_post(id: str, db: Session = Depends(get_db)):
    post = get_post(db, post_id=id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.post("/", response_model=Post)
def create_post_for_user(post_in: PostCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_post(db=db, post=post_in, owner_id=current_user.id)

@router.put("/{id}", response_model=Post)
def update_existing_post(id: str, post_in: PostUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    post = get_post(db, post_id=id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return update_post(db=db, db_post=post, post=post_in)

@router.delete("/{id}", response_model=Post)
def delete_post_for_user(id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    post = get_post(db, post_id=id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    delete_post(db=db, db_post=post)
    return post
