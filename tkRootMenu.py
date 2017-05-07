#!/usr/bin/python2
# A custom menu (tsouchlarakis@gmail.com)
# GNU/GPL https://www.gnu.org/licenses/gpl.html

import os
from Tkinter import *
#import subprocess
#print os.name

#__terminal__ = "xfce4-terminal --disable-server --geometry=120x40"
__terminal__ = "terminology"
__editor__ = "atom"
#__file_manager__ = "gentoo --root-ok"
__file_manager__ = "xfe"
__browser__ = "firefox"
#__sudo_cmd__ = "SUDO_ASKPASS=/usr/bin/ssh-askpass-fullscreen &&sudo --askpass "
__sudo_cmd__ = "SUDO_ASKPASS=/usr/bin/x11-ssh-askpass sudo --askpass "

def runCommand(app, prm=""):
  print app
  os.system(app + " &")
  #proc = subprocess.Popen([app, ""], stdout=subprocess.PIPE, shell=True)
  #(__out__, __err__) = proc.communicate()
  #print "program: " , app, " output: ", __out__, " error: ", __err__

# Menu
def runRfs():
  app = "/usr/local/bin/tkRootMenu.sh"
  runCommand(app)
  root.quit()

# Volume
def setVlm(widget):
  #app = "amixer cset id=1 " + str(v.get()) + "%"
  app = "amixer set 'Master' " + str(v.get())
  runCommand(app)

# Default Apps
def on_accel_runTerminal(widget):
  runCommand(__terminal__)
def on_accel_runEditor(widget):
  runCommand(__editor__)
def on_accel_runFileManager(widget):
  runCommand(__file_manager__)
def on_accel_runBrowser(widget):
  runCommand(__browser__)

root = Tk()
root.title("Root Menu")
root.option_add('*resizable', TRUE)
root.geometry('110x80+64+64')

r = Button(root, text=">>", width=10, command=lambda: runCommand("xdotool key 'ctrl+alt+Right'"))
l = Button(root, text="<<", width=10, command=lambda: runCommand("xdotool key 'ctrl+alt+Left'"))
v = Scale(root, from_=0, to=100, orient=HORIZONTAL, showvalue=0, command=setVlm)

v.set((100/2)-15)

#tmp=`amixer cget numid=3|grep -e "[0-9]\{5\}\$"`
#vlm=${tmp:(-5)}

r.pack()
l.pack()
v.pack()

root.bind_all("<Control-b>", on_accel_runBrowser)
root.bind_all("<Control-t>", on_accel_runTerminal)
root.bind_all("<Control-f>", on_accel_runFileManager)
root.bind_all("<Control-e>", on_accel_runEditor)

menubar = Menu(root)

# File system tools
toolsmenu = Menu(menubar)

for lbl, cmmnd in (
  ("Terminology", "terminology"),
  ("Xfce4 Terminal", "xfce4-terminal --disable-server --geometry=120x40"),
  ("URXVT", "urxvt"),
  #("Hyper", "hyper"),
  ("Midnight Commander", __terminal__ + " -e mc"),
  ("Ranger", __terminal__ + " -e ranger"),
  #("Rox filer", "rox"),
  ("Gentoo", "gentoo"),
  ("Xfe", "xfe"),
  ("Thunar", "thunar")):
  toolsmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

# Admin tools
adminmenu = Menu(menubar)

for lbl, cmmnd in (
  ("Terminal", __sudo_cmd__ + " " + __terminal__),
  ("Text Editor", __sudo_cmd__ + " " + __editor__),
  ("File manager",  __sudo_cmd__ + " " + __file_manager__),
  ("Midnight Commander", __sudo_cmd__ + " " + __terminal__ + " -e mc"),
  ("Ranger", __sudo_cmd__ + " " + __terminal__ + " -e ranger"),
  ("Porthole", __sudo_cmd__ + " porthole"),
  ("Wireshark", __sudo_cmd__ + " " + __terminal__ + " -e wireshark"),
  #("DStat", __sudo_cmd__ + " " + __terminal__ + " -e dstat -fcdngy"),
  ("Glances", __sudo_cmd__ + " " + __terminal__ + " -e glances"),
  ("PowerTop", __sudo_cmd__ + " " + __terminal__ + " -e powertop"),
  ("HTop", __sudo_cmd__ + " " + __terminal__ + " -e htop"),
  ("Top", __sudo_cmd__ + " " + __terminal__ + " -e top")):
  adminmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

# Config Menu
configmenu = Menu(menubar)

for lbl, cmmnd in (
  ("Compiz settings manager", "ccsm"),
  ("Emerald themes manager", "emerald-theme-manager"),
  ("Conky config", __editor__ + " ~/.conky.conf/"),
  ("Edit backup files", __editor__ + " ~/.backup.*"),
  ("Edit shell files", __editor__ + " ~/.zsh* ~/.bash* /etc/bash/bashrc.d/*.sh "),
  #("View Log files", __editor__ + " /var/log/system.update.log /var/log/perl.update.log /var/log/data.mirror.log /var/log/paperjam.backup.log"),
  ("View Log files", __editor__ + " /var/log/"),
  ("X Screen Saver", "xscreensaver-demo"),
  ("Pavucontrol", "pavucontrol"),
  #("Xfce4-alsa-control", "xfce4-alsa-control"),
  #("Alsamixer Gui", "alsamixergui"),
  ("Alsamixer", __terminal__ + " -e alsamixer")):
  configmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

