#!/usr/bin/python2
# A custom menu (tsouchlarakis@gmail.com)
# GNU/GPL https://www.gnu.org/licenses/gpl.html

import os
from Tkinter import *
#print os.name

__terminal__ = "terminology"
#__terminal__ = "xfce4-terminal --disable-server --geometry=120x40"
#__editor__ = "vscode"
#__editor__ = "sublime"
#__editor__ = "light"
__editor__ = "atom"
#__editor__ = "emacs"
#__editor__ = "gvim"
#__file_manager__ = "gentoo"
__file_manager__ = "xfe"
__browser__ = "firefox"
#__sudo_cmd__ = "SUDO_ASKPASS=/usr/bin/ssh-askpass-fullscreen &&sudo --askpass "
__sudo_cmd__ = "SUDO_ASKPASS=/usr/bin/x11-ssh-askpass &&sudo --askpass "

def runCommand(app):
  os.system(app + " &")


# Default Apps
def on_accel_runTerminal(widget):
  runCommand(__terminal__)
def on_accel_runEditor(widget):
  runCommand(__editor__)
def on_accel_runFileManager(widget):
  runCommand(__file_manager__)
def on_accel_runBrowser(widget):
  runCommand(__browser__)

# Menu
def runRfs():
  app = "/usr/local/bin/tkRootMenu.sh"
  print app
  runCommand(app)
  root.quit()

# Volume
def setVlm(widget):
    app = "amixer cset numid=3 " + str(v.get()) + "%"
    print app
    runCommand(app)

root = Tk()
root.title("Root Menu")
root.option_add('*resizable', TRUE)
root.geometry('110x75+0+0')

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

devmenu=Menu(menubar)
netmenu=Menu(menubar)
mmmenu=Menu(menubar)
gammenu=Menu(menubar)
configmenu=Menu(menubar)
utilmenu=Menu(menubar)
toolsmenu=Menu(menubar)
adminmenu=Menu(menubar)
appsmenu=Menu(menubar)

# Dev menu
for lbl, cmmnd in (("Eclipse", "runeclipse.sh"),
                  ("Netbeans", "netbeans"),
                  ("KDevelop", "kdevelop"),
                  ("QtCreator", "qtcreator.sh"),
                  ("QtDesigner", "qtchooser -run-tool=designer -qt=5"),
                  ("Glade", "glade"),
                  ("GVim", "gvim"),
                  ("Vim", __terminal__ + " -e vim"),
                  ("Diakonos", __terminal__ + " -e diakonos"),
                  ("Xemacs", __terminal__ + " -e xemacs"),
                  ("Emacs", "emacs"),
                  ("ZED", __terminal__ + " -e /bin/env /bin/bash ~/opt/zed/zed"),
                  ("Sublime Text", "sublime"),
                  ("LightTable", "light"),
                  ("Atom", "atom")):
  devmenu.add_command(label=lbl,command=lambda command=cmmnd: runCommand(command))

# Internet
for lbl, cmmnd in (("Firefox", "firefox"),
                  ("Firefox DE", "firefox-de"),
                  ("Mozilla", "mozilla"),
                  ("FileZilla", "filezilla"),
                  ("HexChat", "hexchat")):
  netmenu.add_command(label=lbl,command=lambda command=cmmnd: runCommand(command))

# Multimedia
for lbl, cmmnd in (("Gimp", "gimp"),
                  ("Open Shot", "openshot"),
                  ("Audacious", "audacious"),
                  ("VLC", "vlc"),
                  ("Open Office", "ooffice"),
                  ("Libre Office", "/opt/libreOffice"),
                  ("Foxit Reader", "~/bin/FoxitReader"),
                  ("Qpdf Viewer", "qpdfview"),
                  ("Ghost View", "gv")):
  mmmenu.add_command(label=lbl,command=lambda command=cmmnd: runCommand(command))

# Games menu
for lbl, cmmnd in (("Quake 3", "~/bin/ioq3"),
                  ("Quake 3 TA", "~/bin/ioq3-ta"),
                  ("Urban Terror", "~/bin/ut42u"),
                  ("Warsow", "~/warsow_21/warsow")):
  gammenu.add_command(label=lbl,command=lambda command=cmmnd: runCommand(command))

