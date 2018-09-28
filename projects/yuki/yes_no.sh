#!/bin/bash

function yes_no () {

    all_done=0
    while (( !all_done )); do
	
	echo $@

	read yn
	case $yn in
	    y | Y | yes | Yes | Yea | yea | Yeah | yeah | yep | Yep | yup | Yup | ya | Ya) return 1 ;; 
	    n | N | no | No | nah | Nah | nope | Nope | Na | na) return 0 ;;
	esac
	
	echo "Not a valid response. Try again."
    done
}

yes_no "Does this work"
if [ $? == 1 ] ; then
    echo "It works."
else
    echo "Id doesn't work"
fi

