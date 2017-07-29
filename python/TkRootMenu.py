#!/bin/env python2
# A custom menu (tsouchlarakis@gmail.com)
# GNU/GPL https://www.gnu.org/licenses/gpl.html

import os
import sys
from Tkinter import Tk, Label, Button, Scale, Menu, HORIZONTAL, TRUE
#import subprocess
#print os.name

def runCommand(app, prm=""):
  print app
  os.system(app + prm + " &")
  #proc = subprocess.Popen([app, ""], stdout=subprocess.PIPE, shell=True)
  #(__out__, __err__) = proc.communicate()
  #print "program: " , app, " output: ", __out__, " error: ", __err__

#__terminal__ = "xfce4-terminal --disable-server --geometry=120x40"
__terminal__ = "terminology"
#__editor__ = __terminal__ + " -e /bin/env /bin/bash  ~/opt/zed/zed"
#__editor__ = __terminal__ + " -e micro"
__editor__ = "atom"
#__editor__ = "nedit"
#__file_manager__ = "gentoo --root-ok"
__file_manager__ = "xfe"
#__file_manager__ = "spacefm"
__browser__ = "~/bin/firefox-de"
#__sudo_cmd__ = "SUDO_ASKPASS=/usr/bin/ssh-askpass-fullscreen &&sudo --askpass "
__sudo_cmd__ = "SUDO_ASKPASS=/usr/bin/x11-ssh-askpass sudo --login --askpass "

basic_apps = (
    ("Terminal", __terminal__, "ctl+t"),
    ("Editor", __editor__, "ctl+e"),
    ("File Manager", __file_manager__, "ctl+f"),
    ("Browser", __browser__, "ctl+b"))

net_apps = (
    ("Firefox", "firefox"),
    ("Firefox DE", "~/bin/firefox-de"),
    ("Seamonkey", "seamonkey"),
    ("Tor Network", "cd /opt/tor/ && " + __terminal__ + " --login=false"),
    ("Mail", "seamonkey -mail"),
    #("FileZilla", "filezilla"),
    ("W3m", __terminal__ + " -e w3m www.google.com"),
    ("Quassel IRC", "quassel"),
    ("HexChat IRC", "hexchat"))

dev_apps = (
    ("Eclipse", "eclipse"),
    ("Netbeans", "netbeans"),
    ("KDevelop", "kdevelop"),
    #("QtCreator", "qtcreator.sh"),
    #("QtDesigner", "qtchooser -run-tool=designer -qt=5"),
    ("QtDesigner", "~/opt/qt/5.8/gcc_64/bin/designer"),
    ("QtCreator", "~/opt/qt/Tools/QtCreator/bin/qtcreator.sh"),
    ("Code Blocks", "codeblocks"),
    ("Glade", "glade"),
    ("Pg Admin3", "pgadmin3"),
    ("Micro", __terminal__ + " -e " + "micro"),
    ("Idle", "idle"),
    ("Diakonos", __terminal__ + " -e " + "diakonos"),
    #("Slap", __terminal__ + " -e " + "~/bin/slap"),
    ("Vim", __terminal__ + " -e vim"),
    ("Cuda Text", "${HOME}/bin/cudatext"),
    ("NEdit", "nedit"),
    ("Tea", "tea"),
    ("GVim", "gvim"),
    #("Xemacs", __terminal__ + " -e xemacs"),
    #("Yudit", "yudit"),
    #("JuPyter", __terminal__ + " -e jupyter notebook"),
    ("Emacs", "emacs"),
    ("ZED", __terminal__ + " -e /bin/env /bin/bash ~/opt/zed/zed"),
    ("VSCode", "code"),
    ("LightTable", "light"),
    ("Sublime Text", "sublime"),
    ("Atom", "atom"))

media_apps = (
    ("Open Office", "ooffice"),
    ("Gimp", "gimp"),
    #("Open Shot", "openshot"),
    ("Blender", "/opt/blender"),
    ("VLC", "vlc"),
    ("Audacious", "audacious"),
    ("Audacity", "audacity"))

