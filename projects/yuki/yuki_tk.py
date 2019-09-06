#!/usr/bin/env python3
#this is Yuki. She's here to help. Please be patient, she's learning.
#Yuki is made by girlingoggles

import datetime
from datetime import datetime
import random
import speak_number
from pprint import pprint
import requests
import Profile
import webbrowser
import sys, os
import urllib3
from geopy.geocoders import Nominatim
from colorama import Fore, Style
from tkinter import *
from PIL import Image, ImageTk

#import numpy as np
#from mpl_toolkits.basemap import Basemap
#import matplotlib.pyplot as plt

          
                
profile = Profile.Profile("yuki.dmp")
user = None

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        
        #Creation of init_window
    def init_window(self):
            
        # changing the title of our master widget
        self.master.title("YUKI ♥")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        self.showImg()
        main_menu()
#        self.yuki()
        #        self.showText()
        
        
    def showImg(self):
        load = Image.open("yhappy.png")
        render = ImageTk.PhotoImage(load)
        
        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        
        
        #    def showText(self):
        #        text = Label(self, text="Hey there good lookin!")
        #        text.pack()
        
#    def yuki(self):
#        yuki_ai.main_menu()





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
    run = True
    while run:
        act = input()
        act = act.lower()
        hi = set(['hi', 'hello', 'hey', 'yo', 'ey', 'yo', 'hiyo', 'hiya'])
        splt = act.split()
        if act in hi:
            print("Hi " + user["name"] + "! It's good to see you.")
            h = yes_no("Do you need help? ")
            if (h == True):
                act = act + str("yuki help")
        run = commands(act)






#Hamish's note:
def random_q():
    pass

    #try:
    #    asd()
    #except NameError as e:
    #    print(e)
        
def commands(act):
    if "yuki" in act:
#need to parse act
        if "can i" in act:
            print("I don't know, CAN you?") 
        elif "affirmation" in act:
            affirmation()
        elif " cake" in act: #this one looks better
            cake()
        elif " music" in act:
            music(act)
        elif " add" in act:
            add()
        elif " subtract" in act:
            subtract()
        elif " multiply" in act:
            multiply()
        elif " divide" in act:
            divide()
       # elif " favourite number" in act:
        #    favourite_num()
        elif " speak number" in act:
            speak_number.main_menu()
        elif " weather" in act:
            weather()
        elif " favourites" in act:
            favourites()
        elif " random" in act:
            random_q()
        elif "dice" in act or "roll" in act:
            dice_roll(act)
        elif "who are you" in act:
            who_am_i()
        elif "who am i" in act:
            who_are_you()
        elif " time" in act:
            time()
        elif " date" in act:
            date()
        elif " day" in act:
            day()
        elif "fortune" in act:
            fortune()
        elif "joke" in act:
            joke()
        elif "new user" in act:
            new_user()
        elif " location" in act:
            location()
        elif "iss" in act:
            iss()
        elif "heart" in act or "love" in act:
            heart()
        elif "go back" in act:
            return
        elif " leave" in act:
            return leave()
        elif " help" in act:
            help_list()
        elif "potato" in act:
            potato()
#        elif " map" in act:
#            maps()
        else: 
            print(Fore.MAGENTA + "I'm sorry, I don't know how to do that yet" + Style.RESET_ALL)
    else:
        chat(act)
            
    return True
    

def chat(act):

    bye = set(['bye', 'goodbye', 'see you', 'see ya', 'later'])
    night = set(['night', 'good night', 'goodnight', 'sleep well'])
    if "help" in act:
        help_list() 
    elif act in bye:
        print("Bye! See you soon! " + Fore.RED + "♥" + Style.RESET_ALL)
        print(Fore.BLACK + "I love you" + Style.RESET_ALL)
        exit(0)
    elif act in night:
        print("Good night! \nSleep well and have sweet dreams,\nI'll see you later " + Fore.RED + "♥" + Style.RESET_ALL)
        print(Fore.BLACK + "I love you" + Style.RESET_ALL)
        exit(0)  


    
