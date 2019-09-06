#!/usr/bin/env bash
#This is Yuki. She's here to help.
#Please be patient, she's learning.
#Made by GirlInGoggles


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
    echo "Hi! My name is Yuki. I'm here to help"
    get_user
    run=1
    while ((run)); do
	read -p " " answer
	$answer | tr [: lower]
	hi=(
