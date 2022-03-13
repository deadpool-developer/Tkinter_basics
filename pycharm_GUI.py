from cProfile import label
from cgitb import text
import tkinter


#geometry 
#minsize
#maxsize
#pack
#label

from tkinter import *

root = Tk()

root.geometry("733x434")
root.minsize(733,434)
a = Label(text="PyCharm Community Edition")
a.pack()

root.mainloop()