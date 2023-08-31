from flask import Flask,jsonify
from db import *

app=Flask(__name__)

# configuring mongodb
app.config['MONGODB_HOST']=url
mydb.init_app(app)

@app.route("/")
def checkConnection():
    #return make_response("<h1>Hell</h1>")
    return jsonify(Laptop.objects.all())

if __name__=="__main__":
    app.run(debug=True,port=9988)