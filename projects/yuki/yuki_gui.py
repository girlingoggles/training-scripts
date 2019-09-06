#!/usr/bin/env python3
#tutorial/trial gui for yuki

from tkinter import *
from PIL import Image, ImageTk
import yuki_ai

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("YUKI ♥")
    
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        self.showImg()
        self.yuki()
        #        self.showText()

        
    def showImg(self):
        load = Image.open("yhappy.png")
        render = ImageTk.PhotoImage(load)
        
        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        
        
#    def showText(self):
#        text = Label(self, text="Hey there good lookin!")
#        text.pack()

    def yuki(self):
        yuki_ai.main_menu()
            
            
root = Tk()
        
root.geometry("500x500")

app = Window(root)
root.mainloop()
