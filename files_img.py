from logging import root
from tkinter import *
from PIL import Image,ImageTk
import os

root = Tk()
root.title("Photo Album")
root.geometry("1250x988")

reference = []
for (root_,dirs,files) in os.walk("imgages"):
    if files:
        for file_ in files:
            path = os.path.join("imgages",file_)
            image_ = Image.open(path)
            n_image = image_.resize((400,400))
            photo = ImageTk.PhotoImage(n_image)
            img_label = Label(root,image=photo)
            img_label.pack()
            reference.append(photo)

root.mainloop()