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
            fh = open(self.DumpFile, 'r')
            self.load()
            self.new = False
        except FileNotFoundError:
            if self.verbose: print("Dump file (" + self.DumpFile + ") not found, creating new file.")
            self.new = True

        self.save()
        
    def toJSON(self):
                return json.dumps(self, default=lambda o: o.__dict__,
                                              sort_keys=True, indent=4)
        
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

        self.defaultUser = self.profiles[username][self.username]
        self.save()


    def add_user(self, user, default = False):

        if (len(self.profiles.keys()) == 0):
            self.defauluser = user[self.username]
        self.profiles[user[self.username].lower()] = user

        self.save()

    def get_user(self, user):
        try:
            return self.profiles[user.lower()]
        except KeyError:
            return None
