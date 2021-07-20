import json 

with open("data/userdata.json", "r") as file:
    userdata = json.load(file)

def checklogin(username, password):
    for i in userdata:
        if i["username"] == username and i["password"] == password:
            return True
        else:
            return False
