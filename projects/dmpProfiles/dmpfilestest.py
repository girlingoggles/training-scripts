#!/usr/bin/env python3
import json
import Profile

DumpFile = "yuki.dmp"

prof1 = {'name': 'Kyle', 'favorite_color': "Red"}
prof2 = {'name': 'miru', 'favorite_color': "Blue"}

profile = Profile.Profile(DumpFile, False)
#profile.add_user(prof1)
#profile.add_user(prof2)
#profile.list_users()
print(profile.get_user("tom"))

#profiles = yuki_load()

#list_users()



