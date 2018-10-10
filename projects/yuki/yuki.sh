#!/usr/bin/env bash
#This is Yuki. She's here to help.
#Please be patient, she's learning.

#You should add a yes_or_no funtion.
#funtion yes_or_no should accept a string question, and prompt that string with read -p then return 1 for all forms of yes (y,ya,yep,yes) or 0 for all forms of no (n, no, nah)


function yes_no () {
    all_done=0
    while (( !all_done)); do
    echo -n $@
    read yn
    case $yn in
            y | Y | yes | Yes | Yea | yea | Yeah | yeah | yep | Yep | yup | Yup | ya | Ya) return 1 ;; 
            n | N | no | No | nah | Nah | nope | Nope | Na | na) return 0 ;;
    esac
    
    echo "yes or no only, please"
    done
}

function main_menu () {
    all_done=0
    while (( !all_done )); do
    echo "Would you like to:"
    echo "chat"
    echo "affirmation"
    echo "math"
    echo "cake"
    echo "music"
    echo "leave"
    read -p "Please choose one:" answer
    
    case $answer in
        Chat | chat) have_chat ;;        
        Math | math) number_loop ;;
        Affirmation | affirmation) affirmation ;;
        Cake | cake) cake ;;
        Music | music) music ;;
        Leave | leave) leave ;;
        *) echo "try again" ;;
    esac
    done
    
}

function number_loop () {
    errors=0
    error_answer="Please return to your class. I hear you're learning how to count today!"
    while [ 1 ]
    do
    read -p "What is your favourite number between 0 and 10?" answer
    case $answer in
        1) echo "Because you're the best!" ; return 0 ;;
        2|4|6|8) echo "Even Steven?" ; return 0 ;;
        3|9) echo "You're an odd one, aren't you?" ; return 0 ;;
        5) echo "Right in the middle, best of both!" ; return 0 ;;
        0|10) echo "Of course YOU would choose such a fancy number" ; return 0 ;;
        7) echo "Feeling lucky, huh?" ; return 0 ;;
            *) echo $error_answer ; ((errors++)) ;;
    esac
    if [ $errors -eq 3 ]
    then error_answer="Are you even trying?" ;
    fi
       if [ $errors -eq 4 ]
    then error_answer="For the love of... Stop fucking with me, yea?" ;
    fi
    if [ $errors -eq 6 ]
    then error_answer="This is annoying now. Stop it." ;
    fi
    echo " "
    done
}

function have_chat () {
    yes_no "Do you want to know something?"
    if [[ $? == 1 ]] ; then
    echo "today is $(date '+%A %D') !"
    echo "and I think you're awesome"
    echo "Thanks for talking to me!"
    echo " "
    else echo "Well, that went well."
     echo " "
    fi
}

function affirmation () {
    echo "All things are for the eventual best"
    read -n 1 -srp " "
    echo "You've got this"
    read -n 1 -srp " "
    echo "Focus on what you can do"
    echo " You can do anything"
    read -n 1 -srp " "
    echo "You are Smaug"
    read -n 1 -srp " "
    echo "Hakuna Matata"
    echo " It means no worries"
    read -n 1 -srp " "
    echo "Being afraid of things going wrong isn't the way to make things go right"
    echo " You know this"
    read -n 1 -srp " "
    echo "Remember how far you've come, not just how far you have to go. \n You are not where you want to be, but neither are you where you used to \
be"
    echo " "
}

function cake () {
    yes_no "Do you like cake?"
    if [[ $? == 1 ]] ; then
    echo "The cake is a lie"
    echo "But you already knew that"
    echo " "
    else
    echo "The cake is a lie anyway"
    echo "Which do you like?"
    read -p "Pie IceCream Cookies Candy" answer
    case $answer in
        Pie | pie)
        echo "Pie  is a fantastic choice!" ;;
        Ice | Cream | ice | cream | IceCream | icecream)
        echo "IceCream is so cold!" ;;
        Cookies | cookies)
        echo "Anzac, chocolate chip, coconut... There are so many!" ;;
        Candy | candy)
        echo "Too many varieties of sweets to list, too many to try!" ;;
        *)
        answer=False
        echo "Is that a dessert?"  ;;
    esac
    # it says this even if it triggers "Is that a dessert?" Also, should be quoted.
    if [[ $answer == False ]] ; then
        echo "I'll have to look into this"
        echo " "
    else
        echo "I like $answer too!"
        echo " "
    fi
    fi
}

function music () {
    echo "lofi"
    echo "trance"
    echo "dubstep"
    echo "ghibli"
    echo "samurai"
    echo "violin"
    read -p "I want:" answer
    case $answer in
    lofi) xdg-open https://www.youtube.com/watch?v=dJhW1J6gIWA&t=766s ;;
    trance) xdg-open https://www.youtube.com/watch?v=buqNTkjTY20 ;;
    dubstep) xdg-open https://www.youtube.com/watch?v=a41icW_FtsI ;;
        ghibli) xdg-open https://www.youtube.com/watch?v=YjohMzHkBqI ;;
    samurai) xdg-open https://www.youtube.com/watch?v=jrTMMG0zJyI ;;
    violin) xdg-open https://www.youtube.com/watch?v=jvipPYFebWc&start_radio=1&list=RDEMzT1XwmFnIup_KYXuc2rUZA
    esac
    echo "Enjoy!"
    echo " "
}

function leave () {
    echo "It will be lonely without you here."
    echo "but if you must..."
    yes_no "Must you?"
    if [[ $? == 1 ]] ; then
    echo "Goodbye then. I'm glad you stopped by."
    exit
    else echo "I'm glad you can stay with me for a little longer."
     echo "what would you like to do now?"
     echo " "
    fi
}



echo "Hello"
echo "My name is Yuki. I'm here to help"
read -p "what's your name?" varname
echo "it's nice to meet you $varname"
main_menu

