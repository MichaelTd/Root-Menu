#!/usr/bin/env python3
# TkRootMenu.py (tsouchlarakis@gmail.com) A custom menu
# GNU/GPL https://www.gnu.org/licenses/gpl.html
# alsa-utils, sudo, ssh-askpass, xscreensaver, xdotool

import os, sys, shutil
from tkinter import Tk, Button, Scale, Menu, HORIZONTAL, TRUE, FALSE, E, W, S, N
from Executables import __sudo_cmd__, __terminal__, __editor__, __file_manager__, __browser__, __basic_apps__, __net_apps__, __dev_apps__, __media_apps__, __game_apps__, __fs_apps__, __shells__, __admin_apps__, __util_apps__, __config_apps__, __pc_options__

def runCommand(app, prm="", hlpr=0, sudo=0):

    runstr = ""

    if sudo == 1: # Prefix sudo
        runstr += __sudo_cmd__ + " "

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

        opts = (("*resizable", TRUE), ("*tearOff", TRUE))

        for opt, cond in opts:
            self.master.option_add(opt, cond)

        self.master.geometry('105x80+64+64')

        self.u = Button(master, width=1, height=1, text=u"\u2191", command=lambda: runCommand("xdotool key 'ctrl+alt+Up'"))
        self.l = Button(master, width=1, height=3, text=u"\u2190", command=lambda: runCommand("xdotool key 'ctrl+alt+Left'"))
        self.r = Button(master, width=1, height=3, text=u"\u2192", command=lambda: runCommand("xdotool key 'ctrl+alt+Right'"))
        self.d = Button(master, width=1, height=1, text=u"\u2193", command=lambda: runCommand("xdotool key 'ctrl+alt+Down'"))

        self.v = Scale(master, from_=0, to=100, orient=HORIZONTAL, showvalue=0, command=self.setVlm)

        self.u.grid(row=0, sticky=N)
        self.l.grid(row=0, sticky=W)
        self.r.grid(row=0, sticky=E)
        self.d.grid(row=0, sticky=S)
        self.v.grid(row=1)

        self.v.set(75)

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
        for lbl, cmmnd, k in __basic_apps__:
            if shutil.which(cmmnd) is not None:
                appsmenu.add_command(label=lbl, accelerator=k, command=lambda param=cmmnd: runCommand(param))

        appsmenu.add_separator()

        # Internet
        netmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __net_apps__:
            if shutil.which(cmmnd) is not None:
                netmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Dev menu
        devmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __dev_apps__:
            if shutil.which(cmmnd) is not None:
                devmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Multimedia
        mmmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __media_apps__:
            if shutil.which(cmmnd) is not None:
                mmmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Games menu
        gammenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __game_apps__:
            if shutil.which(cmmnd) is not None:
                gammenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # File system tools
        toolsmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __fs_apps__:
            if shutil.which(cmmnd) is not None:
                toolsmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Shells
        shellsmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __shells__:
            if shutil.which(cmmnd) is not None:
                shellsmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Admin tools
        adminmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __admin_apps__:
            adminmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp, 1))

        # Util Menu
        utilmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __util_apps__:
            if shutil.which(cmmnd) is not None:
                utilmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

        # Config Menu
        configmenu = Menu(menubar)
        for lbl, cmmnd, cla, hlpr in __config_apps__:
            if shutil.which(cmmnd) is not None:
                configmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr: runCommand(param, arg, hlp))

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
        for lbl, cmmnd, cla, hlpr, adm in __pc_options__:
            appsmenu.add_command(label=lbl, command=lambda param=cmmnd, arg=cla, hlp=hlpr, sd=adm: runCommand(param, arg, hlp, sd))

        self.master.config(menu=menubar)

    # Menu
    def runRfs(self):
        app = sys.argv[0]
        runCommand(app)
        self.master.quit()

    # Accelearator difinitions
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
