#!/bin/bash
#Lucy S
#Version 1: Takes a one-digit number and echoes the word
#Version 2: Takes a one or two digit number and passes it to a function (speak_number_tens) which says the tens place (special for 10-19) and then sends the digit in the ones place through speak_number_ones.



function speak_number_ones  () {
# you should not be reading the answer outside of the main section
    read answer
    #the case in speak_number_one should assume it has been given a 1 digit not 2 digit number
    case ${answer:1} in
	?1) echo "one" ;;
	?2) echo "two" ;;
	?3) echo "three" ;;
	?4) echo "four" ;;
	?5) echo "five" ;;
	?6) echo "six" ;;
	    ?7) echo "seven" ;;
	    ?8) echo "eight" ;;
	    ?9) echo "nine" ;;	
	    ?0) echo "zero" ;;
	    *) echo "That is not a two-digit number. Please try again." ; return ;;
    esac
}
function speak_number_tens () {
    #reads should one be in the main section
    read -p "please type a number between 0 and 100" answer
    
    echo ${answer:0:1}
    case $answer in
	# 1? should be a special case. there is no such thing as "ten one", "ten two"
	1?) echo "ten " ;;
	2?) echo "twenty " ;;
	3?) echo "thirty " ;;
	4?) echo "fourty" ;;
	5?) echo "fifty" ;;
	6?) echo "sixty" ;;
	7?) echo "seventy" ;;
	8?) echo "eighty" ;;
	9?) echo "ninety" ;;
    esac
    #you should be passing the second digit to speak_number_ones, this passes nothing to it.
    speak_number_ones 
    return
}

#main section
echo "Welcome!"
#should not be a while loop.
while [ 1 ]
do
    #should do read here and then pass input to speak_number_tens
    speak_number_tens
echo "Thank you!"
done
#exit at the end of the function is redundent
exit
