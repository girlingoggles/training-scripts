#!/usr/bin/python3
#GiG

import tkinter as tk
#import cv2

result = "0"


def add():
	global result
	global t3
	t3.delete(1.0, tk.END)
	a = float(t1.get())
	b = float(t2.get())
	result = a + b
	t3.insert(tk.END, result)
def mult():
	global result
	global t3
	t3.delete(1.0, tk.END)
	a = float(t1.get())
	b = float(t2.get())
	result = a*b
	t3.insert(tk.END, result)
def sub():
	global result
	global t3
	t3.delete(1.0, tk.END)
	a = float(t1.get())
	b = float(t2.get())
	result = a-b
	t3.insert(tk.END, result)
def div():
	global result
	global t3
	t3.delete(1.0, tk.END)
	a = float(t1.get())
	b = float(t2.get())
	if (b==0):
		result = "cannot divide by zero"
	else:
		result = a/b
	t3.insert(tk.END, result)

root = tk.Tk()
root.title("Calculator")
tk.Label(root, text="Input1").grid(row=0)
tk.Label(root, text="Input2").grid(row=1)
tk.Label(root, text="Result").grid(row=2)
t1 = tk.Entry(root, width=20)
t2 = tk.Entry(root, width=20)
t3 = tk.Text(root, height=1, width=20)
t1.grid(row=0, column=1)
t2.grid(row=1, column=1)
t3.grid(row=2, column=1)
t3.insert(tk.END, result)

tk.Button(root, text="Add", command=add).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(root, text="Mulitply", command=mult).grid(row=3, column=1, sticky=tk.W, pady=4)
tk.Button(root, text="Subtract", command=sub).grid(row=4, column=0, sticky=tk.W, pady=4)
tk.Button(root, text="Divide", command=div).grid(row=4, column=1, sticky=tk.W, pady=4)
tk.Button(root, text="Exit", command=root.quit).grid(row=4, column=2, sticky=tk.W, pady=4)

root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=1)
root.grid_rowconfigure(3,weight=1)
root.grid_rowconfigure(4,weight=1)

tk.mainloop()
