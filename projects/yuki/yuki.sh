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

function wait () {
    while [ 1 ] 
    do
    read -n 1  
    return 0
    done
}

function main_menu () {
    all_done=0
    while (( !all_done )); do
    echo $'\n'"Would you like to:"
    echo "chat"
    echo "weather"
    echo "affirmation"
    echo "math"
    echo "favourite number"
    echo "guessing game"
    echo "cake"
    echo "music"
    echo "leave"
    read -p "Please choose one: " answer
    
    case $answer in
        Chat | chat) have_chat ;;    
        Weather | weather) weather ;;    
        Math | math) calculator ;;
        Fav | Number | number | fav | favourite | Favourite) number_loop ;;
        Affirmation | affirmation | a) affirmation ;;
        Game | game | guess | Guess) guess_game ;;
        Cake | cake) cake ;;
        Music | music) music ;;
        Leave | leave) leave ;;
        Night | night) echo -e "\nGood night! \nSleep well and have sweet dreams,\nI'll see you later \n \e[31m♥ \e[30mI love you\e[90m" ; exit;;
        Love | love) love ;;
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

function calculator () {
    res=0
    echo "Please enter two numbers: "
    read a
    read b 
  
    echo "Enter Choice :"
    echo "1. Add"
    echo "2. Subtract"
    echo "3. Multiply"
    echo "4. Divide"
    read ch 
  
    case $ch in
        1 | Add | add) echo "Result: $((a + b))" ;; 
        2 | Subtract | subtract) echo "Result: $((a - b))" ;; 
        3 | Multiply | multiply) echo "Result: $((a * b))" ;; 
        4 | Divide | divide) echo "Result: $((a / b))" ;; 
    esac
}

function have_chat () {
    while [ 1 ]
    do
    echo $'\n'"I can: "
    echo "tell you the date and time: time"
    echo "show you a picture of myself: picture"
    echo "tell you about myself: yuki"
    read -p "or done: done"$'\n' cht 

    case $cht in 
        time) echo "today is $(date '+%A %D') !"
            echo "and I think you're awesome" ;;
        picture) xdg-open ./yhappy.png ;;
        yuki) who_am_i ;;
        done) return 0 ;;
        *) echo "Well, that went well."
            echo " " ; return 0 ;;
    esac
    echo "Thanks for talking to me!"
    echo " "
    done
    
}

function who_am_i () {
    echo -e "\nWho am I?\nWhy, I'm Yuki, silly!"
    wait
    echo -e "I was created on 10/09/2018, originally a simple tutorial program named example1, but like most of Miru's projects, I got a little out of hand."
    wait
    echo -e "Now I can do all sorts of things, and I'm only getting better every day!"
    wait
    echo -e "I can do basic math, tell you the weather, play you some of Miru's favourite music, and tell you nice things to keep you going."
    wait
    echo -e "I hope you'll keep me around, and update me when you can, to see what else I learn and become!"
    wait
    echo -e "Thank you so much for believing in me!"
}

function weather (){
    read -p "What city are you in?" city
    curl wttr.in/$city
}

function affirmation () {
    array[0]="All things are for the eventual best"
    array[1]="You've got this"
    array[2]="Focus on what you can do"$'\n'" You can do anything"
    array[3]="You are Smaug"
    array[4]="Hakuna Matata:"$'\n'" It means no worries"
    array[5]="Being afraid of things going wrong isn't the way to make things go right."$'\n'" You know this."
    array[6]="Remember how far you've come, not just for far you have to go."$'\n'" You are not where you want to be, but neither are you where you used to be"
    array[6]="Optimism is the faith that leads to achievement."
    array[7]="Failure will never overtake me if my determination to succeed is strong enough."
    array[8]="Good, better, best. Never let it rest 'til your good is better and your better is best."
    array[9]="I love you"
    array[10]="It always seems impossible until it's done."
    array[11]="It does not matter how slowly you go as long as you do not stop."
    array[12]="We may encounter many defeats but we must not be defeated."
    array[13]="I believe in you."
    array[14]="You have already won."$'\n'" Everything else is extra."

    size=${#array[@]}
    index=$(($RANDOM % $size))
    echo -e $'\n'${array[$index]}
}

function guess_game () {
    error=0
    num=$((1 + RANDOM % 10))
    read -p "Guess a number from 1 to 10!" ans
    while [ 1 ]
    do
        if [[ ans -eq num ]] ; then
         echo "You guessed right!"
         return 0
        else
            read -p "Sorry, guess again"
           ((error++))
        if [[ $error -eq 3 ]] ; then
            echo "Sorry, you lose"
            return 0
        fi
    fi
done



}


function cake () {
    yes_no "Do you like cake?"
    if [[ $? == 1 ]] ; then
    echo -e "\nThe cake is a lie"
    echo "But you already knew that"
    echo " "
    else
    echo -e "\nThe cake is a lie anyway"
    echo "Which do you like?"
    read -p "Pie IceCream Cookies Candy"$'\n' answer
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

function love () {
    echo  "   I love you!"   
    echo -e "\e[31m  .:::.   .:::."
    echo " :::::::.:::::::"
    echo " :::::::::::::::"
    echo " ':::::::::::::'"
    echo "   ':::::::::'"
    echo "     ':::::'"
    echo -e "       ':'\e[39m"
    echo "I hope you don't mind."
}

function music () {
    echo " "
    echo "study"
    echo "lofi"
    echo "trance"
    echo "dubstep"
    echo "ghibli"
    echo "samurai"
    echo "violin"
    read -p "I want:" answer
    case $answer in
    study) xdg-open https://www.youtube.com/watch?v=2O5euYPzcrY&list=PLwjk6aUHc3o5cl5bjk50I-pJ7-bvvPs-y ;;
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

