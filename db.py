from flask_mongoengine import MongoEngine,json

mydb=MongoEngine()

url="mongodb+srv://razak:mohamed@cluster0.ptmlylq.mongodb.net/vignesh?retryWrites=true&w=majority"

class Laptop(mydb.Document):
    model=mydb.StringField()
    serial=mydb.StringField()
    ram=mydb.IntField()
    ssd=mydb.IntField()
    stock=mydb.IntField()
    price=mydb.IntField()
    type=mydb.StringField()
