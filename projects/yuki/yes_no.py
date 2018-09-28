#!/usr/bin/env python3

def yes_no( str ):

    while (1):
        answer = input(str)
        answer = answer.lower()
        if (answer == "y" or answer == "yes" or answer == "yep"):
            return True
        elif (answer == "n" or answer == "no" or answer == "nah"):
            return False
        else:
            print("Not a valid response. Try again.")
        

if (yes_no("Does this work? ")):
    print("YES!!")
else:
    print("NO!!")
