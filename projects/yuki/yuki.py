#!/usr/bin/env python3
#This is Yuki. She's here to help.
#Please be patient, she's learning.
#Yuki is made by girlingoggles

import datetime
import random
import speak_number
from pprint import pprint
import requests
import Profile

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
#    all_done = 0
    #unless you are going to change all_done, hard-code whileloops
    print("Hello")
    print("My name is Yuki. I'm here to help")
    while True:
        print("Would you like to: ")
        print("chat")
        print("affirmation")
        print("math")
        print("cake")
        print("music")
        print("leave")
        answer = input("\nPlease choose one: \n")
        answer.lower()
        
        
        if answer == "chat":
            have_chat()
        elif answer == "affirmation":
            affirmation()
        elif answer == "math":
            do_math()
        elif answer == "cake":
            cake()
        elif answer == "music":
            music()
        elif answer == "leave":
            if leave():
                return
        else:
            print("\nTry again: \n")


def do_math():
    repeat = True
    while repeat:
        print("You can: ")
        print("0. go back")
        print("1. do basic math")
        print("2. tell me your favourite number")
        print("3. say a number")
        answer = input("Please choose 0-3: ")

        if answer == "1" or answer == "1.":
            #you are returning booleans in basic_math but not catching them
            basic_math()
        elif answer == "2" or answer == "2.":
            favourite_num()
        elif answer == "3" or answer == "3.":
            speak_number.main_menu()
        elif answer == "0" or answer == "0." or answer == "back":
            repeat = False

def basic_math():
    calc = True
    while calc:
        def add(x,y):
            return x + y
        def subtract(x, y):
            return x - y
        def multiply(x, y):
            return x * y
        def divide(x, y):
            return x / y
        print("Would you like to: ")
        print("0. go back")
        print("1. add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
    
        act = input("I would like to: ")
        print(act)
        if act == '0' or act == '0.' or act == '0. ' or act == 'go back' or act == 'back':
            return False

        num1 = int(input("First number please: "))
        num2 = int(input("Second number please: "))
        if act == '1' or act == '1.' or act == '1. ' or act == 'add':
            print(num1, "+", num2, "=", add(num1, num2))
        elif act == '2' or act == '2.' or act == '2. ' or act == 'subtract':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif act == '3' or act == '3.' or act == '3. ' or act == 'multiply':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif act == '4' or act == '4.' or act == '4. ' or act == 'divide':
            if (num2 == 0):
                print("Please don't hurt me like that")
            else:
                print(num1, "/", num2, "=", divide(num1, num2))
        else:
            print("Please choose a number")
            
        calc = yes_no("again?")
        #you could deal with calc here (inside the while loop but outside the ifs
        #can also be done easier by using the boolean return from yes_no directly
        #ie: calc = yes_no("more?")
            
#    favourite_num()
#    errors = 0




    
def have_chat():
    talk = True
    while True:
        print("What would you like to talk about?")
        print("0. go back")
        print("1. weather")
        print("2. favourites")
        print("3. random")
        print("4. who am I?")
        ch = input("I would like to: ")
        print(ch)
        ch = ch.lower()
        if ch == "0" or ch == "0." or ch == "go back":
            return False
        elif ch == "1" or ch == "1." or ch == "weather":
#            if (user{"location"} == None):
            if value not in Profile.location():
                loc = True
                loc_city = input("What city are you in?")
                print(loc_city)
                loc_country = input("What country are you in? Abbreviations only please")
                print(loc_country)
                Profile.save()
            else:
                Profile.load()
                print("Your location is ", loc_city, ", ", loc_country)
                loc = yes_no("Is that right?")
                r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID={APIKEY}')
                pprint(r.json())
            
        #           Profile.save()  ?
        
            


'''
    # Maybe you should have a seperate function for Date, and lets chat could be more interactive. 
    #    yn = yes_no("Do you want to know something?\n")
    if yes_no("Do you want to know something?\n"):
        t = datetime.datetime.now().strftime("%A, %d/%m/%Y")
        print("Today is", t, "!")
        print("And I think you're awesome")
        print("Thanks for talking to me!")
        print(" ")
    else:
        print("Well, that went well.")
        print(" ")
   '''     
    
def affirmation():
    yn = 1
    nice = [ "All things are for the eventual best", "You've got this!", "Focus on what you can do, and you can do anything.", "You are Smaug", "Hakuna Matata: \nIt means No Worries!", "Being afraid of things going wrong isn't the way to make things go right. \nYou know this.", "Remember how far you've come, not just for far you have to go. \nYou are not where you want to be, but neither are you where you used to be", "Optimism is the faith that leads to achievement.", "Failure will never overtake me if my determination to succeed is strong enough.", "Good, better, best. Never let it rest 'til your good is better and your better is best.", "I love you", "It always seems impossible until it's done.", "It does not matter how slowly you go as long as you do not stop.", "We may encounter many defeats but we must not be defeated.", "I believe in you.", "You have already won. \nEverything else is extra."]
    print(random.choice(nice))
    while yes_no("more?"):
        print(random.choice(nice))
        

        
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
            
#def music():

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


#I have no idea what I'm doing but I'm pretty sure these are wrong?
#user = Profile.Profile(DumpFile, False)
#profile = profile.add_user(prof) 
    
if ( __name__ == "__main__"):
    main_menu()
