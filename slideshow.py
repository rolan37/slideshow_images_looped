# import required modules 
import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk

# adjust window
root=tk.Tk()
# adjust the size as per your requirements
root.geometry("5760x1080")    

# loading the images  ---> if there are many images. It is recommended to use a loop with generic filename.
img1=ImageTk.PhotoImage(Image.open("1.jpg"))
img2=ImageTk.PhotoImage(Image.open("2.jpg"))
img3=ImageTk.PhotoImage(Image.open("3.jpg"))

def read_image():
  for i in range


l=Label()
l.pack()

# using recursion to slide to next image
x = 1

# function to change to next image
def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		l.config(image=img1)
	elif x == 2:
		l.config(image=img2)
	elif x == 3:
		l.config(image=img3)
	x = x+1
	root.after(4000, move)

# calling the function
move()



root.mainloop()