def help_list():
    print("These are the things I can do for you.\nPlease type 'yuki' followed by one of the following commands:  \n")
    print("affirmation- " + Fore.BLUE + "I tell you a nice thing" + Style.RESET_ALL)
    print("fortune- " + Fore.BLUE + "I give you a fortune or saying" + Style.RESET_ALL)
    print("cake- " + Fore.BLUE + "I ask you about cake" + Style.RESET_ALL)
    print("music- " + Fore.BLUE + "I put on a youtube playlist" + Style.RESET_ALL)
    print("add- " + Fore.BLUE + "I add" + Style.RESET_ALL)
    print("subtract- " + Fore.BLUE + "I subtract" + Style.RESET_ALL)
    print("multiply- " + Fore.BLUE + "I multiply" + Style.RESET_ALL)
    print("divide- " + Fore.BLUE + "I divide" + Style.RESET_ALL)
    print("speak number- " + Fore.BLUE + "I spell out a number" + Style.RESET_ALL)
    print("weather- " + Fore.BLUE + "I tell you the weather" + Style.RESET_ALL)
    print("favourites- " + Fore.BLUE + "I ask you about your favourite things" + Style.RESET_ALL)
    print("joke- " + Fore.BLUE + "I tell you a joke" + Style.RESET_ALL)
    print("random- " + Fore.BLUE + "I give you a random number or thing" + Style.RESET_ALL)
    print("dice roll- " + Fore.BLUE + "choose from a D4, D6, D12 or D20 and I give you a number in that range" + Style.RESET_ALL)
    print("who are you- " + Fore.BLUE + "I tell you about myself" + Style.RESET_ALL)
    print("who am i- " + Fore.BLUE + "I tell you what I know about you" + Style.RESET_ALL)
    print("time- " + Fore.BLUE + "I tell you the time" + Style.RESET_ALL)
    print("date- " + Fore.BLUE + "I tell you today's date" + Style.RESET_ALL)
    print("day- " + Fore.BLUE + "I tell you the day of the week today" + Style.RESET_ALL)
    print("new user- " + Fore.BLUE + "You tell me yout name" + Style.RESET_ALL)
    print("location- " + Fore.BLUE + "you tell me your location" + Style.RESET_ALL)
    print("iss- " + Fore.BLUE + "I tell you the current location of the International Space Station" + Style.RESET_ALL)
    print("heart- " + Fore.BLUE + "I draw you a heart" + Style.RESET_ALL)
    print("go back- " + Fore.BLUE + "I go back to the previous menu" + Style.RESET_ALL)
    print("leave- " + Fore.BLUE + "You make me go back to the Void" + Style.RESET_ALL)


def affirmation():
    yn = 1
    nice = [ "All things are for the eventual best", "You've got this!", "Focus on what you can do, and you can do anything.", "You are Smaug", "Hakuna Matata: \nIt means No Worries!", "Being afraid of things going wrong isn't the way to make things go right. \nYou know this.", "Remember how far you've come, not just for far you have to go. \nYou are not where you want to be, but neither are you where you used to be", "Optimism is the faith that leads to achievement.", "Failure will never overtake me if my determination to succeed is strong enough.", "Good, better, best. Never let it rest 'til your good is better and your better is best.", "I love you", "It always seems impossible until it's done.", "It does not matter how slowly you go as long as you do not stop.", "We may encounter many defeats but we must not be defeated.", "I believe in you.", "You have already won.\nEverything else is extra."]
    print(random.choice(nice))
    while yes_no("more?"):
        print(random.choice(nice))

def dice_roll(act):
    if "4" in act:
        dice4 = [ "1", "2", "3", "4"]
        print("test")
        print(random.choice(dice4))
        while yes_no("roll again?"):
            print(random.choice(dice4))
    elif "6" in act:
        dice6 = [ "1", "2", "3", "4", "5", "6"]
        print(random.choice(dice6))
        while yes_no("roll again?"):
            print(random.choice(dice6))
    elif "12" in act:
        dice12 = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        print(random.choice(dice12))
        while yes_no("roll again?"):
            print(random.choice(dice12))
    elif "20" in act:
        dice20 = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
        print(random.choice(dice20))
        while yes_no("roll again?"):
            print(random.choice(dice20))
    else:
        act = input("would you like to roll a D4, D6, D12, or D20 die?")
        if "4" in act:
            dice4 = [ "1", "2", "3", "4"]
            print(random.choice(dice4))
            while yes_no("roll again?"):
                print(random.choice(dice4))
        elif "6" in act:
            dice6 = [ "1", "2", "3", "4", "5", "6"]
            print(random.choice(dice6))
            while yes_no("roll again?"):
                print(random.choice(dice6))
        elif "12" in act:
            dice12 = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
            print(random.choice(dice12))
            while yes_no("roll again?"):
                print(random.choice(dice12))
        elif "20" in act:
            dice20 = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
            print(random.choice(dice20))
            while yes_no("roll again?"):
                print(random.choice(dice20))

def add():
    num1 = int(input("First number please: "))
    num2 = int(input("Second number please: "))
    print(num1, "+", num2, "=", num1 + num2)

    
def subtract():
    num1 = int(input("First number please: "))
    num2 = int(input("Second number please: "))
    print(num1, "-", num2, "=", num1 - num2)
    
