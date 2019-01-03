#!/usr/bin/env python3
#this is Yuki. She's here to help. Please be patient, she's learning.
#Yuki is made by girlingoggles

import datetime
import random
import speak_number
from pprint import pprint
import requests
import Profile
import webbrowser
import sys, os


'''
def yes_no(question):
    yes = set(['yes', 'y', 'ye', 'yea', 'yeah', 'yep', 'yup', 'ya', ' '])
    no = set(['no', 'nope', 'n', 'nah', 'na', 'neh'])
    
    while True:
    yn = input(question)
    yn = yn.lower()
    if yn in yes:
        return True
    elif yn in no:
        return False
    else:
        print("\nyes or no only, please.\n")
       

class Yuki(object):
    YUKI_CALL = ["yuki,", "yuki", "@yuki"]
    '''

def main_menu():
    print("Hi! My name is Yuki. I'm here to help")
    get_user()
    print("Hello " + user["name"])
    act = input(chat)
    act = act.lower()
    command = (['affirmation', 'cake', 'music', 'add', 'subtract', 'multiply', 'divide', 'favourite number', 'speak number', 'weather', 'favourites', 'random', 'dice roll', 'roll dice', 'who am i', 'time', 'date', 'new user', 'location', 'heart', 'go back', 'leave', 'help'])
    
    if command in act and "yuki," in act:
        commands()

    
def commands():
    if command == "affirmation":
        affirmation()
    elif command == "cake":
        cake()
    elif command == "music":
        music()
    elif command == "add":
        add()
    elif command == "subtract":
        subtract()
    elif command == "multiply":
        multiply()
    elif command == "divide":
        divide()
    elif command == "favourite number":
        favourite_num()
    elif command == "speak number":
        speak_number.main_menu()
    elif command == "weather":
        weather()
    elif command == "favourites":
        favourites()
    elif command == "random":
        random_q()
    elif command == "dice roll" or command == "roll dice":
        dice_roll()
    elif command == "who am i":
        who_am_i()
    elif command == "time":
        time()
    elif command == "date":
        date()
    elif command == "new user":
        new_user()
    elif command == "location":
        location()
    elif command == "heart":
        heart()
    elif command == "go back":
        return
    elif command == "leave":
        leave()
    elif command == "help":
        help_list()
    else:
        print("I'm sorry, I don't know how to do that yet")
    
def help_list():
    print("These are the things I can do for you: ")
    print("affirmation")
    print("cake")
    print("music")
    print("add")
    print("subtract")
    print("multiply")
    print("divide")
    print("favourite number")
    print("speak number")
    print("weather")
    print("favourites")
    print("random")
    print("dice roll")
    print("who am i")
    print("time")
    print("date")
    print("new user")
    print("location")
    print("heart")
    print("go back")
    print("leave")

    
#def time():
   
def get_user():
    
    global user
    if (profile.get_user_num() == 0):
        print("I don't know anyone, yet")
        username = input("What's your name? ")
        user = profile.add_user({"name" : username})
    elif (profile.defaultuser != None and profile.defaultuser != ""):
        user = profile.get_user(profile.defaultuser);
    else:
        print("users exist, but no default user set")
        while (user == None):
            profile.list_users()
            username = input("please pick from the list of users")
            user = profile.get_user(username)
            if (user == None):
                print("please enter one of the usernames listed")

                
                
    profile = Profile.Profile("yuki.dmp")
    user = None
    
if ( __name__ == "__main__"):
    main_menu()
        
        
                    
    
