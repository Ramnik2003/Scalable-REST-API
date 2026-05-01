from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from .database import engine, Base, get_db
from .models import DBUser, DBTask
from .schemas import UserRegister, TaskCreate, TaskResponse
from .auth import hash_password, verify_password, create_access_token, oauth2_scheme, SECRET_KEY, ALGORITHM

# Initialize DB
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def health_check():
    return {"status": "online"}

@app.post("/register")
async def register(user: UserRegister, db: Session = Depends(get_db)):
    if db.query(DBUser).filter(DBUser.username == user.username).first():
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = DBUser(username=user.username, hashed_password=hash_password(user.password), role=user.role)
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(DBUser).filter(DBUser.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid entries")
    token = create_access_token(data={"sub": user.username, "role": user.role})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/tasks", response_model=TaskResponse)
async def create_task(task: TaskCreate, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        new_task = DBTask(owner=payload.get("sub"), title=task.title, description=task.description)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/tasks")
async def list_tasks(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("role") == "admin":
            return db.query(DBTask).all()
        return db.query(DBTask).filter(DBTask.owner == payload.get("sub")).all()
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
    