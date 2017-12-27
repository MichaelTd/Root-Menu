#!/usr/bin/env python3
# A custom menu (tsouchlarakis@gmail.com)
# GNU/GPL https://www.gnu.org/licenses/gpl.html

import os, sys, shutil
from tkinter import Tk, Label, Button, Scale, Menu, HORIZONTAL, TRUE, FALSE, E, W, S, N

print (os.name)
print (sys.argv[0])

__sudo_cmd__ = "SUDO_ASKPASS=`which x11-ssh-askpass|which ssh-askpass` sudo --login --askpass "
__terminal__ = "terminology"
__editor__ = "code"
__file_manager__ = "gentoo --root-ok"
__browser__ = "firefox"

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

basic_apps = (
    ("Terminal", __terminal__, "ctl+t"),
    ("Editor", __editor__, "ctl+e"),
    ("File Manager", __file_manager__, "ctl+f"),
    ("Browser", __browser__, "ctl+b"))

net_apps = (
    ("Firefox", "firefox", "", 0),
    ("Firefox DE", "firefox-de", "", 0),
    ("Seamonkey", "seamonkey", "", 0),
    ("Opera","opera", "", 0),
    ("Seamonkey Mail", "seamonkey", "-mail", 0),
    ("Pidgin", "pidgin", "", 0),
    ("FileZilla", "filezilla", "", 0),
    ("Midori", "midori", "", 0),
    ("W3m", "w3m", "-v", 1),
    ("Lynx", "lynx", "", 1),
    ("Quassel IRC", "quassel", "", 0),
    ("HexChat IRC", "hexchat", "", 0))

dev_apps = (
    ("Eclipse", "eclipse", "", 0),
    ("Netbeans", "netbeans", "", 0),
    ("KDevelop", "kdevelop", "", 0),
    ("QtCreator", "qtcreator.sh", "", 0),
    ("QtDesigner", "qtchooser", "-run-tool=designer -qt=5", 0),
    ("QtDesigner", "designer", "", 0),
    ("QtCreator", "qtcreator.sh", "", 0),
    ("Code Blocks", "codeblocks", "", 0),
    ("Glade", "glade", "", 0),
    ("Pg Admin3", "pgadmin3", "", 0),
    ("Scite", "scite", "", 0),
    ("Idle", "idle", "", 0),
    ("Diakonos", "diakonos", "", 1),
    ("Slap", "slap", "", 1),
    ("Just MarkDown", "justmd", "", 0),
    ("Micro", "micro", "", 1),
    ("Vim", "vim", "", 1),
    ("emacs-nox", "emacs", "-nw", 1),
    ("Cuda Text", "cudatext", "", 0),
    ("NEdit", "nedit", "", 0),
    ("Tea", "tea", "", 0),
    ("GVim", "gvim", "", 0),
    ("Yudit", "yudit", "", 0),
    ("JuPyter", "jupyter", "notebook", 1),
    ("XEmacs", "xemacs", "", 0),
    ("Emacs", "emacs", "", 0),
    ("Geany", "geany", "", 0),
    ("Blue Fish", "bluefish", "", 0),
    ("ZED", "zed", "", 1),
    ("Brackets", "brackets", "", 0),
    ("VSCode", "code", "", 0),
    ("VSCode", "vscode", "", 0),
    ("LightTable", "light", "", 0),
    ("LightTable", "lighttable", "", 0),
    ("Sublime Text", "sublime_text", "", 0),
    ("Atom", "atom", "", 0))

media_apps = (
    ("Open Office", "ooffice", "", 0),
    ("Libre Office", "loffice", "", 0),
    ("Calcurse", "calcurse", "", 1),
    ("Abi Word", "abiword", "", 0),
    ("Scribus", "scribus-1.4.6", "", 0),
    ("Inkscape", "inkscape", "", 0),
    ("XFig", "xfig", "", 0),
    ("Dia", "dia", "", 0),
    ("FreeCAD", "freecad", "", 0),
    ("Open Shot", "openshot", "", 0),
    ("Blender", "blender", "", 0),
    ("Kodi", "kodi", "", 0),
    ("VLC", "vlc", "", 0),
    ("Dark Table", "darktable", "", 0),
    ("Gimp", "gimp", "", 0),
    ("Audacity", "audacity", "", 0),
    ("Audacious", "audacious", "", 0))

game_apps = (
    ("GTypist", "gtypist", "", 1),
    ("KLavaro", "klavaro", "", 0),
    ("Lutris", "lutris", "", 0),
    ("Gx Mame", "gxmame", "", 0),
    ("Advanced Mame Menu", "advmenu", "", 0),
    ("Snake 3D", "snake3d", "", 0),
    ("GNU Back Gammon", "gnubg", "", 0),
    ("XGammon", "xgammon", "", 0),
    ("XBoard", "xboard", "", 0),
    ("Xmahjongg","xmahjongg", "", 0),
    ("X Mah-jongg","xmj", "", 0),
    ("Quake 3", "ioq3", "", 1),
    ("Quake 3 TA", "ioq3-ta", "", 1),
    ("Urban Terror", "Quake3-UrT.x86_64", "", 1),
    ("Warsow", "warsow", "", 1))

