from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate
app = FastAPI()

text_posts = {
    1: {"title": "New Post", "content": "cool test post"},
    2: {"title": "Morning Thoughts", "content": "Woke up feeling motivated today"},
    3: {"title": "FastAPI Progress", "content": "Finished setting up routes and schemas"},
    4: {"title": "Gym Update", "content": "Hit a new PR on bench press"},
    5: {"title": "Study Session", "content": "Reviewed system design basics"},
    6: {"title": "Bug Fixed", "content": "Resolved authentication issue"},
    7: {"title": "Learning Git", "content": "Understanding branches and merges"},
    8: {"title": "Weekend Plan", "content": "Building a small backend project"},
    9: {"title": "Tech Stack", "content": "Python, FastAPI, PostgreSQL"},
    10: {"title": "Daily Reflection", "content": "Consistency beats motivation"}
}

@app.get("/posts")
def get_all_posts(limit: int=None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_posts(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404,detail="post not found")
    return text_posts.get(id)

@app.post
def create_post(post: PostCreate):
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts) + 1] = new_post
    return new_post
