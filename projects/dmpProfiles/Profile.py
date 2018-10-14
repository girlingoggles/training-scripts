#!/usr/bin/env python3
import json

class Profile:

    def __init__(self, file_name = "profile.dmp", verbose = False, username = "name"):
        self.verbose = verbose
        if self.verbose and file_name == "profile.dmp":
            print("file name not specified. using default file name (" + file_name + ") instead.")
        self.DumpFile = file_name
        self.username = username
        self.profiles = {}
        try:
            open(self.DumpFile, 'r')
            self.load()
        except FileNotFoundError:
            if self.verbose: print("Dump file (" + self.DumpFile + ") not found, creating new file.")

        self.save()
        
    def save(self):
        with open(self.DumpFile, 'w') as outfile:  
            json.dump(self, outfile, default=lambda o: o.__dict__,
                sort_keys=True, indent=4)

    def load(self):

        with open(self.DumpFile, 'r') as json_file:  
            hold = json.loads(json_file.read())
            for key in hold:
                setattr(self, key, hold[key])

    def list_users(self):

        for user in self.profiles.keys():
            print(user)
        
    def set_default(self, username):

        username.lower()
        if (self.profiles[username] != None):
            self.defaultUser = username
            self.save()
        else:
            return False


    def add_user(self, user, default = False):

        username = user[self.username]
        username = username.lower()
        if (len(self.profiles.keys()) == 0):
            self.defaultuser = username
        self.profiles[username] = user
        self.save()
        return self.get_user(username)

    def get_user(self, user):
        user = user.lower()
        try:
            return self.profiles[user]
        except KeyError:
            return None

    def get_user_num(self):

        return len(self.profiles.keys())
