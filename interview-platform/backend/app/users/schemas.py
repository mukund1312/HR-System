from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: str
    email: str
    roles: List[str]
    permissions: List[str]
