#!/usr/bin/env python 
import json

profiles = []
DumpFile = "yuki.dmp"

#REQUIREMENTS LIST:
#Global array of profiles(class or dict)
#Global dmp file name (settable?)
#Functions:
#dump/save 
#load    Assign global profiles, but return profiles or default user?
#list users
#reassign default (index 0)


def yuki_dump(x):

    with open(DumpFile, 'w') as outfile:  
        json.dump(x, outfile)

def yuki_load():

    with open(DumpFile, 'r') as json_file:  
        data = json.loads(json_file.read())
    return data

def list_users():

    for user in profiles:
        print(user['Name'])
        
def set_default(user):

    profiles.remove(user)
    profiles.insert(0, user)
    


prof1 = {'Name': 'Kyle', 'favorite_color': "Blue", 'default': 'yes'}
prof2 = {'Name': 'miru', 'favorite_color': "Blue", 'default': 'yes'}

#profiles.append(prof1)
#profiles.append(prof2)
#yuki_dump(profiles)

profiles = yuki_load()

list_users()



