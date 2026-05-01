from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserRegister(BaseModel):
    username: str
    password: str
    role: Optional[str] = "user"

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    owner: str
    created_at: datetime

    class Config:
        from_attributes = True