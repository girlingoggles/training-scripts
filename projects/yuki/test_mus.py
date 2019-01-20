#!/usr/bin/env python3

def yes_no(question):
    yes = set(['yes', 'y', 'ye', 'yea', 'yeah', 'yep', 'yup', 'ya', ' '])
    no = set(['no', 'nope', 'n', 'nah', 'na', 'neh'])
    
    while True:
        yn = input(question + " ")
        yn = yn.lower()
        if yn in yes:
            return True
        elif yn in no:
            return False
        else:
            print("\nyes or no only, please.\n")


def music(act):
        mus = {"lofi": "https://www.youtube.com/watch?v=dJhW1J6gIWA", "trance": "https://www.youtube.com/watch?v=buqNTkjTY20", "dubstep": "https://www.youtube.com/watch?v=a41icW_FtsI", "ghibli": "https://www.youtube.com/watch?v=YjohMzHkBqI", "samurai": "https://www.youtube.com/watch?v=jrTMMG0zJyI", "violin": "https://www.youtube.com/watch?v=jvipPYFebWc&start_radio=1&list=RD\EMzT1XwmFnIup_KYXuc2rUZA","chill": "https://www.youtube.com/watch?v=G2WneYqu-ao","glitch": "https://www.youtube.com/watch?v=52Qug_siqKw"}
        print(act)
        words = act.split()
        title = ""
        print("first word is " + words[0])
        for word in words[:]:
            print("testing for " + word)
            if word in mus:
                title = word
                print("Found " + word + " in music")

        if title == "":
            print("these are the things i can play: " + str(mus.keys()))
            song = input("which of these would you like? If none, I can add your favourite. ")
            song = song.lower()
            if song in mus:
                title = song
            else:
                cont = True
                while cont:
                    if song == "" or song == "none":
                        song = input("What would you like me to add?")
                    song = song.lower()
                    if yes_no("so you want to add a new song to the lable:" + song + ": right?"):
                        new_link = input("Can you give me the link as well please?")                            
                        if yes_no("so the new song :" + song + ": should open the link " + new_link + " is this correct?"):
                            mus[song] = new_link
                            title = song
                            cont = False
                        else:
                            print("Let's try that again")
                    song = ""

            
        print(title + "'s link is " + mus[title])
#        webbrowser.open(mus[title])

act = input("hi: ")
act = act.lower()
music(act)

