#!/usr/bin/env python3
# A custom menu (tsouchlarakis@gmail.com)
# GNU/GPL https://www.gnu.org/licenses/gpl.html

import os, sys, shutil
from tkinter import Tk, Label, Button, Scale, Menu, HORIZONTAL, TRUE, FALSE, E, W, S, N
from apps import *

print (os.name)
print (sys.argv[0])

def runCommand(app, prm="", hlpr=0, sudo=0):
    runstr = ""
    if sudo == 1: # Prefix sudo
        runstr += __sudo_cmd__ + " "

    if hlpr == 1: # Postfix helper
        runstr += __terminal__ + " -e "
    elif hlpr == 2:
        runstr += __editor__ + " "
    elif hlpr == 3:
        runstr += __file_manager__ + " "
    elif hlpr == 4:
        runstr += __browser__ + " "

    runstr += app + " " + prm + " &" # Append app, params and background

    print(runstr)
    os.system(runstr)

class TkRootMenu(Tk):

    def __init__(self, master):

        self.master = master
        self.master.title("Root Menu")

        opts=(("*resizable", TRUE), ("*tearOff", FALSE))
        for opt, cond in opts:
          self.master.option_add(opt, cond)

        self.master.geometry('105x50+64+64')

        self.l = Button(master, width=3, text="<=", command=lambda: runCommand("xdotool key 'ctrl+alt+Left'"))
        self.r = Button(master, width=3, text="=>", command=lambda: runCommand("xdotool key 'ctrl+alt+Right'"))

        self.v = Scale(master, from_=0, to=100, orient=HORIZONTAL, showvalue=0, command=self.setVlm)

        self.l.grid(row=0, sticky=W)
        self.r.grid(row=0, sticky=E)
        self.v.grid(row=1)

        self.v.set(100)

        self.master.bind_all("<Control-b>", self.on_accel_runBrowser)
        self.master.bind_all("<Control-t>", self.on_accel_runTerminal)
        self.master.bind_all("<Control-f>", self.on_accel_runFileManager)
        self.master.bind_all("<Control-e>", self.on_accel_runEditor)

        menubar = Menu(master)

        appsmenu = Menu(menubar)

        menubar.add_cascade(label="Root Menu", menu=appsmenu)

        # Basic apps
        for lbl, cmmnd, k in basic_apps:
            if shutil.which(cmmnd) is not None:
                appsmenu.add_command(label=lbl, accelerator=k, command=lambda param=cmmnd: runCommand(param))

        appsmenu.add_separator()

        # Internet
        netmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in net_apps:
            if shutil.which(cmmnd) is not None:
                netmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Dev menu
        devmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in dev_apps:
            if shutil.which(cmmnd) is not None:
                devmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Multimedia
        mmmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in media_apps:
            if shutil.which(cmmnd) is not None:
                mmmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Games menu
        gammenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in game_apps:
            if shutil.which(cmmnd) is not None:
                gammenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # File system tools
        toolsmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in fs_apps:
            if shutil.which(cmmnd) is not None:
                toolsmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Admin tools
        adminmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in admin_apps:
            adminmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp, 1))

        # Util Menu
        utilmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in util_apps:
            if shutil.which(cmmnd) is not None:
                utilmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Config Menu
        configmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in config_apps:
            if shutil.which(cmmnd) is not None:
                configmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        self.groups = (
            ("Internet", netmenu),
            ("Development", devmenu),
            ("Mediums", mmmenu),
            ("Games", gammenu),
            ("File System", toolsmenu),
            ("Admin Tools", adminmenu),
            ("Utilities", utilmenu),
            ("Config", configmenu))

        # Groups
        for lbl, mnGrp in self.groups:
            appsmenu.add_cascade(label=lbl, menu=mnGrp)

        appsmenu.add_separator()

        # Menu
        appsmenu.add_command(label="Edit Menu", command=lambda: runCommand(__editor__ + " " + sys.argv[0]))
        appsmenu.add_command(label="Refresh Menu", command=self.runRfs)
        appsmenu.add_command(label="Close Menu", command=self.master.quit)

        appsmenu.add_separator()

        appsmenu.add_command(label="Lock Screen", command=lambda: runCommand("xscreensaver-command -lock"))

        appsmenu.add_separator()

        # PC
        for lbl, cmmnd, cla, hlpr, adm in pc_options:
            appsmenu.add_command(label=lbl,command=lambda param=cmmnd, arg=cla, hlp=hlpr, sd=adm: runCommand(param, arg, hlp, sd))

        self.master.config(menu=menubar)

    # Menu
    def runRfs(self):
        app = sys.argv[0]
        runCommand(app)
        self.master.quit()

    # Default Apps
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

if __name__ == "__main__":
    master = Tk()
    myMenu = TkRootMenu(master)
    master.mainloop()
