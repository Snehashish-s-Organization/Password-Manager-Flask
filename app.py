"""
author: snehashish laskar,
email: snehashish.laskar@gmail.com
github: snehashish090

"""

# importing all the necessary modules

from flask import Flask, request, render_template, redirect, url_for, session
from signup import *
from log import *

app = Flask(__name__)
app.secret_key = "snehashishkasecretkey"

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route('/lol', methods=["GET", "POST"])
def signupPage():
    return session

@app.route('/auth', methods=["GET", "POST"])
def auth():
    try:
        if session["status"] != "logged": 
            if request.method == "POST":
                if "LogButton" in request.form:

                    username = request.form["LogName"]
                    password = request.form["LogPass"]

                    if checklogin(username, password):
                        session["username"] = username
                        session["status"] = "logged"
                        return redirect("/lol")
                    else:
                        return redirect("/auth")

                elif "upSubmit" in request.form:
                    
                    username = request.form["UpName"]
                    password = request.form["UpPass"]
                    email = request.form["UpMail"]

                    if signCheck(username,email):
                        signup(username, password, email)
                        session["username"] = username
                        session["status"] = "logged"
                        return redirect("/lol")


                    elif username =="" or password=="" or email=="" : 
                        return render_template("login.html", logmsg="Please dont leave any fields blank!")
                
                    else:
                        return render_template("login.html", logmsg="Sorry! An user with this username or email already exists")
                else:
                    return render_template("login.html")
            
            return render_template("login.html")
        else:
            return redirect("/lol")
            
    except:
        session["status"] = "out"
        return redirect("/auth")

@app.route("/logout")
def logout():
    session["status"] = "out"
    session["username"]  = "blah"
    return redirect("/auth")

app.run(debug=True, host="0.0.0.0")