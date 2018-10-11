#!/usr/bin/env python3
#This is Yuki. She's here to help.
#Please be patient, she's learning.
#Yuki is made by girlingoggles

import datetime
import random


def yes_no(yn):
    yes = set(['yes', 'y', 'ye', 'yea', 'yeah', 'yep', 'yup'])
    no = set(['no', 'nope', 'n', 'nah', 'na'])
    alldone = 1
    
    while not alldone:
        yn = input()
        yn = yn.lower()
        if yn in yes:
            return 1
        elif yn in no:
            return 0
        else:
            print("\nyes or no only, please.\n")

def main_menu():
    all_done = 0
    while not all_done:
        print("Would you like to: ")
        print("chat")
        print("affirmation")
        print("math")
        print("cake")
        print("music")
        print("leave")
        answer = input("\nPlease choose one: \n").lower()
        
        
        if answer == "chat":
            have_chat(yn)
        elif answer == "affirmation":
            affirmation()
        elif answer == "math":
            number_loop()
        elif answer == "cake":
            cake()
        elif answer == "music":
            music()
        elif answer == "leave":
            leave
        else:
            print("\nTry again: \n")


#def number_loop(num):


def have_chat(yn):
    yes_no(input("Do you want to know something?\n"))
    if yn == 1:
        t = datetime.datetime.now().strftime("%A, %d/%m/%Y")
        print("Today is", t, "!")
        print("And I think you're awesome")
        print("Thanks for talking to me!")
        print(" ")
    else:
        print("Well, that went well.")
        print(" ")
    
def affirmation():
    yn = 1
    nice = [ "All things are for the eventual best", "You've got this!", "Focus on what you can do, and you can do anything.", "You are Smaug", "Hakuna Matata: \nIt means No Worries!", "Being afraid of things going wrong isn't the way to make things go right. \nYou know this.", "Remember how far you've come, not just for far you have to go. \nYou are not where you want to be, but neither are you where you used to be", "Optimism is the faith that leads to achievement.", "Failure will never overtake me if my determination to succeed is strong enough.", "Good, better, best. Never let it rest 'til your good is better and your better is best.", "I love you", "It always seems impossible until it's done.", "It does not matter how slowly you go as long as you do not stop.", "We may encounter many defeats but we must not be defeated." ]
    while yn == 1:
        print(random.choice(nice))
        yes_no(input("more?"))
    else:
        return 0
        
#def cake():

#def music():

#def leave():


yn = 1
print("Hello")
print("My name is Yuki. I'm here to help")
main_menu()
