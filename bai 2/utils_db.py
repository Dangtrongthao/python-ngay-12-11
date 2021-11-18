from peewee import *
import requests
import json
import datetime

host='198.13.58.149'
db_name = 'tool_facebook'
db_user='dangtrongthao'
db_pass='29061992'

db = MySQLDatabase(db_name,host=host, user=db_user, passwd=db_pass)

class student(Model):
    name = CharField()
    age= IntegerField()
    lop=CharField()
    class Meta:
        database=db

# db.close()    
if __name__=="__main__":
    # pass
    L = student.select()
    print(len(L))

    # L[0].name
    # L[0].age