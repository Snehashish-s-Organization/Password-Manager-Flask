import json 

with open("data/userdata.json", "r") as file:
    userdata = json.load(file)

def checklogin(username, password):
    mylist = []
    for i in userdata:
        if username == i["username"]:
            if password == i["password"]:
                return True
        
    return False

