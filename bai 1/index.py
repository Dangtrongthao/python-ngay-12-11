from fastapi import FastAPI, params
from pydantic import BaseModel
app = FastAPI()

#class Name(BaseModel):
#    name:str


#@app.get("/thao")
#def index():
#    return "hello thao dep giau co trai"
#
#@app.get("/do-tinh-yeu/thao")
#def index():
#    return "hello thao dep giau co trai"
@app.get("/do-tinh-yeu/{name1}/{name2}")

    
def hell(name1,name2,):
    comparer=set(name1) &set(name2)
    le=len(comparer)
    kq=''
    if le>=3:
        kq='rat hop'
    elif le >0 & le<3:
        kq='hop nhau '
    elif le ==0:    
        kq='khong hop'
    else:
        kq=''   
    return f"cac ban {kq}"
   

