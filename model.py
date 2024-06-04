from pydantic import BaseModel
from datetime import datetime

class Todo(BaseModel):
    id : int
    item : str
    author: str 
    timestamp: datetime
