import os
from CLASSES import *
import json

with open("data/userdata.json", "r") as file:
    data = json.load(file)

def listSites(username):
    sites = None
    for i in data:
        if i['username'] == username:
            sites = i['data']

    return sites
    
def addSite(username, site, used, password):
    for i in data:
        if i['username'] == username:
            list_ = i['data']

    list_.append(Password(site, used, password).__dict__)

    with open('../data/userdata.json', 'w') as file:
        json.dump(data, file, indent=4)

def delete(user, site):
    for i in data:
        if i['username'] == user:
            sites = i['data']
    for i in sites:
        if i['site'] == site:
            index = sites.index(i)
            del sites[index]
    with open('../data/userdata.json', 'w') as file:
        json.dump(data, file, indent=4)

def update(site, newpasword, newusername, user):
    for i in data:
        if i['username'] == user:
            list_ = i['data']
    for i in list_:
        if i['site'] == site:
            i['used'] = newusername
            i['password'] = newpasword
    with open('../data/userdata.json','w') as file:
        json.dump(data, file, indent=4)