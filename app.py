from re import template
from fastapi import FastAPI, Request
from requests import request
from watchgod import RegExpWatcher
from routes.employee import employee
from crud.employee import EmployeeCRUD
from schemas.employee import Employee
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")
'''
"The task is to develop a simple API using Python FASTAPI framework that would process input data, communicate with a database andreturn results to the client.Employee API -will support 2 operations:

1. Create an Employee record. 
    This operation will take 2 parameters: a String and an int.
    String value will populate the emp_name, integer value will populate emp_id value. Do not worry about data validation etc.
2. Return all Employee values tothe client. Any format is fine.
3. Demonstrate how you maintain the application code in a Git Repository
4. Document the usage of the API as part of the Git Readme.md

Bonus task 1: Create a Timesheet API that uses data from the Employee API. When recording a time sheet entry, make sureyou pull Employee data from the Employee API. 
Bonus task 2: Develop a simple UI that can be used directly from the web browser to drive the API -any stack will do, from plain HTML forms to JQuery to Angular/React/et"
'''
app.include_router(employee)

@app.get("/", tags=["web-app"])
def root(request: Request):
    employees = EmployeeCRUD.get_employees()
    return templates.TemplateResponse("inicio.html", {"request": request, "listaded":employees})

@app.post("/create_employee/", tags=["web-app"])
async def post_new_employee(request: Request):
    formdata = await request.form()
    employee = {
        "emp_name" : formdata['emp_name']
    }
    response = EmployeeCRUD.create_employee(employee)
    return RedirectResponse("/", 303)

@app.get("/delete_employee/{emp_id}", tags=["web-app"])
def delete_employee(request: Request, emp_id:str):
    response = EmployeeCRUD.delete_employee(emp_id)
    return RedirectResponse("/", 303)
