#!/usr/bin/env python3
#girlingoggles


from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.filedialog import askopenfilenameuur



class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)  
        self.master = master
        self.init_window()
    
    def  init_window(self):
        self.master.title("TRIAL")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        edit = Menu(menu)
        edit.add_command(label="Undo")
        edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)
        menu.add_cascade(label="Edit", menu=edit)
        showYuki()
        
        
        #quitButton = Button(self, text="Quit",command=self.client_exit)
        #quitButton.place(x=20, y=20)
        
        def showYuki(self):
       # load = Image.open("yhappy.jpg")
    #    render = ImageTk.PhotoImage(load)
     #   img = Label(self, image=render)
      #  img.image=render
       # img.place(x=0,y=0)


    def showImg():
        load = Image.open("yhappy.png")
        render = ImageTk.PhotoImage(load)
        img = Label(image=render)
        img.image=render
        img.pack()
        img.place(x=0,y=0)

        path=askopenfilename(filetypes=[("Image File",'.jpg')])
        im = Image.open(path)
        tkimage = ImageTk.PhotoImage(im)
        myvar=Label(self,image = tkimage)
        myvar.image = tkimage
        myvar.place(x=0,y=0)
        
    def showText(self):
        text=Label(self, text = "Heya!")
        text.pack()
        
        
    def client_exit(self):
        exit()
        
        
root = Tk()
width  = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry('%sx%s' % (int(width/3), int(height/4)))
app = Window(root)
root.mainloop()