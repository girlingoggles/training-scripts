#!/usr/bin/env python3
#girlingoggles made this

#phase 3: add speak_number_hundreds that takes a 3 digit number and if it's more that 99, calls speak_number_ones on the hundreds place then prints hundred, then passes the last two digits to speak_number_tens

import sys


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
        #wrong imput to pass to speak_number_teens
        speak_number_teens(ten)
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

    #need to cast value of hundred as an int
    hundred=(number / 100)
    if number > 99:
        speak_number_ones(hundred)
        print("hundred", end= ' ')
    speak_number_tens(number % 100)
        
def main(input):

    try:
        sys.argv[1]
    except IndexError:
        number = int(input('Enter your number: '))
    else:
        number = int(sys.argv[1])
    speak_number_hundreds(number)
    print("")
    

main(input)
