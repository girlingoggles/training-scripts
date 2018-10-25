#!/usr/bin/env python3
#girlingoggles made this

#phase 3: add speak_number_hundreds that takes a 3 digit number and if it's more that 99, calls speak_number_ones on the hundreds place then prints hundred, then passes the last two digits to speak_number_tens

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
        
# you only need one of these functions. whichever name you chose
def get_digit_set(digit):
#    dig = set_place
    digit = int(digit)
    if (int(digit) > 3):
        dig = (int(digit) // 3)
        global number

        speak_number_hundreds(us)
        if dig == 1:
            print("thousand", end=' ')
        elif dig == 2:
            print("million", end=' ')
        elif dig == 3:
            print("billion", end=' ')

    

def main_menu():

    # I put extra hints in hints.txt
    # 4 steps in main_menu
    # step 1: parse input
    global number
    try:
        sys.argv[1]
    except IndexError:
        number = int(input('Enter your number: '))
    else:
        number = int(sys.argv[1])


    # step 2:
    # A: declare and init digits variable
    digit = len(str(abs(number)))
    digit = str(digit)
    # B: delcare "uneven_set" variable
    # C: if (uneven_set > 0):
    global us
    us = (int(digit) % 3)
    if (int(digit) < 3):
        number = int(number)
        speak_number_hundreds(us)
    # deal with uneven set like you would in loop
    
    # step 3: for each even set

    # python does for loops stupidly (they try and make it too simple) use a while loop instead
    # A: while digits > 0:
#    while digit > 2:
 #       speak_number_hundreds(bit)
    # B: declare and init set_place var
    # C: call speak_number_hundreds
    # D: call get_digit_set
    # E: update number and digits 
    while (digit > "2"):
        dig = (int(digit) // 3)
        bit = str(number)[-3:]
        bit = int(bit)
#        set_place = int(int(digit) / 3)
      #  speak_number_hundreds(uneven_set)
        get_digit_set(int(digit))
        speak_number_hundreds(bit)
        s_n = 0
        digit = str(digit)
        digit = str(number)[:-3]
#        digit = int(digit)
        
        #    speak_number_hundreds(number)

    # step 4: end: print newline and return (don't return in this version)
    print("")

    
if (__name__ == "__main__"):
    main_menu()


