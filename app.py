from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods=["GET", "POST"])
def loginPage():
    return render_template("login.html")

app.run(debug=True, host="127.0.0.1")