from tkinter import *

root = Tk()

root.title("About TkRootMenu")

var = StringVar()

label = Label( root, textvariable=var, relief=RAISED )

var.set("TkRootMenu\nJust for fun adhoc python menu\ntsouchlarakis@gmail.com\n")

label.pack()

root.mainloop()
