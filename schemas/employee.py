from unicodedata import name
from typing import Optional
from pydantic import BaseModel

class Employee(BaseModel):
    emp_id: Optional[str]
    emp_name: str
