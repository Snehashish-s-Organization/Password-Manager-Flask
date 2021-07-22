import json 
import hashlib 

with open("data/userdata.json", 'r') as file:
    userdata = json.load(file)

class User(object):

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        
    def returnData(self):

        return {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "data":[]
        }

def signup(username="default", password="default", email="default", mydata = userdata):
    with open("data/userdata.json", "w") as file:
        userdata.append(User(username=username,email=email, password=password).returnData())
        json.dump(userdata, file, indent=4)
        #User(username=username,email=email, password=password).returnData()
        
def signCheck(username, email):
    names = []
    emails = []
    for i in userdata:
        names.append(i["username"])
        emails.append(i["email"])

    if username in names or username in emails:
        return False
    else:
        return True