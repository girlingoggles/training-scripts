#!/usr/bin/env python3
#girlingoggles made this

import sys


#All of these funtions should have a parameter in their () it can be called number or anything you want.

def speak_number_ones():
    #use ifs, elif, and else for the number and print the human readable name for the number (one through nine)
    #use print("Hello World!", end = '') to print without newlines.
    print("Testing", end = '') #remove this when function is no longer blank
    
def speak_number_teens():
    #use ifs, elif, and else for the number and print the human readable name for the number (ten through nineteen)
    #use print("Hello World!", end = '') to print without newlines.
    print("Testing", end = '') #remove this when function is no longer blank

def speak_number_tens():
    # use ifs, elif, and else for the number and print the human readable name for the tens digit in number ( twenty, thirty, forty, ect)
    # print nothing if less than 10, and send to speak_number_teens if between 10 and 19 and return
    # send ones digit (number % 10) to speak_number_ones
    #use print("Hello World!", end = '') to print without newlines.
    print("Testing", end = '') #remove this when function is no longer blank

def main(number):
    #call speak_number_tens passing it the number parameter
    print("Testing", end = '') #remove this when function is no longer blank

try:
    sys.argv[1]
except IndexError:
    number = int(input('Enter your number: '))
else:
    number = int(sys.argv[1])
main(number)