# Dev menu
devmenu = Menu(menubar)

for lbl, cmmnd in (
  ("Eclipse", "eclipse"),
  ("Netbeans", "netbeans"),
  ("KDevelop", "kdevelop"),
  #("QtCreator", "qtcreator.sh"),
  ("QtDesigner", "qtchooser -run-tool=designer -qt=4"),
  ("Glade", "glade"),
  ("Pg Admin3", "pgadmin3"),
  ("Micro", __terminal__ + " -e " + "micro"),
  ("Diakonos", __terminal__ + " -e " + "diakonos"),
  ("Atom", "atom"),
  ("VStudio Code", "code"),
  ("Sublime Text", "sublime"),
  ("LightTable", "light"),
  ("Cuda Text", "${HOME}/bin/cudatext"),
  ("Emacs", "emacs"),
  ("GVim", "gvim"),
  ("Idle", "idle")):
  #("Vim", __terminal__ + " -e vim"),
  #("Diakonos", __terminal__ + " -e diakonos"),
  #("Xemacs", __terminal__ + " -e xemacs"),
  #("Yudit", "yudit"),
  #("JuPyter", __terminal__ + " -e jupyter notebook"),
  #("ZED", __terminal__ + " -e /bin/env /bin/bash ~/opt/zed/zed"),
  devmenu.add_command(label = lbl,command = lambda param = cmmnd: runCommand(param))

# Internet
netmenu = Menu(menubar)

for lbl, cmmnd in (
  ("Firefox", "firefox"),
  #("Firefox DE", "firefox-de"),
  ("Seamonkey", "seamonkey"),
  ("Mail", "seamonkey -mail"),
  #("FileZilla", "filezilla"),
  ("HexChat", "hexchat")):
  netmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

# Multimedia
mmmenu = Menu(menubar)

for lbl, cmmnd in (
  ("Open Office", "ooffice"),
  ("Gimp", "gimp"),
  #("Open Shot", "openshot"),
  ("VLC", "vlc"),
  ("Audacious", "audacious")):
  mmmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

# Games menu
gammenu = Menu(menubar)

for lbl, cmmnd in (
  ("GTypist", __terminal__ + " -e gtypist"),
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

# Util Menu
utilmenu = Menu(menubar)

for lbl, cmmnd in (
  ("App Runner", "~/bin/runcmd.sh"),
  ("Xfce4 App Finder", "xfce4-appfinder --collapsed --disable-server"),
  ("Xfce4 Screenshot", "xfce4-screenshooter"),
  ("Screengrab", "screengrab"),
  ("Take a shot now", "~/bin/imss.sh 2"),
  ("Viewnior", "viewnior"),
  #("PeaZip", "peazip"),
  ("Xarchiver", "xarchiver"),
  ("Ghost View", "gv"),
  ("Foxit Reader", "foxitreader"),
  ("Xv", "xv"),
  ("jCalculator", "jCalculator.sh"),
  ("jsCalculator", __browser__ + " ~/git/fcc-app/01-front-end-cert/07-javascript-calculator/jc.html"),
  ("Calculator", "calculator")):
  utilmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

appsmenu = Menu(menubar)

menubar.add_cascade(label="Root Menu", menu=appsmenu)

# Basic apps
for lbl, cmmnd, k in (
  ("Terminal", __terminal__, "ctl+t"),
  ("Editor", __editor__, "ctl+e"),
  ("File Manager", __file_manager__, "ctl+f"),
  ("Browser", __browser__, "ctl+b")):
  appsmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param), accelerator=k)

appsmenu.add_separator()

# Groups
for lbl, mnGrp in (
  ("Internet", netmenu),
  ("Development", devmenu),
  ("Mediums", mmmenu),
  ("Games", gammenu),
  ("Config", configmenu),
  ("File System", toolsmenu),
  ("Admin Tools", adminmenu),
  ("Utilities", utilmenu)):
  appsmenu.add_cascade(label=lbl,menu=mnGrp)

appsmenu.add_separator()

# Menu
appsmenu.add_command(label="Edit Menu", command=lambda: runCommand("idle2.7" + " /usr/local/bin/tkRootMenu.py"))
appsmenu.add_command(label="Refresh Menu", command=runRfs)
appsmenu.add_command(label="Close Menu", command=root.quit)

appsmenu.add_separator()

# PC
for lbl, cmmnd in (
  ("Logout", "kill -15 -1"),
  ("Reboot", __sudo_cmd__ + " shutdown -r now"),
  ("Shutdown", __sudo_cmd__ + " shutdown -h now")):
  appsmenu.add_command(label=lbl,command=lambda param=cmmnd: runCommand(param))

root.config(menu=menubar)

if __name__ == "__main__":
  root.mainloop()
