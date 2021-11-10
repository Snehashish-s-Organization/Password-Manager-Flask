# CLI CLIENT FOR THE API
from prettytable import PrettyTable
import requests

# from v2.DB import add_password

url = "http://127.0.0.1:5555/api/v1/"
page = requests.get(url)
data = page.json()

table = PrettyTable()
table.field_names = ["Site Name", "Site Email","Site Username", "Site Password"]

def getUserSpeceficData():
    name = input("enter the username of user whose data you wanna acces: ")

    names = []
    for i in data:
        names.append(i["username"])

    if name in names:
        page2 = requests.get(url, params = {"username":name})

    new_data = page2.json()

    for i in new_data["data"]:
        lis = [i["site_name"], i["site_email"], i["site_username"], i["site_password"]]
        table.add_row(lis)

    print(table)
    

def AddPassword():
    name = input("enter the username to whose databse you want to write the data: ")
    site_name = input("Enter the site's name: ")
    site_email = input("Enter the email address you used to signup for this site: ")
    site_password = input("Enter the password you used to signup for this site: ")
    site_username = input("Enter the username you used to signup for this site: ")


    page3 = requests.post(url+"?newpw=true&username="+name+"&sitename="+site_name+"&sitepassword="+site_password+"&siteemail="+site_email+"&siteusername="+site_username) 
    print(page3)
    names = []
    for i in data:
        names.append(i["username"])

    if name in names:
        page2 = requests.get(url, params = {"username":name})

    new_data = page2.json()

    for i in new_data["data"]:
        lis = [i["site_name"], i["site_email"], i["site_username"], i["site_password"]]
        table.add_row(lis)

    print(new_data["data"])

def main():
    while True:
        inp = input("passwordmanager:~$ ")
        
        if inp == "post":
            AddPassword()
        elif inp == "get":
            getUserSpeceficData()

main()
