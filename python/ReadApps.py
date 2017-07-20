#!/bin/env python2
# A custom menu (tsouchlarakis@gmail.com)
# GNU/GPL https://www.gnu.org/licenses/gpl.html

import os
import sys
#from Tkinter import Tk, Label, Button, Scale, Menu, HORIZONTAL, TRUE
import subprocess
print os.name

def runCommand(app, prm=""):
  #print app
  #os.system(app + prm + " &")
  proc = subprocess.Popen([app, prm], stdout=subprocess.PIPE, shell=True)
  (__out__, __err__) = proc.communicate()
  print "program: " , app, " output: ", __out__, " error: ", __err__


desktop_dir="~/.local/share/applications"
desktop_files="/*.desktop"
