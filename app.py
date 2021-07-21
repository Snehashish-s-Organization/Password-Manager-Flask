
# Author: snehashish laskar,
# Email: snehashish.laskar@gmail.com
# Github Username: snehashish090

# importing all the necessary modules
from flask import Flask, request, render_template, redirect, url_for, session
from signup import *
from log import *

# Initializing the flask app
app = Flask(__name__)
# setting a secret_key required for sessions
app.secret_key = "snehashishkasecretkey"

# Making a home page and rendering the template "home.html"
@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("home.html")

# Making a page to return the user details or "cookies"
@app.route('/lol', methods=["GET", "POST"])
def signupPage():
    # returning the cookies
    return session

# Creating the page for user authentication and signup
@app.route('/auth', methods=["GET", "POST"])
def auth():
    # trying to get the status cookie 
    try:
        # if there is a status key then it will check if 
        # the user is logged in or not
        if session["status"] != "logged": 
            # If not logged in then:
            # Checking if a form has been submitted
            if request.method == "POST":
                if "LogButton" in request.form:

                    # Getting the credentials entered in the input fields
                    myusername = request.form["LogName"]
                    mypassword = request.form["LogPass"]
                    
                    # Using the function checklogin from the file "log.py"
                    if checklogin(myusername, mypassword):
                        # If the function returns true then the user is logged in
                        # The status is set to logged
                        # And the username of the user logged in is set as username
                        session["username"] = myusername
                        session["status"] = "logged"
                        # returning the user to home 
                        return redirect("/lol")
                    else:
                        # if the credentials are wrong then displaying the message to the user
                        return render_template("login.html", logmsg = "Please check your username and password")

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

