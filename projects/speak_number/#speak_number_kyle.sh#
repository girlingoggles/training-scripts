#!/bin/bash
# By Kyle A. King (kyconquers@gmail.com)

#TODO:
# 1: add alternitive (backup) input
# 2: expand digits set
# 3: parse input

print_numbers_ones () {

    case $1 in
	1) echo -n "one" ;;
	2) echo -n "two" ;;
	3) echo -n "three" ;;
	4) echo -n "four" ;;
	5) echo -n "five" ;;
	6) echo -n "six" ;;
	7) echo -n "seven" ;;
	8) echo -n "eight" ;;
	9) echo -n "nine" ;;
    esac
}

print_numbers_teens () {

    case $1 in
	10) echo -n "ten" ;;
	11) echo -n "eleven" ;;
	12) echo -n "twelve" ;;
	13) echo -n "thirteen" ;;
	14) echo -n "fourteen" ;;
	15) echo -n "fifteen" ;;
	16) echo -n "sixteen" ;;
	17) echo -n "seventeen" ;;
	18) echo -n "eighteen" ;;
	19) echo -n "ninteen" ;;
    esac
}

print_numbers_tens () {

    tens=`expr $1 / 10`
    case $tens in
	1)
	    print_numbers_teens $1;
	    return
	    ;;
	2) echo -n "twenty" ;;
	3) echo -n "thirty" ;;
	4) echo -n "fourty" ;;
	5) echo -n "fifty" ;;
	6) echo -n "sixy" ;;
	7) echo -n "seventy" ;;
	8) echo -n "eighty" ;;
	9) echo -n "ninety" ;;
    esac
    
    if [ $tens -ne 0 ]
    then
	echo -n ' '
    fi
    
    print_numbers_ones `expr $1 % 10`
}

print_numbers_hundreds () {

    declare -i number
    number=$1

    if [ $number -gt 99 ]
    then
	print_numbers_ones `expr $number / 100 % 10`
	echo -n ' hundred '
	number=number%100
    fi

    print_numbers_tens $number
}

print_numbers_digit_set () {

    echo -n ' '
    case $1 in
	1) echo -n "thousand" ;;
	2) echo -n "million" ;;
	3) echo -n "billion" ;;
	4) echo -n "trilion" ;;
    esac
    echo -n ' '
}

print_numbers () {

    declare -i number
    declare -i digits
    number=$1
    digits=${#number}
    
    if [ `expr $digits % 3` -gt  0 ]
    then
	echo uneven first set
	digits_in_set=$(($digits % 3))
	hold=$((10**($digits - $digits_in_set)))

	print_numbers_hundreds `expr $number / $hold`
	print_numbers_digit_set `expr $digits / 3`

	number=$(($number % (10**($digits-$digits_in_set))))
	digits=${#number}
    fi
    
    while [ `expr $digits / 3` -gt  0 ]
    do
	hold=$((10**($digits - 3)))
	print_numbers_hundreds `expr $number / $hold`
	print_numbers_digit_set $((($digits - 3 ) / 3))
	
	if [ $digits -gt 0 ]
	then
	    number=$(($number % (10**($digits-3))))
	fi
	digits=$(($digits - 3))
    done
    echo ''
}

print_numbers $1
echo done
