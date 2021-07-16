from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    return "Hallo!"

@app.route('/signup', methods=["GET", "POST"])
def signupPage():
    return "Signup bruh!"

@app.route('/login', methods=["GET", "POST"])
def loginPage():
    if request.method == "POST":
        if "LogButton" in request.form:
            if request.form["LogName"] == "snehashish" and request.form["LogPass"] == "snehashish":
                return redirect("https://snehashish090.github.io")
            else:
                return redirect("/login")
        
        elif "upSubmit" in request.form:
            return redirect("/signup")

        else:
            return render_template("login.html")
            
    return render_template("login.html")

app.run(debug=True, host="127.0.0.1")