#!/bin/bash
#Lucy S
#Version 1: Takes a one-digit number and echoes the word
#Version 2: Takes a one or two digit number and passes it to a function (speak_number_tens) which says the tens place (special for 10-19) and then sends the digit in the ones place through speak_number_ones.
#Version 3: Check for $1 in global, if exists, use it, else prompt for user input. Each function should use $1 as their input and pass other input to next function. new function speak_number_hundreds that (if number has a hundred) uses the speak_number_ones function on the hundreds place, echos "hundred" and then passes remaining 2 digits to speak_number_tens



function speak_number_ones  () {

    case $1 in
	1) echo -n "one " ;;
	2) echo -n "two " ;;
	3) echo -n "three " ;;
	4) echo -n "four " ;;
	5) echo -n "five " ;;
	6) echo -n "six " ;;
	7) echo -n "seven " ;;
	8) echo -n "eight " ;;
	9) echo -n "nine " ;;	
    esac
}

function speak_number_teens () {
    case $1 in
	10) echo -n "ten " ;;
	11) echo -n "eleven " ;;
	12) echo -n "twelve " ;;
	13) echo -n "thirteen " ;;
	14) echo -n "fourteen " ;;
	15) echo -n "fifteen " ;;
	16) echo -n "sixteen " ;;
	17) echo -n "seventeen " ;;
	18) echo -n "eighteen " ;;
	19) echo -n "nineteen " ;;
    esac
}

function speak_number_tens () {
    tens=`expr $1 / 10` 
    case $tens in
	1) speak_number_teens $1 ; return ;;
	2) echo -n "twenty " ;;
	3) echo -n "thirty " ;;
	4) echo -n "fourty " ;;
	5) echo -n "fifty " ;;
	6) echo -n "sixty " ;;
	7) echo -n "seventy " ;;
	8) echo -n "eighty " ;;
	9) echo -n "ninety " ;;
    esac
    speak_number_ones `expr $1 % 10` 
}

function speak_number_hundreds () {

    hundreds=`expr $1 / 100`
    if [ $1 -gt 99 ]
    then
	speak_number_ones $hundreds
	echo -n "hundred "
    fi
	#speak_number_tens expects a 2 digit, not 3 digit number. use % 100 (similar to line 52)
	speak_number_tens `expr $1 % 100`
}

function main () {
    echo "Welcome!"

    #why did you change this from an if else?
    if [ $# -gt 0 ]
    then
	speak_number_hundreds $1
    else
	read -p "Please type a number between 0 and 100: " answer
	speak_number_hundreds $answer
    fi
}

main $1
echo -e "\nThank you!"
