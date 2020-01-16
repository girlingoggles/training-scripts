#!/usr/bin/env python3

import matplotlib, sys
matplotlib.use('TkAgg')
import numpy as np 
from numpy import arange
from math import pi
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter.filedialog import askopenfilename
from lmfit.models import LinearModel, LorentzianModel


file = None
#df1 = pd.read_csv("Lorentz.txt", sep="	+", engine='python')
df = None
amp1=1.0
wid1=1.0
cen1=1.0
x=None
y=None
x1 = None
updated=""
fitx= x
fity= y


def load():
	global file
	global df
	global x, fitx
	global y, fity
	global x1
	file = askopenfilename()
	df = pd.read_csv(file, sep="	+", engine='python')
	x = df['X']
	y = df['Y']
	x1 = np.array(df['X'])
	fitx = np.array(df['X'])
	fitx.ravel()
	fity = np.array(df['Y'])
	fity.ravel()


def refresh():
	b.clear()
	b.plot(x1,y)
	#a.plot(x1,s)
	dataPlot.draw()
	
def update():
	global amp1
	global wid1
	global cen1
	global updated
	global x1, s, y
	if t1.get():
		amp1 = float(t1.get())
	if t2.get():
		wid1 = float(t2.get())
	if t3.get():
		cen1 = float(t3.get())
	a.clear()
	a.plot(x1,s)
	b.plot(x1,y)

	dataPlot.draw()
	updated=tk.StringVar()
	updated.set("Updated: A=" + str(amp1) + " G=" + str(wid1) + " M=" + str(cen1))
	tk.Label(root, textvariable=updated).grid(row=4, column = 1, sticky=tk.W)
	

def fit():
	global fitx
	global fity
	fitx =fitx
	fity =fity
	a.clear
	mod = LorentzianModel()
	pars = mod.guess(fity,x=fitx)
	out = mod.fit(fity,pars, x=fitx)
	a.plot(fitx, fity)
	dataPlot.draw()

root = tk.Tk()
root.title("Hello Graph!")
load()

tk.Label(root, text="A").grid(row=0, column = 0, sticky=tk.N)
tk.Label(root, text="G").grid(row=0, column = 1, sticky=tk.N)
tk.Label(root, text="M").grid(row=0, column = 2, sticky=tk.N)
t1 = tk.Entry(root, width=20)
t2 = tk.Entry(root, width=20)
t3 = tk.Entry(root, width=20)
t1.grid(row=1, column=0, sticky=tk.N)
t2.grid(row=1, column=1, sticky=tk.N)
t3.grid(row=1, column=2, sticky=tk.N)


tk.Button(root, text="Update", command=update).grid(row=4, column=0, sticky=tk.W, pady=4)
tk.Button(root, text="Fit", command=fit).grid(row=4, column=0, sticky=tk.E, pady=4)
#tk.Label(root, text=updated).grid(row=4, column = 1, sticky=tk.W)
tk.Button(root, text="Load", command=load).grid(row=5, column=0, sticky=tk.W, pady=4)
tk.Button(root, text="Refresh", command=refresh).grid(row=5, column=1, sticky=tk.W, pady=4)
tk.Button(root, text="Exit", command=root.quit).grid(row=5, column=2, sticky=tk.W, pady=4)



f = plt.figure(figsize=(5,4), dpi=100)
plt.ion()
a = f.add_subplot(111)
b = f.add_subplot(111)
#a = plt.subplot(111)
#b = plt.subplot(111)
start = np.array(df['X'].iloc[0])
end = np.array(df['X'].iloc[-1])
t = arange(start,end)
u = df['Y']
#s = amp1 * wid1**2 / ( wid1**2 + ( x - cen1 )**2)
s = amp1*((wid1/(2*pi)) /((x1-cen1)**2+((wid1/2)**2)))
a.plot(x1,s)
b.plot(x1,y)
#plt.plot(x1, s)

#a.plot(t,u)


dataPlot = FigureCanvasTkAgg(f, master=root)
dataPlot.draw()
plot_widget = dataPlot.get_tk_widget().grid(row=2, column = 0, sticky=tk.W)
#dataPlot.get_tk_widget().grid(row=2, column=0, sticky=tk.W)

root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=1)

root.mainloop()