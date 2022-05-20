from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta

employees = Table("Employees", meta, 
    Column("emp_id", Integer, primary_key=True), 
    Column("emp_name", String(255)))

meta.create_all(engine)