game_apps = (
    ("GTypist", __terminal__ + " -e gtypist"),
    ("KLavaro", "klavaro"),
    ("Lutris", "~/opt/lutris/bin/lutris"),
    ("GNU Back Gammon", "gnubg"),
    ("XGammon", "xgammon"),
    ("XBoard", "xboard"),
    ("Xmahjongg","xmahjongg"),
    ("X Mah-jongg","xmj"),
    ("Quake 3", "~/bin/ioq3"),
    ("Quake 3 TA", "~/bin/ioq3-ta"),
    ("Urban Terror", __terminal__ + " -e ~/opt/UrbanTerror43/Quake3-UrT.x86_64"),
    ("Warsow", __terminal__ + " -e ~/opt/warsow_21/warsow"))

fs_apps = (
    ("Terminology", "terminology"),
    ("Xfce4 Terminal", "xfce4-terminal --disable-server --geometry=120x40"),
    ("URXVT", "urxvt"),
    ("XTerm", "xterm"),
    #("Hyper", "hyper"),
    ("Midnight Commander", __terminal__ + " -e mc"),
    #("Ranger", __terminal__ + " -e ranger"),
    #("Rox filer", "rox"),
    ("ViFm", __terminal__ + " -e vifm"),
    ("Gentoo", "gentoo"),
    ("Xfe", "xfe"),
    ("SpaceFM", "spacefm"),
    ("Thunar", "thunar"))

admin_apps = (
    ("Terminal", __sudo_cmd__ + " " + __terminal__),
    ("Text Editor", __sudo_cmd__ + " " + __editor__),
    ("File manager",  __sudo_cmd__ + " " + __file_manager__),
    ("Midnight Commander", __sudo_cmd__ + " " + __terminal__ + " -e mc"),
    #("Ranger", __sudo_cmd__ + " " + __terminal__ + " -e ranger"),
    ("Porthole", __sudo_cmd__ + " porthole"),
    ("Wireshark", __sudo_cmd__ + " " + __terminal__ + " -e wireshark"),
    #("DStat", __sudo_cmd__ + " " + __terminal__ + " -e dstat -fcdngy"),
    ("Glances", __sudo_cmd__ + " " + __terminal__ + " -e glances"),
    ("PowerTop", __sudo_cmd__ + " " + __terminal__ + " -e powertop"),
    ("HTop", __sudo_cmd__ + " " + __terminal__ + " -e htop"),
    ("Top", __sudo_cmd__ + " " + __terminal__ + " -e top"))

util_apps = (
    ("App Runner", "~/bin/runcmd.sh"),
    ("Xfce4 App Finder", "xfce4-appfinder --collapsed --disable-server"),
    ("Xfce4 Screenshot", "xfce4-screenshooter"),
    #("Screengrab", "screengrab"),
    ("Take a shot now", "~/bin/imss.sh 2"),
    ("Viewnior", "viewnior"),
    #("PeaZip", "peazip"),
    ("Xarchiver", "xarchiver"),
    ("Ghost View", "gv"),
    ("Foxit Reader", "foxitreader"),
    ("Xv", "xv"),
    ("jCalculator", "jCalculator.sh"),
    ("jsCalculator", __browser__ + " ~/git/freeCodeCamp/01-front-end-cert/07-javascript-calculator/jc.html"),
    ("Calculator", "calculator"))

config_apps = (
    ("Compiz settings manager", "ccsm"),
    ("Emerald themes manager", "emerald-theme-manager"),
    ("Conky config", __editor__ + " ~/.conky.conf/"),
    ("Edit backup files", __editor__ + " ~/.backup.txt"),
    ("Edit shell files", __editor__ + " ~/.zsh* ~/.bash* /etc/bash/bashrc.d/*.sh "),
    ("View Log files", __editor__ + " /var/log/"),
    ("X Screen Saver", "xscreensaver-demo"),
    #("Xfce4-alsa-control", "xfce4-alsa-control"),
    #("Alsamixer Gui", "alsamixergui"),
    ("Alsamixer", __terminal__ + " -e alsamixer"),
    ("Volume Prefs", "paprefs"),
    ("Volume Controls", "pavucontrol"))

