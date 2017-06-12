#!/bin/env python2
# A custom menu (tsouchlarakis@gmail.com)
# GNU/GPL https://www.gnu.org/licenses/gpl.html

# What?
import os
import sys
#from Tkinter import *
from Tkinter import Tk, Label, Button, Scale, Menu, HORIZONTAL, TRUE
#import subprocess
#print os.name

def runCommand(app, prm=""):
  print app
  os.system(app + prm + " &")
  #proc = subprocess.Popen([app, ""], stdout=subprocess.PIPE, shell=True)
  #(__out__, __err__) = proc.communicate()
  #print "program: " , app, " output: ", __out__, " error: ", __err__

class TkRootMenu(Tk):

    def __init__(self, master):

        #self.__terminal__ = "xfce4-terminal --disable-server --geometry=120x40"
        self.__terminal__ = "terminology"
        self.__editor__ = "atom"
        #self.__file_manager__ = "gentoo --root-ok"
        self.__file_manager__ = "xfe"
        self.__browser__ = "firefox"
        #self.__sudo_cmd__ = "SUDO_ASKPASS=/usr/bin/ssh-askpass-fullscreen &&sudo --askpass "
        self.__sudo_cmd__ = "SUDO_ASKPASS=/usr/bin/x11-ssh-askpass sudo --askpass "

        self.master = master
        self.master.title("Root Menu")
        self.master.option_add('*resizable', TRUE)
        self.master.geometry('110x80+64+64')

        self.r = Button(master, text=">>", width=10, command=lambda: runCommand("xdotool key 'ctrl+alt+Right'"))
        self.l = Button(master, text="<<", width=10, command=lambda: runCommand("xdotool key 'ctrl+alt+Left'"))
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
        for lbl, cmmnd, k in (
            ("Terminal", self.__terminal__, "ctl+t"),
            ("Editor", self.__editor__, "ctl+e"),
            ("File Manager", self.__file_manager__, "ctl+f"),
            ("Browser", self.__browser__, "ctl+b")):
            appsmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param), accelerator=k)

        appsmenu.add_separator()

        # Internet
        netmenu = Menu(menubar)

        for lbl, cmmnd in (
            ("Firefox", "firefox"),
            #("Firefox DE", "firefox-de"),
            ("Seamonkey", "seamonkey"),
            ("Tor Network", "cd /opt/tor/ && " + self.__terminal__ + " --login=false"),
            ("Mail", "seamonkey -mail"),
            #("FileZilla", "filezilla"),
            ("W3m", self.__terminal__ + " -e w3m www.google.com"),
            ("HexChat", "hexchat")):
            netmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

        # Dev menu
        devmenu = Menu(menubar)

        for lbl, cmmnd in (
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
            ("Micro", self.__terminal__ + " -e " + "micro"),
            ("Idle", "idle"),
            ("Diakonos", self.__terminal__ + " -e " + "diakonos"),
            ("Vim", self.__terminal__ + " -e vim"),
            #("Cuda Text", "${HOME}/bin/cudatext"),
            ("GVim", "gvim"),
            ("Emacs", "emacs"),
            ("VStudio Code", "code"),
            ("LightTable", "light"),
            ("Sublime Text", "sublime"),
            ("Atom", "atom")):
            #("Xemacs", self.__terminal__ + " -e xemacs"),
            #("Yudit", "yudit"),
            #("JuPyter", self.__terminal__ + " -e jupyter notebook"),
            #("ZED", self.__terminal__ + " -e /bin/env /bin/bash ~/opt/zed/zed"),
            devmenu.add_command(label = lbl,command = lambda param = cmmnd: runCommand(param))

        # Multimedia
        mmmenu = Menu(menubar)

        for lbl, cmmnd in (
            ("Open Office", "ooffice"),
            ("Gimp", "gimp"),
            #("Open Shot", "openshot"),
            ("Blender", "/opt/blender"),
            ("VLC", "vlc"),
            ("Audacious", "audacious"),
            ("Audacity", "audacity")):
            mmmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

        # Games menu
        gammenu = Menu(menubar)

        for lbl, cmmnd in (
            ("GTypist", self.__terminal__ + " -e gtypist"),
            ("KLavaro", "klavaro"),
            ("GNU Back Gammon", "gnubg"),
            ("XGammon", "xgammon"),
            ("XBoard", "xboard"),
            ("Xmahjongg","xmahjongg"),
            ("X Mah-jongg","xmj"),
            ("Quake 3", "~/bin/ioq3"),
            ("Quake 3 TA", "~/bin/ioq3-ta"),
            ("Urban Terror", "~/bin/ut42u"),
            ("Warsow", "~/warsow_21/warsow")):
            gammenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

        # File system tools
        toolsmenu = Menu(menubar)

        for lbl, cmmnd in (
            ("Terminology", "terminology"),
            ("Xfce4 Terminal", "xfce4-terminal --disable-server --geometry=120x40"),
            ("URXVT", "urxvt"),
            ("XTerm", "xterm"),
            #("Hyper", "hyper"),
            ("Midnight Commander", self.__terminal__ + " -e mc"),
            #("Ranger", self.__terminal__ + " -e ranger"),
            #("Rox filer", "rox"),
            ("Gentoo", "gentoo"),
            ("Xfe", "xfe"),
            ("Thunar", "thunar")):
            toolsmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

        # Admin tools
        adminmenu = Menu(menubar)

        for lbl, cmmnd in (
            ("Terminal", self.__sudo_cmd__ + " " + self.__terminal__),
            ("Text Editor", self.__sudo_cmd__ + " " + self.__editor__),
            ("File manager",  self.__sudo_cmd__ + " " + self.__file_manager__),
            ("Midnight Commander", self.__sudo_cmd__ + " " + self.__terminal__ + " -e mc"),
            #("Ranger", self.__sudo_cmd__ + " " + self.__terminal__ + " -e ranger"),
            ("Porthole", self.__sudo_cmd__ + " porthole"),
            ("Wireshark", self.__sudo_cmd__ + " " + self.__terminal__ + " -e wireshark"),
            #("DStat", self.__sudo_cmd__ + " " + self.__terminal__ + " -e dstat -fcdngy"),
            ("Glances", self.__sudo_cmd__ + " " + self.__terminal__ + " -e glances"),
            ("PowerTop", self.__sudo_cmd__ + " " + self.__terminal__ + " -e powertop"),
            ("HTop", self.__sudo_cmd__ + " " + self.__terminal__ + " -e htop"),
            ("Top", self.__sudo_cmd__ + " " + self.__terminal__ + " -e top")):
            adminmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

        # Util Menu
        utilmenu = Menu(menubar)

        for lbl, cmmnd in (
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
            ("jsCalculator", self.__browser__ + " ~/git/fcc-app/01-front-end-cert/07-javascript-calculator/jc.html"),
            ("Calculator", "calculator")):
            utilmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

        # Config Menu
        configmenu = Menu(menubar)

        for lbl, cmmnd in (
            ("Compiz settings manager", "ccsm"),
            ("Emerald themes manager", "emerald-theme-manager"),
            ("Conky config", self.__editor__ + " ~/.conky.conf/"),
            ("Edit backup files", self.__editor__ + " ~/.backup.*"),
            ("Edit shell files", self.__editor__ + " ~/.zsh* ~/.bash* /etc/bash/bashrc.d/*.sh "),
            ("View Log files", self.__editor__ + " /var/log/"),
            ("X Screen Saver", "xscreensaver-demo"),
            ("Pavucontrol", "pavucontrol"),
            #("Xfce4-alsa-control", "xfce4-alsa-control"),
            #("Alsamixer Gui", "alsamixergui"),
            ("Alsamixer", self.__terminal__ + " -e alsamixer")):
            configmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

        # Groups
        for lbl, mnGrp in (
            ("Internet", netmenu),
            ("Development", devmenu),
            ("Mediums", mmmenu),
            ("Games", gammenu),
            ("File System", toolsmenu),
            ("Admin Tools", adminmenu),
            ("Utilities", utilmenu),
            ("Config", configmenu)):
            appsmenu.add_cascade(label=lbl,menu=mnGrp)

        appsmenu.add_separator()

        # Menu
        #appsmenu.add_command(label="Edit Menu", command=lambda: runCommand("idle2.7" + " /usr/local/bin/tkRootMenu.py"))
        appsmenu.add_command(label="Edit Menu", command=lambda: runCommand(self.__editor__ + " " + sys.argv[0]))
        appsmenu.add_command(label="Refresh Menu", command=self.runRfs)
        appsmenu.add_command(label="Close Menu", command=self.master.quit)

        appsmenu.add_separator()

        # PC
        for lbl, cmmnd in (
            ("Logout", "kill -15 -1"),
            ("Reboot", self.__sudo_cmd__ + " shutdown -r now"),
            ("Shutdown", self.__sudo_cmd__ + " shutdown -h now")):
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
        runCommand(self.__terminal__)
    def on_accel_runEditor(self, widget):
        runCommand(self.__editor__)
    def on_accel_runFileManager(self, widget):
        runCommand(self.__file_manager__)
    def on_accel_runBrowser(self, widget):
        runCommand(self.__browser__)

    # Volume
    def setVlm(self, widget):
        #app = "amixer cset id=1 " + str(v.get()) + "%"
        app = "amixer set 'Master' " + str(self.v.get())
        runCommand(app)

if __name__ == "__main__":
    master = Tk()
    myMenu = TkRootMenu(master)
    master.mainloop()