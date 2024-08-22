from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

posts = []

@app.get("/")
def root():
    return {"message": "Hello World !!!"}

@app.get('/posts')  
def get_posts():
    return {'data': posts}
  
@app.get('/post/latest')  
def get_latest_post():
  if len(posts) > 0:
    post = posts[len(posts) - 1]
    return {'data': post}
  else: 
    return  {'data': None}


@app.get('/post/{id}')  
def get_post(id: str):
    post = next((item for item in posts if item['id'] == id), None)
    if post:
        return {'data': post}
    else:
        return {'error': 'Post not found'}, 404

@app.post('/post')
def create_post(new_post: Post):
    post_dict = new_post.model_dump() 
    post_dict['id'] = str(uuid.uuid4()) 
    posts.append(post_dict) 
    return {'data': post_dict}
