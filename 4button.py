from Tkinter import *
import Tkinter
import sys
from sys import argv
import time

import tkMessageBox
top=Tkinter.Tk()
def helloCallBack1():
    tkMessageBox.showinfo("you pressed top butto","pressed FORWARD button ")
def helloCallBack2():
    tkMessageBox.showinfo("you pressed top butto","pressed LEFT button")
def helloCallBack3():
    tkMessageBox.showinfo("you pressed top butto","pressed RIGHT button")
def helloCallBack4():
    tkMessageBox.showinfo("you pressed top butto","pressed BACKWORD button")
    
A=Tkinter.Button(top,text="FORWARD",command=helloCallBack1,bg='green',activebackground='black')
A.config( height = 15, width = 75 ,padx=60)
A.pack(padx=1, pady=1,side=TOP)
A.grid(row=6,column=6)
A.pack()

B=Tkinter.Button(top,text="LEFT",command=helloCallBack2,bg='red')
B.config( height = 180, width = 30 ,padx=20)
B.pack(padx=5, pady=10, side=LEFT)
B.pack()

C=Tkinter.Button(top,text="RIGHT",command=helloCallBack3,bg='red')
C.config(height = 180, width = 30 ,padx=20)
C.pack(padx=5, pady=10, side=RIGHT)
C.pack()

D=Tkinter.Button(top,text="BACKYARD",command=helloCallBack4,bg='green')
D.config( height = 15, width = 35 ,padx=200)
D.pack(padx=5, pady=10,side=BOTTOM)
D.pack()
top.mainloop()
