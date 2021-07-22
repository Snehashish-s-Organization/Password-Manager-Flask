
# Importing the necessary modules
import json

with open("data/userdata.json", "r") as file:
    data = json.load(file)

class Password:
    """
        A class Password to represent each password
        Each password has :

        => The name of the site this password is being saved for
        => The Password used in this site 
        => The email given in this site 
        => The username given in this site 
    """

    def __init__(self, sitename=None, password=None, email=None, username=None):
        self.sitename = sitename
        self.password = password
        self.email = email
        self.username = username

    def return_data(self):
        mydata = {
            "site_name":self.sitename,
            "site_password":self.password,
            "site_email":self.email,
            "site_username":self.username,
        
        }
        return mydata

def add_password(username, site_name, site_password, site_email, site_username):
    for i in data:
        if i["username"] == username:
            myPassword = Password(site_name, site_password, site_email, site_username).return_data()
            i["data"].append(myPassword)

    with open("data/userdata.json", "w") as file:
        json.dump(data, file,indent=4 )

def delete_password(username, site_name):
    for i in data:
        if i["username"] == username:
            for h in i["data"]:
                if h["site_name"] == site_name:
                    index = i["data"].index(h)
                    del i["data"][index]

    with open("data/userdata.json", "w") as file:
        json.dump(data, file,indent=4 )

add_password("romeo", "lol", "lol", "lol", "lol")