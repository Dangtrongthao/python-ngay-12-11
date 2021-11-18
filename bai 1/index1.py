# pip install fastapi
# pip install pydantic

# uvicorn: asynchronous server gateway interface
# pip install uvicorn
# uvicorn hello_word:app --reload --port 3005

# docs
# localhost:3005/docs


# from typing import Optional
from fastapi import FastAPI, params
from pydantic import BaseModel
# from typing import Optional

# class UserDataPost(BaseModel):
#     name:str
#     age:Optional[int]
#     job:Optional[str] = "IT dev"
    
# instance cua class
app = FastAPI()

@app.get("/index")
def index():
    return "Đây là trang chủ"

@app.get("/about")
def about():
    return "Đây là giới thiệu"

@app.get("/store")
def store():
    return "Chungs tôi đã hết hàng"

# async def index():
#     return "hello from index"


# @app.post("/user")
# def submit(userDataPost:UserDataPost):
#     # svalidation UserDataPost
#     return {'userDataPost':userDataPost}

# @app.get("/hello/nghia")
# def hello1():
#     return "Xin chào nghia"

# @app.get("/hello/thao")
# def hello2():
#     return "Xin chào thao"

# @app.get("/hello/tung")
# def hello3():
#     return "Xin chào tung"

# truyền params vào url (path parameters)
@app.get("/hello/{name}")
def hello(name):
    return f"Xin chào {name} zzz"

@app.get("/post/{id_post}")
def get_post(id_post):
    return f"Bạn đã tra cứu bài viết có id là {id_post}"

@app.get("/{so_1}/{so_2}")
def sum(so_1:int,so_2:int):
    return f"Tổng 2 số {so_1} và {so_2} là {so_1+so_2}"

# BTVN: Cài các hết ác thứ

#  người dùng xem bói:
# http://127.0.0.1:3005/do-tinh-yeu/thao/linh

# nếu 2 người này có số ký tự trong chữ, trùng nhau hơn 3:
# rất hợp
#  1< và <3: khá bt

#  trùng trùng nhau ký tự nào => ko hợp

#  thao
#  linh => h => ko hợp