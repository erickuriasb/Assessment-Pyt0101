from fastapi import APIRouter
from sqlalchemy import insert
from config.db import conn
from models.employee import employees
from schemas.employee import Employee



employee = APIRouter()

@employee.get("/employees/", response_model=list[Employee], tags=["endpoints"])
def get_employee():
    return conn.execute(employees.select()).fetchall()

@employee.post("/employee/", tags=["endpoints"])
def create_employee(employee: Employee):
    new_employee = {
        "emp_name": employee.emp_name,
    }
    result = conn.execute(employees.insert().values(new_employee))
    return result