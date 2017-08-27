#!/usr/bin/python2.7

import os
from Tkinter import *

def runCommand(app):
  os.system(app + " &")

def runBrowser():
  app = "firefox"
  runCommand(app)
def runTerminal():
  app = "terminology"
  runCommand(app)
def runFileManager():
  app = "xfe"
  runCommand(app)
def runEditor():
  app = "atom"
  runCommand(app)

root = Tk()
root.title("Root Menu")

menubar=Menu(root)
appsmenu=Menu(menubar)

menubar.add_cascade(label="Root Menu", menu=appsmenu)

appsmenu.add_command(label="Terminal", command=runTerminal)
appsmenu.add_command(label="Editor", command=runEditor)
appsmenu.add_command(label="File Manager", command=runFileManager)
appsmenu.add_command(label="Browser", command=runBrowser)
appsmenu.add_separator()
appsmenu.add_command(label="Close Menu", command=root.quit)

root.config(menu=menubar)

root.mainloop()