fs_apps = (
    ("Terminology", "terminology", "", 0),
    ("CRT", "cool-retro-term", "", 0),
    ("Xfce4 Terminal", "xfce4-terminal", "--disable-server", 0),
    ("URXVT", "urxvt", "", 0),
    ("URXVT", "uxterm", "", 0),
    ("XTerm", "xterm", "", 0),
    ("Hyper", "hyper", "", 0),
    ("Midnight Commander", "mc", "", 1),
    ("Ranger", "ranger", "", 1),
    ("Rox filer", "rox", "", 0),
    ("ViFm", "vifm", "", 1),
    ("Gentoo", "gentoo", "", 0),
    ("Xfe", "xfe", "", 0),
    ("SpaceFM", "spacefm", "", 0),
    ("Thunar", "thunar", "", 0))

admin_apps = (
    ("Terminal", __terminal__, "", 0),
    ("Text Editor", __editor__, "", 0),
    ("File manager", __file_manager__, "", 0),
    ("Midnight Commander", "mc", "", 1),
    ("Ranger", "ranger", "", 1),
    ("Porthole", "porthole", "", 0),
    ("Synaptic", "synaptic", "", 0),
    ("gtk Partition Editor", "gparted", "", 0),
    ("cli Partition Editor", "parted", "", 1),
    ("Wireshark", "wireshark", "", 0),
    ("DStat", "dstat", "-fcdngy", 1),
    ("C Sys Dig", "csysdig", "", 1),
    ("Glances", "glances", "", 1),
    ("PowerTop", "powertop", "", 1),
    ("HTop", "htop", "", 1),
    ("Top", "top", "", 1))

util_apps = (
    ("App Runner", 'xterm -e TMPFILE=/tmp/${RANDOM}.input.box.txt && dialog --title "Command Input" --default-button "ok" --inputbox "Enter command to continue" 10 40 command 2> ${TMPFILE} && $(cat ${TMPFILE})', "", 0),
    ("App Runner", "runcmd.sh", "", 0),
    ("Xfce4 App Finder", "xfce4-appfinder", "--collapsed --disable-server", 0),
    ("Synapse", "synapse", "", 0),
    ("Xfce4 Screenshot", "xfce4-screenshooter", "", 0),
    ("Screengrab", "screengrab", "", 0),
    ("Shutter","shutter", "", 0),
    ("Take a shot now", "imss.sh", "2", 0),
    ("Simple Screen Recorder", "simplescreenrecorder", "", 0),
    ("Viewnior", "viewnior", "", 0),
    ("Ristretto", "ristretto", "", 0),
    ("PeaZip", "peazip", "", 0),
    ("Xarchiver", "xarchiver", "", 0),
    ("Foxit Reader", "foxitreader", "", 0),
    ("Evince", "evince", "", 0),
    ("XPdf", "xpdf", "", 0),
    ("Ghost View", "gv", "", 0),
    ("Xv", "xv", "", 0),
    ("Fox Calc","calculator", "", 0),
    ("XCalc","xcalc", "", 0),
    ("Calcoo","calcoo", "", 0),
    ("Term Calc", "calc", "", 1),
    ("jCalc", "jCalc.sh", "", 0),
    ("jsCalculator", "~/git/freeCodeCamp/01-front-end-cert/07-javascript-calculator/jc.html", "", 4))

config_apps = (
    ("Compiz settings manager", "ccsm", "", 0),
    ("Emerald themes manager", "emerald-theme-manager", "", 0),
    ("Tint Wizard", "tintwizard", "", 0),
    ("Tint2 Config", "tint2conf", "", 0),
    ("OpenBox conf", "obconf", "", 0),
    ("Qt Config", "qtconfig", "", 0),
    ("X Screen Saver", "xscreensaver-demo", "", 0),
    ("Wicd gtk", "wicd-gtk", "", 0),
    ("Wicd curses", "wicd-curses", "", 1),
    ("Xfce4-alsa-control", "xfce4-alsa-control", "", 0),
    ("Alsamixer Gui", "alsamixergui", "", 0),
    ("Alsamixer", "alsamixer", "", 1),
    ("Xfce4 Mixer", "xfce4-mixer", "", 0),
    ("Volume Prefs", "paprefs", "", 0),
    ("Volume Controls", "pavucontrol", "", 0))

pc_options = (
    ("Logout", "kill", "-15 -1", 1, 0),
    ("Reboot", "shutdown", "-r now", 1, 1),
    ("Shutdown","shutdown", "-h now", 1, 1))

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
