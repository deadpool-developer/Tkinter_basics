#photoImage function support png , gif format only -> support more search it on google
#Python Imaginary Library- -> pillow -> to support jpg format files
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("1255x944")

#do not support jpg
# photo = PhotoImage(file="img.png")

# For jpg Images
images = Image.open("img.jpg")
photo = ImageTk.PhotoImage(images)

a_label = Label(image=photo)
a_label.pack()

root.mainloop()