# Config Menu
for lbl, cmmnd in (("Compiz settings manager", "ccsm"),
                  ("Emerald themes manager", "emerald-theme-manager"),
                  ("Conky config", __editor__ + " ~/.conky.conf/.conkyrc.left ~/.conky.conf/.conkyrc.middle ~/.conky.conf/.conkyrc.right ~/.conky.conf/.conkyrc.lxde.my ~/.conky.conf/.conkyrc.right.full"),
                  ("Edit backup files", __editor__ + " ~/.backup.files.txt ~/.backup.themes.txt ~/.backup.git.txt"),
                  ("View Log files", __editor__ + " /var/log/update.perl.log /var/log/rsync.data.log /var/log/portage.emerge.log /var/log/backup-paperjam.log"),
                  ("X Screen Saver", "xscreensaver-demo"),
                  ("Alsamixer", __terminal__ + " -e alsamixer")):
  configmenu.add_command(label=lbl,command=lambda command=cmmnd: runCommand(command))

# Util Menu
for lbl, cmmnd in (("App Runner", "runcmd.sh"),
                  ("Xfce4 App Finder", "xfce4-appfinder -c --disable-server"),
                  ("Xarchiver", "xarchiver"),
                  ("PeaZip", "peazip"),
                  ("Viewnior", "viewnior"),
                  ("Xfce4 Screenshot", "xfce4-screenshooter"),
                  ("Take a shot now", "~/bin/imss.sh 2"),
                  ("Calculator", "calculator"),
                  ("jCalculator", "jCalculator.sh"),
                  ("Javascript Calculator", __browser__ + " ~/git/fcc-app/01-front-end-cert/07-javascript-calculator/jc.html")):
  utilmenu.add_command(label=lbl,command=lambda command=cmmnd: runCommand(command))

# File system tools
for lbl, cmmnd in (("Terminology", "terminology"),
                  ("Xfce4 Terminal", "xfce4-terminal --disable-server --geometry=120x40"),
                  ("URXVT", "urxvt"),
                  ("Midnight Commander", __terminal__ + " -e mc"),
                  ("Gentoo", "gentoo"),
                  ("Xfe", "xfe"),
                  ("Thunar", "thunar")):
  toolsmenu.add_command(label=lbl,command=lambda command=cmmnd: runCommand(command))

# Admin tools
for lbl, cmmnd in (("Terminal", __sudo_cmd__ + " " + __terminal__),
                  ("Text Editor", __sudo_cmd__ + " " + __editor__),
                  ("File manager", __sudo_cmd__ + " " + __terminal__ + " -e mc"),
                  ("Porthole", __sudo_cmd__ + " porthole"),
                  ("DStat", __sudo_cmd__ + " " + __terminal__ + " -e dstat -fcdngy"),
                  ("Glances", __sudo_cmd__ + " " + __terminal__ + " -e glances"),
                  ("PowerTop", __sudo_cmd__ + " " + __terminal__ + " -e powertop"),
                  ("HTop", __sudo_cmd__ + " " + __terminal__ + " -e htop"),
                  ("Top", __sudo_cmd__ + " " + __terminal__ + " -e top")):
  adminmenu.add_command(label=lbl,command=lambda command=cmmnd: runCommand(command))

menubar.add_cascade(label="Root Menu", menu=appsmenu)

# Basic apps
for lbl, cmmnd, k in (("Terminal", __terminal__, "ctl+t"),
                  ("Editor", __editor__, "ctl+e"),
                  ("File Manager", __file_manager__, "ctl+f"),
                  ("Browser", __browser__, "ctl+b")):
  appsmenu.add_command(label=lbl,command=lambda command=cmmnd: runCommand(command), accelerator=k)

appsmenu.add_separator()

# Groups
for lbl, mnGrp in (("Development", devmenu),
                  ("Internet", netmenu),
                  ("MultiMedia", mmmenu),
                  ("Games", gammenu),
                  ("Utilities", utilmenu),
                  ("Config", configmenu),
                  ("File Managers", toolsmenu),
                  ("Admin Tools", adminmenu)):
  appsmenu.add_cascade(label=lbl,menu=mnGrp)

appsmenu.add_separator()

# Menu
appsmenu.add_command(label="Edit Menu", command=lambda: runCommand(__editor__ + " " + "/usr/local/bin/tkRootMenu.py"))
appsmenu.add_command(label="Refresh Menu", command=runRfs)
appsmenu.add_command(label="Close Menu", command=root.quit)

appsmenu.add_separator()

# PC
for lbl, cmmnd in (("Logout", "kill -15 -1"),
                  ("Reboot", __sudo_cmd__ + " shutdown -r now"),
                  ("Shutdown", __sudo_cmd__ + " shutdown -h now")):
  appsmenu.add_command(label=lbl,command=lambda command=cmmnd: runCommand(command))

root.config(menu=menubar)

if __name__ == "__main__":
  root.mainloop()
