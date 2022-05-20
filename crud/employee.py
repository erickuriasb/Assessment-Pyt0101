from config.db import conn
from models.employee import employees
from schemas.employee import Employee

class EmployeeCRUD:
    def get_employees():
        return conn.execute(employees.select()).fetchall()


    def create_employee(employee: Employee):
        new_employee = {
            "emp_name": employee['emp_name'],
        }
        
        response = conn.execute(employees.insert().values(new_employee))
        return response

    def delete_employee(emp_id: str):
        response = conn.execute(employees.delete().where(employees.c.emp_id == emp_id))