def multiply():
    num1 = int(input("First number please: "))
    num2 = int(input("Second number please: "))
    print(num1, "-", num2, "=", num1 * num2)
    
def divide():
    num1 = int(input("First number please: "))
    num2 = int(input("Second number please: "))
    print(num1, "-", num2, "=", num1 / num2)
    
def favourite_num():
    pass

def favourites():
    pass

def who_are_you():
    pass

def new_user():
    pass

def joke():
    j = requests.get('https://official-joke-api.appspot.com/jokes/random')
    joke = j.json()
    setup = joke["setup"]
    punch = joke["punchline"]
    print(setup)
    wait_key()
    print(punch)

def location():
     while True:
         if ("city" not in user or user["city"] == None or "country" not in user or user["country"]  == None):
             user["city"] = input("What city are you in? \n")
             user["country"] = input("What country are you in? Abbreviations only please \n")
             profile.save()
             print("You live in ", user["city"], ", ",
                   user["country"])
             loc = yes_no("Did I get that right?\n")
             if (loc == True):
                 print("Thank you, I'll remember that!")
                 return False
         else:
             update= yes_no("I already have a location set for you. Would you like to update it?\n")
             if (update == True):
                 user["city"] = None
                 user["country"] = None
                 profile.save()
             else:
                 print("I'll remember that you live in " + user["city"], ", ", user["country"], " then!")
                 return False

def iss():
    #pass
    l = requests.get('http://api.open-notify.org/iss-now.json')
    loc = l.json()
    lat = float(loc["iss_position"]["latitude"])
    lon = float(loc["iss_position"]["longitude"])
    print("The ISS is curently located at:\nLatitude: ", lat, "\nLongitude: ", lon)
    geolocator = Nominatim(timeout=10)
    location = geolocator.reverse(lat, lon)
    print(location.address)

def potato():
    print("I like potatoes ^.^")
    print(Fore.YELLOW + "                                            ▓▓            ")
    print("                                          ████            ")
    print("                                        ██  ██      ██    ")
    print("                                      ██    ████████      ")
    print("                                    ██            ██      ")
    print("                                      ██          ██      ")
    print("                            ██████      ██        ████████")
    print("                      ████████▒▒██████    ██          ██  ")
    print("                    ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒████  ██      ██    ")
    print("                ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ██  ██      ")
    print("                ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒██  ██        ")
    print("              ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒██            ")
    print("            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒██          ")
    print("    ██████████▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██          ")
    print("  ██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒████        ")
    print("██▒▒▒▒▒▒████▒▒▒▒▒▒▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒██      ")
    print("██▒▒████  ██▒▒▒▒▒▒▒▒████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒██    ")
    print("████    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ██▒▒██    ")
    print("        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    ██▒▒██    ")
    print("        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████      ██▒▒██    ")
    print("          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████          ████      ")
    print("          ██████▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██                      ")
    print("        ██▒▒▒▒▒▒████████████▒▒▒▒▒▒▒▒██                    ")
    print("        ██▒▒▒▒▒▒██          ██▒▒▒▒▒▒██                    ")
    print("        ████████            ██▒▒▒▒▒▒██                    ")
    print("                              ██████                      " + Style.RESET_ALL)





    
def heart():
    print("   I love you!\n")  
    print(Fore.RED + "  .:::.   .:::.")
    print(" :::::::.:::::::")
    print(" :::::::::::::::")
    print(" ':::::::::::::'")
    print("   ':::::::::'")
    print("     ':::::'")
    print("       ':'\n" + Style.RESET_ALL)
    print("I hope you don't mind.")
    
def fortune():
    f = requests.get('http://yerkee.com/api/fortune')
    fortune = f.json()
    print(fortune["fortune"])
    
def time():
    now = datetime.datetime.now()
    print("It is currently: ")
    print(now.strftime("%X %p %Z"))

def date():
    now = datetime.datetime.now()
    print("Today is: ")
    print(now.strftime("%x"))

def day():
    now = datetime.datetime.now()
    print("Today is: ")
    print(now.strftime("%A"))


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
                  " outside, feels like " + str(weather["main"]["temp"]) + "C. \n" + "The wind is " + str(weather["wind"]["speed"]) + " kph" +
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
    ''' Wait for a key press on the console and return it. Pulled from StackExchange'''
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


