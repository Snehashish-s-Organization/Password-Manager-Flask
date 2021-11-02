
from flask import Flask, request, jsonify
import json
from DB import *

with open("data/userdata.json", 'r') as file:
    data = json.load(file)

app = Flask(__name__)

@app.route('/api/v1/', methods = ['GET', 'POST', 'DEL'])
def main_page():
    if request.method == 'GET':
        if "username" in request.args:
            for i in data:
                if i["username"] == request.args["username"]:
                    return jsonify(i)
        else:
            return jsonify(data)

    elif request.method == 'POST':
        if "newuser" in  request.args:
            if "username" in request.args and "password" in request.args and "email" in request.args:
                username = request.args["username"]
                password= request.args["password"]
                email = request.args["email"]
                addUser(username, password, email)
            return jsonify(data)
        
        if "newpw" in request.args:
            if "username" in request.args and "sitename" in request.args and "sitepassword" in request.args and "siteemail" in request.args and "siteusername" in request.args:
                site_name = request.args["sitename"]
                site_password = request.args["sitepassword"]
                site_email = request.args["siteemail"]
                site_username = request.args["siteusername"]
                username = request.args["username"]
                add_password(
                    username,
                    site_name,
                    site_password,
                    site_email,
                    site_username,
                )        
            return jsonify(data)

app.run(debug=True, host="0.0.0.0", port=8235)
