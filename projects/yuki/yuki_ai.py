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
           

def main_menu():
    print("Hi! My name is Yuki. I'm here to help")
    get_user()
    print("Hello " + user["name"])
# act should not be global
    while True:
        act = input()
        act = act.lower()
#should command be an array or a function call?    
#    command = (['affirmation', 'cake', 'music', 'add', 'subtract', 'multiply', 'divide', 'favourite number', 'speak number', 'weather', 'favourites', 'random', 'dice roll', 'roll dice', 'who am i', 'time', 'date', 'new user', 'location', 'heart', 'go back', 'leave', 'help'])
        commands(act)
        #chat()
    
def commands(act):
    comm = True
    while comm:
        if "yuki" in act:
#need to parse act
        
            if " affirmation" in act:
                affirmation()
            elif " cake" in act: #this one looks better
                cake()
            elif " music" in act:
                music()
            elif " add" in act:
                add()
            elif " subtract" in act:
                subtract()
            elif " multiply" in act:
                multiply()
            elif " divide" in act:
                divide()
            elif " favourite number" in act:
                favourite_num()
            elif " speak number" in act:
                speak_number.main_menu()
            elif " weather" in act:
                weather()
            elif " favourites" in act:
                favourites()
            elif " random" in act:
                random_q()
            elif ("dice roll" or "roll dice") in act:
                dice_roll()
            elif "who are you" in act:
                who_am_i()
            elif " time" in act:
                time()
            elif " date" in act:
                date()
            elif "new user" in act:
                new_user()
            elif " location" in act:
                location()
            elif " heart" in act:
                heart()
            elif "go back" in act:
                return
            elif " leave" in act:
                leave()
            elif " help" in act:
                help_list()
            else:
                print("I'm sorry, I don't know how to do that yet")
        comm = False
            #            continue
            
def help_list():
    print("These are the things I can do for you: ")
    print("affirmation- I tell you a nice thing")
    print("cake- I ask you about cake")
    print("music- I put on a youtube playlist")
    print("add- I add")
    print("subtract- I subtract")
    print("multiply- I multiply")
    print("divide- I divide")
    print("favourite number- I ask your favourite number")
    print("speak number- I spell out a number")
    print("weather- I tell you the weather")
    print("favourites- I ask you about your favourite things")
    print("random- I give you a random number or thing")
    print("dice roll- Igive you a random number from 1 to 6")
    print("who are you- I tell you about myself")
    print("who am i- I tell you what I know about you")
    print("time- I tell you the time")
    print("date- I tell you today's date")
    print("new user- You tell me yout name")
    print("location- you tell me your location")
    print("heart- I draw you a heart")
    print("go back- I go back to the previous menu")
    print("leave- You make me go back to the Void")
    return
    
#def time():


def weather():
    while True:
        if ("city" not in user or user["city"] == None or "country" not in user or user["country"]  == None):
            user["city"] = input("What city are you in? \n")
            user["country"] = input("What country are you in? Abbreviations only please \n")
            profile.save()
                                                                        #should relook at this part again later
        print("You live in ", user["city"], ", ",
                  user["country"])
        loc = yes_no("Did I get that right?\n")
        if (loc == True):
            r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + user["city"] + ',' + user["country"] + '&units=metric&APPID=99f075d4add9b18987e3c66aa77f33a3')
            weather = r.json()
            d = int(weather["wind"]["speed"])
            print("Looks like " +
                  weather["weather"][0]["description"] +
                  " outside, feels like " + str(weather["main"]["temp"]) + "C. \n" + "The wind is" + str(weather["wind"]["speed"]) + " kph" +
                  " in a " + cardinal(d)
                  + "-ish sort of a direction.")
            return False
        else:
            user["city"] = None
            user["country"] = None
            profile.save()
            
            
def cardinal(d):
    dir = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    met = int((d + 11.25)/22.5)
    return dir[met % 16]

def who_am_i():
    print("Who am I?\nWhy, I'm Yuki, silly!")
    wait_key()
    print("I was created on 10/09/2018, originally a simple tutorial program named example1, but like most of Miru's projects, I got a little out of hand.")
    wait_key()
    print("Now I can do all sorts of things, and I'm only getting better every day!")
    wait_key()
    print("I can do basic math, tell you the weather, play you some of Miru's favourite music, and tell you nice things to keep you going.")
    wait_key()
    print("I hope you'll keep me around, and update me when you can, to see what else I learn and become!")
    wait_key()
    print("Thank you so much for believing in me!")

def wait_key():
    ''' Wait for a key press on the console and return it. '''
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()
    else:
        import termios
        fd = sys.stdin.fileno()
        
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        
        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            
    return result

def music():
    print("I can offer you a selection of: ")
    print("lofi\ntrance\ndubstep\nghibli\nsamurai\nviolin\nchill\nglitch")
    mus = input("I want to listen to: \n")
    mus = mus.lower()
    if mus == 'lofi':
        webbrowser.open('https://www.youtube.com/watch?v=dJhW1J6gIWA')
    elif mus == 'trance':
        webbrowser.open('https://www.youtube.com/watch?v=buqNTkjTY20')
    elif mus == 'dubstep':
        webbrowser.open('https://www.youtube.com/watch?v=a41icW_FtsI')
    elif mus == 'ghibli':
        webbrowser.open('https://www.youtube.com/watch?v=YjohMzHkBqI')
    elif mus == 'samurai':
        webbrowser.open('https://www.youtube.com/watch?v=jrTMMG0zJyI')
    elif mus == 'violin':
        webbrowser.open('https://www.youtube.com/watch?v=jvipPYFebWc&start_radio=1&list=RD\EMzT1XwmFnIup_KYXuc2rUZA')
    elif mus == 'chill':
        webbrowser.open('https://www.youtube.com/watch?v=G2WneYqu-ao')
    elif mus == 'glitch':
        webbrowser.open("https://www.youtube.com/watch?v=52Qug_siqKw")
    print("I hope you like it!\n")

    
def leave():
    print("It will be lonely without you here.")
    print("but if you must...")
    if yes_no("Must you?\n"):
        print("Goodbye then. I'm glad you stopped by.")
        print("I hope I'll see you again soon.")
        return True
    else:
        print("I'm glad you can stay with me for a little longer.")
        print("What would you like to do now?")
        print(" ")
        return False
                                                                                        

def get_user():

#should declare using the profile var like you did the user    
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
        
        
                    
    
