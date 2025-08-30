from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

students = {
    1:{"name":"Rohith","age":23,"Gender":"Male"},2:{"name":"Murari","age":24,"Gender":"Male"}
}

class Student(BaseModel):
    Name:str
    Age:int
    Gender:str

@app.get("/")

def index():
    return {"name": "Hello, World!"}

@app.get("/getstudent/{studentid}")
def getstudent(studentid:int=Path(...,description="The ID of the student you want to view" ,gt=0,le=3)):
    return students[studentid]

@app.get("/getbyname")
def getstudent(name:Optional[str]=None):
    for studentid in students:
        if students[studentid]["name"]==name:
            return students[studentid]
    return {"Data":"Not Found"}

@app.post("/createstudent/{studentid}")
def createstudent(studentid:int,student:Student):
    if studentid in students:
        return {"Error":"Student Exists"}
    students[studentid]=student
    return students[studentid]
@app.put("/updatestudent/{studentid}")
def updatestudent(studentid:int,student:Student):
    if studentid not in students:
        return {"Error":"Student Does Not Exist"}
    students[studentid]=student
    return students[studentid]