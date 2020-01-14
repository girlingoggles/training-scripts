#!/usr/bin/env python3
#GiG

import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk


class App:
	def __init__(self, window, window_tite, video_source=0):
		self.window = window
		window_title = "test"
		self.window.title(window_title)
		self.video_source = video_source
		self.vid = MyVideoCapture()
		self.canvas = tk.Canvas(window, width = self.vid.width, height = self.vid.height)
		self.canvas.pack()
		self.delay = 15
		self.update()

		self.window.mainloop()

	def update(self):
		ret, frame = self.vid.get_frame()
		if ret:
			self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
			self.canvas.create_image(0,0, image = self.photo, anchor = tk.NW)
		self.window.after(self.delay, self.update)

class MyVideoCapture:
    def __init__(self):
        # Open the video source
        self.vid = cv2.VideoCapture(2)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
  
          # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
 
    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
        self.window.mainloop()

    def get_frame(self):
    	if self.vid.isOpened():
    		ret, frame = self.vid.read()
    		if ret:
    			return(ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    		else:
    			return(ret, None)
    	else:
    		return(ret, None)

App(tk.Tk(), "tkinter and opencv")