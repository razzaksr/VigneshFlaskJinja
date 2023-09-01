from flask import Flask,jsonify,render_template, request, redirect
from db import *

app=Flask(__name__)

# configuring mongodb
app.config['MONGODB_HOST']=url
mydb.init_app(app)

@app.route("/pick/<mod>")
def showRead(mod):
    collected=Laptop.objects(model=mod).first()
    return render_template("read.html",data=collected)

@app.route("/new",methods=['GET','POST'])
def newOne():
    if request.method=="GET":
        return render_template("newlaptop.html")
    else:
        laptop=Laptop()
        laptop.model=request.form['model']
        laptop.serial=request.form['serial']
        laptop.ram=int(request.form['ram'])
        laptop.ssd=int(request.form['ssd'])
        laptop.price=int(request.form['price'])
        laptop.stock=int(request.form['stock'])
        laptop.type=request.form['type']
        
        laptop.save()
        
        return redirect("/list")

@app.route("/")
def showHome():
    return render_template("navigation.html")

@app.route("/list")
def listAll():
    collected=Laptop.objects.all()
    return render_template("view.html",data=collected)

@app.route("/test")
def checkConnection():
    #return make_response("<h1>Hell</h1>")
    return jsonify(Laptop.objects.all())

if __name__=="__main__":
    app.run(debug=True,port=9988)