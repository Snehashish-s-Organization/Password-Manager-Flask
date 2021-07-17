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
            "email": self.email
        }

def signup(username="default", password="default", email="default", mydata = userdata):
    with open("data/userdata.json", "w") as file:
        userdata.append(User(username=username,email=email, password=password).returnData())
        json.dump(userdata, file, indent=4)
        #User(username=username,email=email, password=password).returnData()
        
def signCheck(username, email):
    for i in userdata:
        if i["username"] == username or i["email"] == email:
            return False
        else:
            return True
print(hashlib.sha256("snehashis2h".encode()).hexdigest())