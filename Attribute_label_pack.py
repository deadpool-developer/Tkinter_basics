from tkinter import *
root  = Tk()

root.geometry("444x233")
root.title("My GUI with harry")

# IMPORTANT LABEL OPTION 

    # text = adds the text
    # bg = background
    # fg = foreground
    # font = sets the font
    # padx = x _Padding
    # pady = y _Padding
    # relief = border styling = SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text=''' Abdul Rashid Salim Salman Khan (Hindi: [səlˈmɑːn xɑːn]; 27 December 1965)[2] is an Indian actor, 
\nfilm producer, and television personality who works in Hindi films.\n
 In a film career spanning over thirty years, Khan has received numerous awards, including\n
  two National Film Awards as a film producer, and two Filmfare Awards for acting.[3] He\n
   is cited in the media as one of the most commercially successful actors of Indian cinema.''', bg="red",foreground="white",padx=45, pady=95)

title_label.pack()



root.mainloop()