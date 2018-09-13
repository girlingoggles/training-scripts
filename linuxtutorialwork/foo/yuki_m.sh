#!/usr/bin/env bash
# ^-- More appropriate shebang

# Renamed all variables with descriptive names throughout script
hello = "Hello"
goodbye = "Goodbye"
see_you_soon = "See you soon!"

echo "$hello"
echo "What's your name?"
read name
# You're inconsistent between the `echo/read` pattern and the `read -p` pattern.
# I don't know enough about bash to know if there's a meaningful difference, I've never used `read` before.
echo "It's nice to meet you, $name."
read -p "Are you leaving me? [y/n]" is_leaving
# Fixed indentation throughout
if [[ $is_leaving == "y" ]] ; then
    echo "$goodbye"
    exit
fi
read -p "Do you like cake? [y/n]" likes_cake
if [[ $likes_cake == "y" ]] ; then
    echo "The cake is a lie."
    echo "$goodbye"
    exit
else
    echo "The cake is a lie anyway."
    echo "Which dessert do you like?"
    read dessert
    echo "I like $dessert too!"
    read -p "Do you want to know something? [y/n]" wants_to_know
    if [[ $wants_to_know == "y" ]] ; then
	echo "Today is $(date '+%A %D')!"
    else
	echo "I'm glad you stayed."
	read -p "you should really go though. [y/n]" wants_to_go
	if [[ $wants_to_go == "y" ]] ; then # Used double square brackets
	    echo "$see_you_soon"
	else
	    echo "I promise I'll see you again. Bye!"
	    # Removed extraneous 'exit'
	fi
    fi
fi
