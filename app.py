from flask import Flask,jsonify,render_template, request, redirect,session
from db import *

app=Flask(__name__)

# configuring mongodb
app.config['MONGODB_HOST']=url
app.secret_key='zealous'
mydb.init_app(app)

@app.route("/logout")
def performOut():
    if session.get('logged'):
        session['logged']=None
    return render_template("login.html")

@app.route("/",methods=['GET','POST'])
def performLogin():
    if request.method=="GET":
        return render_template("login.html")
    else:
        user=request.form['username']
        pas=request.form['password']
        if user=="annamalai" and pas=="vignesh2":
            session['logged']=user
            return redirect("/nav")
        else:
            return render_template("login.html")

@app.route("/shortlist",methods=['GET','POST'])
def performFilter():
    if session.get('logged'):
        if request.method=="GET":
            return render_template("filter.html")
        else:
            mod=request.form['model']
            tp=request.form['type']
            ram=request.form['ram']
            cost=request.form['price']
            
            if mod!="" and tp=="Select type" and ram=="" and cost=="":
                collected=Laptop.objects(model__startswith=mod)
                return render_template("view.html",data=collected)
            elif mod=="" and tp!="Select type" and ram=="" and cost=="":
                collected=Laptop.objects(type__iexact=tp)
                return render_template("view.html",data=collected)
            elif mod=="" and tp=="Select type" and ram!="" and cost=="":
                ram=int(ram)
                collected=Laptop.objects(ram__gte=ram)
                return render_template("view.html",data=collected)
            elif mod=="" and tp=="Select type" and ram=="" and cost!="":
                cost=int(cost)
                collected=Laptop.objects(price__lte=cost)
                return render_template("view.html",data=collected)
            else:
                return render_template("filter.html")
    else:
        return render_template("login.html")

@app.route("/erase/<mod>")
def performDelete(mod):
    if session.get('logged'):
        collected=Laptop.objects(model=mod).first()
        collected.delete()
        return redirect("/list")
    else:
        return render_template("login.html")

@app.route("/update/<mod>",methods=["GET","POST"])
def performEdit(mod):
    if session.get('logged'):
        if request.method=="GET":
            collected=Laptop.objects(model=mod).first()
            return render_template("edit.html",data=collected)
        else:
            model=request.form['model']
            serial=request.form['serial']
            ram=int(request.form['ram'])
            ssd=int(request.form['ssd'])
            price=int(request.form['price'])
            stock=int(request.form['stock'])
            type=request.form['type']
            
            Laptop.objects(model=model).update_one(set__serial=serial,set__ram=ram,
                                                set__ssd=ssd,set__price=price,set__stock=stock,
                                                set__type=type)
            return redirect("/list")
    else:
        return render_template("login.html")

@app.route("/pick/<mod>")
def showRead(mod):
    if session.get('logged'):
        collected=Laptop.objects(model=mod).first()
        return render_template("read.html",data=collected)
    else:
        return render_template("login.html")

@app.route("/new",methods=['GET','POST'])
def newOne():
    if session.get('logged'):
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
    else:
        return render_template("login.html")

@app.route("/nav")
def showHome():
    if session.get('logged'):
        return render_template("navigation.html")
    else:
        return render_template("login.html")

@app.route("/list")
def listAll():
    if session.get('logged'):
        collected=Laptop.objects.all()
        return render_template("view.html",data=collected)
    else:
        return render_template("login.html")

# @app.route("/test")
# def checkConnection():
#     #return make_response("<h1>Hell</h1>")
#     return jsonify(Laptop.objects.all())

if __name__=="__main__":
    app.run(debug=True,port=9988)