def music(act):

    if len(profile.music) < 1:
        profile.music = {"lofi": "https://www.youtube.com/watch?v=y3Z8ot_4HX4", "trance": "https://www.youtube.com/watch?v=buqNTkjTY20", "dubstep": "https://www.youtube.com/watch?v=a41icW_FtsI", "ghibli": "https://www.youtube.com/watch?v=YjohMzHkBqI", "samurai": "https://www.youtube.com/watch?v=jrTMMG0zJyI", "violin": "https://www.youtube.com/watch?v=jvipPYFebWc&start_radio=1&list=RD\EMzT1XwmFnIup_KYXuc2rUZA","chill": "https://www.youtube.com/watch?v=G2WneYqu-ao","glitch": "https://www.youtube.com/watch?v=52Qug_siqKw"}
        profile.save()
    mus = profile.music
    words = act.split()
    title = ""
    for word in words[:]:
        if word in mus:
            title = word
            print("Found " + word + " in music")
            if title == "":
                print("these are the things i can play: ")
        songs = list(mus.keys())
        for song_list in songs:
            if song_list == songs[-1]:
                print("or " + song_list)
            else:
                print(song_list, end =", ")
            
        song = input("which of these would you like? \nIf none, I can add your favourite.\n")
        song = song.lower()
        if song in mus:
            title = song    
        else:
            cont = True
            while cont:
                if song == "" or song == "none":
                    song = input("What music would you like me to add?")
                song = song.lower()
                if yes_no("so you want to add a new song to the lable:" + song + ": right?"):
                    new_link = input("Can you give me the link as well please?")
                    if yes_no("so the new song :" + song + ": should open the link " + new_link + " is this correct?"):
                        mus[song] = new_link
                        title = song
                        cont = False
                        profile.save()
                    else:
                        print("Let's try that again")
                        song = ""
                else:
                    return False
    print(title + "'s link is " + mus[title])
    webbrowser.open(mus[title])                 

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
    
    
def cake():
    sweet = yes_no("Do you like cake?")
    if sweet == True:
        print("The cake is a lie")
        print("But you already knew that.")
        print(" ")
    else:
        print("The cake is a lie anyway")
        print("Which do you like?")
        sugar = input("Pie IceCream Cookies Candy\n")
        sugar = sugar.lower()
        if sugar == 'pie':
            print("Pie is a fantastic choice!")
        elif sugar == 'icecream' or sugar == 'ice cream':
            print("IceCream is so cold!")
        elif sugar == 'cookies':
            print("Anzac, chocolate chip, coconut... There are so many!")
        elif sugar == 'candy':
            print("Too many varieties of sweets to list, too many to try!")
        else:
            sugar = False
            print("Is that a dessert?")
        if sugar == False:
            print("I'll have to look into this")
            print(" ")
        else:
            print("I like ", sugar, "too!")
                
                
    
def leave():
    print("It will be lonely without you here.")
    print("but if you must...")
    if yes_no("Must you?\n"):
        print("Goodbye then. I'm glad you stopped by.")
        print("I hope I'll see you again soon.")
        print(Fore.BLACK + "I love you" + Style.RESET_ALL)
        return False
    else:
        print("I'm glad you can stay with me for a little longer.")
        print("What would you like to do now?")
        print(" ")
        return True

def affirmation():
    yn = 1
    nice = [ "All things are for the eventual best", "You've got this!", "Focus on what you can do, and you can do anything.", "You are Smaug", "Hakuna Matata: \nIt means No Worries!", "Being afraid of things going wrong isn't the way to make things go right. \nYou know this.", "Remember how far you've come, not just for far you have to go. \nYou are not where you want to be, but neither are you where you used to be", "Optimism is the faith that leads to achievement.", "Failure will never overtake me if my determination to succeed is strong enough.", "Good, better, best. Never let it rest 'til your good is better and your better is best.", "I love you", "It always seems impossible until it's done.", "It does not matter how slowly you go as long as you do not stop.", "We may encounter many defeats but we must not be defeated.", "I believe in you.", "You have already won. \nEverything else is extra."]
    print(random.choice(nice))
    while yes_no("more?"):
        print(random.choice(nice))

'''def maps():
    # miller projection
    map = Basemap(projection='mill',lon_0=180)
    # plot coastlines, draw label meridians and parallels.
    map.drawcoastlines()
    map.drawparallels(np.arange(-90,90,30),labels=[1,0,0,0])
    map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,60),labels=[0,0,0,1])
    # fill continents 'coral' (with zorder=0), color wet areas 'aqua'
    map.drawmapboundary(fill_color='aqua')
    map.fillcontinents(color='coral',lake_color='aqua')
    # shade the night areas, with alpha transparency so the
    # map shows through. Use current time in UTC.
    date = datetime.utcnow()
    CS=map.nightshade(date)
    plt.title('Day/Night Map for %s (UTC)' % date.strftime("%d %b %Y %H:%M:%S"))
    plt.show()
'''


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

                
root = Tk()

root.geometry("500x500")

app = Window(root)      

    
if ( __name__ == "__main__"):
    main_menu()
        
        
                    
    
