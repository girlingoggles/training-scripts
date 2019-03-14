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
import urllib3



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
        hi = set(['hi', 'hello', 'hey', 'yo', 'ey', 'yo', 'hiyo'])
        bye = set(['bye', 'goodbye', 'see you', 'see ya', 'later'])
        night = set(['night', 'good night', 'sleep well'])
        splt = act.split()
        if act in hi:
            print("Hi " + user["name"] + "! It's good to see you.")
            h = yes_no("Do you need help?")
            if (h == True):
                help_list()
            else:
                pass
        else:
            pass    
        run = commands(act)
        if "help" in act:
            help_list() 
        #chat()
        if act in bye:
            print("Bye! See you soon! ♥")
            return False
        if act in night:
            print("Good night! \nSleep well and have sweet dreams,\nI'll see you later ♥")
            return False


        
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
        if " affirmation" in act:
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
        elif "can" in act:
            print("I don't know, CAN you?")
        elif "potato" in act:
            potato()
        else:
            print("I'm sorry, I don't know how to do that yet")
    return True
            
def help_list():
    print("These are the things I can do for you.\nPlease type 'yuki' followed by one of the following commands:  \n")
    print("affirmation- I tell you a nice thing")
    print("fortune- I give you a fortune or saying")
    print("cake- I ask you about cake")
    print("music- I put on a youtube playlist")
    print("add- I add")
    print("subtract- I subtract")
    print("multiply- I multiply")
    print("divide- I divide")
    print("speak number- I spell out a number")
    print("weather- I tell you the weather")
    print("favourites- I ask you about your favourite things")
    print("joke- I tell you a joke")
    print("random- I give you a random number or thing")
    print("dice roll- choose from a D4, D6, D12 or D20 and I give you a number in that range")
    print("who are you- I tell you about myself")
    print("who am i- I tell you what I know about you")
    print("time- I tell you the time")
    print("date- I tell you today's date")
    print("day- I tell you the day of the week today")
    print("new user- You tell me yout name")
    print("location- you tell me your location")
    print("iss- I tell you the current location of the International Space Station")
    print("heart- I draw you a heart")
    print("go back- I go back to the previous menu")
    print("leave- You make me go back to the Void")


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
    lat = loc["iss_position"]["latitude"]
    lon = loc["iss_position"]["longitude"]
    print("The ISS is curently located at:\nLatitude: ", lat, "\nLongitude: ", lon)

def potato():
    print("                                            ▓▓            ")
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
    print("                              ██████                      ")





    
def heart():
    print("   I love you!\n")
    print("  .:::.   .:::.")
    print(" :::::::.:::::::")
    print(" :::::::::::::::")
    print(" ':::::::::::::'")
    print("   ':::::::::'")
    print("     ':::::'")
    print("       ':'\n")
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
        
        
                    
    
