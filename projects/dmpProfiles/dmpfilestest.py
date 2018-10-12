#!/usr/bin/env python 

import json

profiles = []

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
        
    


DumpFile = "yuki.dmp"
prof1 = {'Name': 'Kyle', 'favorite_color': "Blue", 'default': 'yes'}
prof2 = {'Name': 'miru', 'favorite_color': "Blue", 'default': 'yes'}

#profiles.append(prof1)
#profiles.append(prof2)
#yuki_dump(profiles)

profiles = yuki_load()

list_users()



