#!/usr/bin/env python3
#girlingoggles made this

# phase 4: fix for commented inputs
# 0
# 20000000
# negitives
# decimals
# non number input #parsing input

import sys
import math

def speak_number_ones(one):
    if one == 1:
        print("one", end = ' ')
    elif one == 2:
        print("two", end = ' ')
    elif one == 3:
        print("three", end = ' ')
    elif one == 4:
        print("four", end = ' ')
    elif one == 5:
        print("five", end = ' ')
    elif one == 6:
        print("six", end = ' ')
    elif one == 7:
        print("seven", end = ' ')
    elif one == 8:
        print("eight", end = ' ')
    elif one == 9:
        print("nine", end = ' ')


def speak_number_teens(teen):
    if teen == 10:
        print("ten", end = ' ')
    elif teen == 11:
        print("eleven", end = ' ')
    elif teen == 12:
        print("twelve", end = ' ')
    elif teen == 13:
        print("thirteen", end = ' ')
    elif teen == 14:
        print("fourteen", end = ' ')
    elif teen == 15:
        print("fifteen", end = ' ')
    elif teen == 16:
        print("sixteen", end = ' ')
    elif teen == 17:
        print("seventeen", end = ' ')
    elif teen == 18:
        print("eighteen", end = ' ')
    elif teen == 19:
        print("nineteen", end = ' ')

        
def speak_number_tens(number):

    ten = int(number / 10)

    if ten == 1:
        speak_number_teens(number)
        return 
    elif ten == 2:
        print("twenty", end = ' ')
    elif ten == 3:
        print("thirty", end = ' ')
    elif ten == 4:
        print("fourty", end = ' ')
    elif ten == 5:
        print("fifty", end = ' ')
    elif ten == 6:
        print("sixty", end = ' ')
    elif ten == 7:
        prinmt("seventy", end = ' ')
    elif ten == 8:
        print("eighty", end = ' ')
    elif ten == 9:
        print("ninety", end = ' ')
    speak_number_ones(int(number % 10))

def speak_number_hundreds(number):

    hundred=int(number / 100)
    if number > 99:
        speak_number_ones(hundred)
        print("hundred", end= ' ')
    speak_number_tens(number % 100)
        
def get_digit_set(digit):

    dig = int((digit - 1) // 3)
    if dig == 1:
        print("thousand", end=' ')
    elif dig == 2:
        print("million", end=' ')
    elif dig == 3:
        print("billion", end=' ')

    

def main_menu():

    # 0
    # 20000000
    # negitives
    # decimals
    # non number input #parsing input
    try:
        sys.argv[1]
    except IndexError:
        number = int(input('Enter your number: '))
    else:
        number = int(sys.argv[1])

    digit = len(str(number))

    while (digit > 0): 
        sl = (digit % 3)
        if (sl == 0):
            sl = 3
        set_place = (10 ** (digit - sl))
        speak_number_hundreds(number // set_place)
        get_digit_set(digit)
        number %= set_place
        digit -= sl

    print("")

    
if (__name__ == "__main__"):
    main_menu()