pc_options = (
    ("Logout", "kill -15 -1"),
    ("Reboot", __sudo_cmd__ + " shutdown -r now"),
    ("Shutdown", __sudo_cmd__ + " shutdown -h now"))

class TkRootMenu(Tk):

    def __init__(self, master):

        self.master = master
        self.master.title("Root Menu")
        self.master.option_add('*resizable', TRUE)
        self.master.geometry('110x80+64+64')

        self.r = Button(master, text="=>", width=10, command=lambda: runCommand("xdotool key 'ctrl+alt+Right'"))
        self.l = Button(master, text="<=", width=10, command=lambda: runCommand("xdotool key 'ctrl+alt+Left'"))
        self.v = Scale(master, from_=0, to=100, orient=HORIZONTAL, showvalue=0, command=self.setVlm)

        self.v.set(100)

        #tmp=`amixer cget numid=3|grep -e "[0-9]\{5\}\$"`
        #vlm=${tmp:(-5)}

        self.r.pack()
        self.l.pack()
        self.v.pack()

        self.master.bind_all("<Control-b>", self.on_accel_runBrowser)
        self.master.bind_all("<Control-t>", self.on_accel_runTerminal)
        self.master.bind_all("<Control-f>", self.on_accel_runFileManager)
        self.master.bind_all("<Control-e>", self.on_accel_runEditor)

        menubar = Menu(master)

        appsmenu = Menu(menubar)

        menubar.add_cascade(label="Root Menu", menu=appsmenu)

        # Basic apps
        for lbl, cmmnd, k in basic_apps:
            appsmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param), accelerator=k)

        appsmenu.add_separator()

        # Internet
        netmenu = Menu(menubar)
        for lbl, cmmnd in net_apps:
            netmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

        # Dev menu
        devmenu = Menu(menubar)
        for lbl, cmmnd in dev_apps:
            devmenu.add_command(label = lbl,command = lambda param = cmmnd: runCommand(param))

        # Multimedia
        mmmenu = Menu(menubar)
        for lbl, cmmnd in media_apps:
            mmmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

        # Games menu
        gammenu = Menu(menubar)
        for lbl, cmmnd in game_apps:
            gammenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

        # File system tools
        toolsmenu = Menu(menubar)
        for lbl, cmmnd in fs_apps:
            toolsmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

        # Admin tools
        adminmenu = Menu(menubar)
        for lbl, cmmnd in admin_apps:
            adminmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

        # Util Menu
        utilmenu = Menu(menubar)
        for lbl, cmmnd in util_apps:
            utilmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

        # Config Menu
        configmenu = Menu(menubar)
        for lbl, cmmnd in config_apps:
            configmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

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
            appsmenu.add_cascade(label=lbl,menu=mnGrp)

        appsmenu.add_separator()

        # Menu
        appsmenu.add_command(label="Edit Menu", command=lambda: runCommand(__editor__ + " " + sys.argv[0]))
        appsmenu.add_command(label="Refresh Menu", command=self.runRfs)
        appsmenu.add_command(label="Close Menu", command=self.master.quit)

        appsmenu.add_separator()

        # PC
        for lbl, cmmnd in pc_options:
            appsmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

        self.master.config(menu=menubar)

    # Menu
    def runRfs(self):
        #app = "/usr/local/bin/tkRootMenu.sh"
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
        #app = "amixer cset id=1 " + str(v.get()) + "%"
        app = "amixer set 'Master' " + str(self.v.get())
        runCommand(app)

if __name__ == "__main__":
    master = Tk()
    myMenu = TkRootMenu(master)
    master.mainloop()
