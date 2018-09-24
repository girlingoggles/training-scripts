#!/bin/bash
#Lucy S
#Version 1: Takes a one-digit number and echoes the word
#Version 2: Takes a one or two digit number and passes it to a function (speak_number_tens) which says the tens place (special for 10-19) and then sends the digit in the ones place through speak_number_ones.



function speak_number_ones  () {
# you should not be reading the answer outside of the main section
    #the case in speak_number_one should assume it has been given a 1 digit not 2 digit number
    case $answer in
	*1) echo "one" ;;
	*2) echo "two" ;;
	*3) echo "three" ;;
	*4) echo "four" ;;
	*5) echo "five" ;;
	*6) echo "six" ;;
	*7) echo "seven" ;;
	*8) echo "eight" ;;
	*9) echo "nine" ;;	
    esac
}

function speak_number_teens () {
    case $answer in
	10) echo -ne "ten \n" ;;
	11) echo -ne "eleven \n" ;;
	12) echo -ne "twelve \n" ;;
	13) echo -ne "thirteen \n" ;;
	14) echo -ne "fourteen \n" ;;
	15) echo -ne "fifteen \n" ;;
	16) echo -ne "sixteen \n" ;;
	17) echo -ne "seventeen \n" ;;
	18) echo -ne "eighteen \n" ;;
	19) echo -ne "nineteen \n" ;;
    esac
}

function speak_number_tens () {
tens='expr $answer / 10' 
    case $answer in
	1?) speak_number_teens ; return ;;
	2?) echo -n "twenty " ;;
	3?) echo -n "thirty " ;;
	4?) echo -n "fourty " ;;
	5?) echo -n "fifty " ;;
	6?) echo -n "sixty " ;;
	7?) echo -n "seventy " ;;
	8?) echo -n "eighty " ;;
	9?) echo -n "ninety " ;;
    esac
    speak_number_ones
    return
}

function main () {
echo "Welcome!"
     read -p $'please type a number between 0 and 100 \n' answer
    #should do read here and then pass input to speak_number_tens
    speak_number_tens
echo "Thank you!"
}

main
#exit at the end of the function is redundent
