from cProfile import label
from cgitb import text
from tkinter import *

root = Tk()

#width x height -> geometry paramter 
root.geometry("644x434")   #size of the GUI

#width,height
root.minsize(200,100)   #minimum size of the GUI

#width,height
root.maxsize(1200,988)   #maximum size of the GUI

#label  -> visiblw on the screen of the GUI
a = Label(text="Aditya's GUI, let's get started")
a.pack()  #we have to pack the label in the pack method else it won't be visible

root.mainloop()

#733x434