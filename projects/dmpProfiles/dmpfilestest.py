#!/usr/bin/env python3
import json
import Profile

DumpFile = "yuki.dmp"

prof1 = {'name': 'Kyle', 'favorite_color': "Red"}
prof2 = {'name': 'miru', 'favorite_color': "Blue"}

test_profile = Profile.Profile(DumpFile, False)

if (test_profile.new):
    yuki("hi I don't know anyone yet")

user = test_profile.get_user("kyle"))

user.favorite_snack = "cookies"
test_profile.save()
user.larp_charictar_name = "Karth"
test_profile.save()
    
test_profile.add_user(prof1)
test_profile.add_user(prof2)
#profile.list_users()
print(test_profile.get_user("tom"))



#profiles = yuki_load()

#list_users()



