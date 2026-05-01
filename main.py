from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime, timedelta


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256" 
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI(title="API")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

users_db = {}

class UserRegister(BaseModel):
    username: str
    password: str
    role: str = "user"

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@app.get("/")
async def health_check():
    return {"status": "online", "message": "API is functional"}

@app.post("/register")
async def register(user: UserRegister):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashed_password = pwd_context.hash(user.password)
    users_db[user.username] = {"password": hashed_password, "role": user.role}
    return {"message": "User created successfully"}

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or not pwd_context.verify(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid enteries")
    
    access_token = create_access_token(data={"sub": form_data.username, "role": user["role"]})
    return {"access_token": access_token, "token_type": "bearer"}

class TaskCreate(BaseModel):
    title: str
    description: str

tasks_db = []

@app.post("/tasks")
async def create_task(task: TaskCreate, token: str = Depends(oauth2_scheme)):
    """
    Creates a task linked to the authenticated user.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        
        new_task = {
            "id": len(tasks_db) + 1,
            "owner": username,
            "title": task.title,
            "description": task.description,
            "created_at": datetime.utcnow()
        }
        tasks_db.append(new_task)
        return new_task
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

@app.get("/tasks")
async def list_tasks(token: str = Depends(oauth2_scheme)):
    """
    Admin: Sees all tasks.
    User: Sees only their own tasks.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        role = payload.get("role")

        if role == "admin":
            return tasks_db
        
        return [t for t in tasks_db if t["owner"] == username]
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate passsword")
        
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
