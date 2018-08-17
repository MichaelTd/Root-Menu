#!/usr/bin/env python3
# TkRootMenu.py (tsouchlarakis@gmail.com) A custom menu
# MIT License
# alsa-utils, sudo, ssh-askpass, xscreensaver, xdotool

import os, sys, shutil
#from PIL import ImageTk, Image
from tkinter import Tk, Button, Scale, Menu, HORIZONTAL, TRUE, FALSE, E, W, S, N
from Executables import __sudo_cmd__, __terminal__, __editor__, __file_manager__, __browser__, __basic__, __net__, __dev__, __media__, __games__, __fs__, __shells__, __admin__, __utils__, __config__, __help__, __pc_options__

ncnss = "0"

def runCommand(app, prm="", hlpr=0, sudo=0):

    runstr = ""

    if sudo == 1: # Prefix sudo
        runstr += __sudo_cmd__ + " "

    runstr += "nice -n " + ncnss + " "

    if hlpr == 1: # Append helper
        runstr += __terminal__ + " -e "
    elif hlpr == 2:
        runstr += __editor__ + " "
    elif hlpr == 3:
        runstr += __file_manager__ + " "
    elif hlpr == 4:
        runstr += __browser__ + " "

    runstr += app + " " + prm + " &" # Postfix app, params and background

    print(runstr)
    os.system(runstr)

class TkRootMenu(Tk):

    def __init__(self, master):

        self.master = master

        self.master.title("Root Menu")

        opts = (("*resizable", FALSE), ("*tearOff", FALSE))

        for opt, cond in opts:
            self.master.option_add(opt, cond)

        self.master.geometry('105x50+64+64')

        #self.u = Button(master, width=1, height=1, text=u"\u21E7", command=lambda: runCommand("xdotool key 'Super_L+Up'"))
        self.l = Button(master, width=3, height=1, text=u"\u21E6", command=lambda: runCommand("xdotool key 'Super_L+Left'"))
        self.r = Button(master, width=3, height=1, text=u"\u21E8", command=lambda: runCommand("xdotool key 'Super_L+Right'"))
        #self.d = Button(master, width=1, height=1, text=u"\u21E9", command=lambda: runCommand("xdotool key 'Super_L+Down'"))

        self.v = Scale(master, from_=0, to=100, orient=HORIZONTAL, showvalue=0, command=self.setVlm)

        #self.n = Scale(master, from_=0, to=19 , orient=HORIZONTAL, showvalue=0, command=self.setNcs)

        #self.u.grid(row=0, sticky=N)
        self.l.grid(row=0, sticky=W)
        self.r.grid(row=0, sticky=E)
        #self.d.grid(row=0, sticky=S)

        self.v.grid(row=1)

	#self.n.grid(row=2)

        self.v.set(75)
        #self.n.set(19)

        binds = (
            ("<Control-b>", self.on_accel_runBrowser),
            ("<Control-t>", self.on_accel_runTerminal),
            ("<Control-f>", self.on_accel_runFileManager),
            ("<Control-e>", self.on_accel_runEditor))

        for keys, envt in binds:
            self.master.bind_all(keys, envt)

        menubar = Menu(master)

        appsmenu = Menu(menubar)

        menubar.add_cascade(label="Root Menu", menu=appsmenu)

        # Basic apps
        for lbl, cmmnd, k in __basic__:
            if shutil.which(cmmnd) is not None:
                appsmenu.add_command(label=lbl, accelerator=k, command=lambda param=cmmnd: runCommand(param))

        appsmenu.add_separator()

        # Internet
        netmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __net__:
            if shutil.which(cmmnd) is not None:
                netmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Dev menu
        devmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __dev__:
            if shutil.which(cmmnd) is not None:
                devmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Multimedia
        mmmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __media__:
            if shutil.which(cmmnd) is not None:
                mmmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Games menu
        gammenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __games__:
            if shutil.which(cmmnd) is not None:
                gammenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # File system tools
        toolsmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __fs__:
            if shutil.which(cmmnd) is not None:
                toolsmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Shells
        shellsmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __shells__:
            if shutil.which(cmmnd) is not None:
                shellsmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Admin tools
        adminmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __admin__:
            adminmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp, 1))

        # Util Menu
        utilmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __utils__:
            if shutil.which(cmmnd) is not None:
                utilmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Config Menu
        configmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __config__:
            if shutil.which(cmmnd) is not None:
                configmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Help Menu
        helpmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __help__:
            if shutil.which(cmmnd) is not None:
                helpmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        self.groups = (
            ("Internet", netmenu),
            ("Development", devmenu),
            ("Mediums", mmmenu),
            ("Games", gammenu),
            ("File System", toolsmenu),
            #("Shells", shellsmenu),
            ("Admin Tools", adminmenu),
            ("Utilities", utilmenu),
            ("Config", configmenu))
            # ("Help", helpmenu))

        # Groups
        for lbl, mnGrp in self.groups:
            appsmenu.add_cascade(label=lbl, menu=mnGrp)

        appsmenu.add_separator()

        # Menu
        appsmenu.add_command(label="Edit Menu", command=lambda: runCommand(__editor__ + " " + sys.argv[0]))
        appsmenu.add_command(label="Refresh Menu", command=self.runRfs)
        appsmenu.add_command(label="Close Menu", command=self.master.quit)

        appsmenu.add_separator()

        appsmenu.add_command(label="Lock Screen", command=lambda: runCommand("${HOME}/bin/lock.sh||xscreensaver-command -lock"))

        appsmenu.add_separator()

        # PC
        for lbl, cmmnd, cla, hlpr, adm in __pc_options__:
            appsmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr, sd=adm: runCommand(param, arg, hlp, sd))

        self.master.config(menu=menubar)

    # Menu
    def runRfs(self):
        app = sys.argv[0]
        runCommand(app)
        self.master.quit()

    # Accelearator definitions
    def on_accel_runTerminal(self, widget):
        runCommand(__terminal__)
    def on_accel_runEditor(self, widget):
        runCommand(__editor__)
    def on_accel_runFileManager(self, widget):
        runCommand(__file_manager__)
    def on_accel_runBrowser(self, widget):
        runCommand(__browser__)

    # Volume
    def setVlm(self, widget):
        app = "amixer set 'Master' " + str(self.v.get()) + "%"
        runCommand(app)

    #def setNcs(self, widget):
		#		pass
    #    #ncnss = str(self.n.get())

if __name__ == "__main__":
    master = Tk()
    myMenu = TkRootMenu(master)
    master.mainloop()
