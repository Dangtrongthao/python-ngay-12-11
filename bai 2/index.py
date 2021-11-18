from logging import exception
from os import name
from typing import Optional
from fastapi import FastAPI
from pydantic.main import BaseModel
from utils_db import *

app =FastAPI()
@app.get("/")
def get_data():
    return "thao"

class POSTdata(BaseModel):
    name:str    
    age:int
    name2:Optional[str]

@app.post("/thao")
def post_data(post:POSTdata):
    name=post.name
    age=post.age
    return int(name) + age

class Hocsinh(BaseModel):
    name:str
    age:int
    
@app.post("/themhocsinh")
def themhocsinh(item:Hocsinh):
    name=item.name
    age=item.age
    # return {'name':name,'age':age}
    try:
        instance=student(name=name,age=age)
        kq=instance.save()
        if kq:
            return {"res":True}
        else:
            return {"res":False}
    except Exception as e:
        return  {"res":False,'err':'%s'%e}