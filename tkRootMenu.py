#!/usr/bin/python2.7
# A custom menu (tsouchlarakis@gmail.com)
# GNU/GPL https://www.gnu.org/licenses/gpl.html
#

import os
from Tkinter import *
#print os.name

__terminal__ = "terminology"
#__terminal__ = "xfce4-terminal --disable-server --geometry=120x40"
#__editor__ = "sublime"
__editor__ = "light"
#__editor__ = "atom"
#__editor__ = "emacs"
#__editor__ = "gvim"
__file_manager__ = "gentoo"
__browser__ = "firefox"
#__sudo_cmd__ = "SUDO_ASKPASS=/usr/bin/ssh-askpass-fullscreen &&sudo --askpass "
__sudo_cmd__ = "SUDO_ASKPASS=/usr/bin/x11-ssh-askpass &&sudo --askpass "

def runCommand(app):
  os.system(app + " &")

# Default Apps
def runBrowser():
  app = __browser__
  print app
  runCommand(app)
def runTerminal():
  app = __terminal__
  print app
  runCommand(app)
def runFileManager():
  app = __file_manager__
  print app
  runCommand(app)
def runEditor():
  app = __editor__
  print app
  runCommand(app)

# Default Apps
def on_accel_runBrowser(widget):
  runBrowser()
def on_accel_runTerminal(widget):
  runTerminal()
def on_accel_runFileManager(widget):
  runFileManager()
def on_accel_runEditor(widget):
  runEditor()

# Menu
def runEdt():
  app = __editor__ + " " + "~/bin/appMenu.py"
  print app
  runCommand(app)
def runRfs():
  app = "/usr/local/bin/appMenu.py"
  print app
  runCommand(app)
  root.quit()

# Development
def runEclipse():
  app = "runeclipse.sh"
  print app
  runCommand(app)
def runNetbeans():
  app = "netbeans"
  print app
  runCommand(app)
def runKdev():
  app = "kdevelop"
  print app
  runCommand(app)
def runQtc():
  app = "qtcreator.sh"
  print app
  runCommand(app)
def runQtd():
  app = "qtchooser -run-tool=designer -qt=5"
  print app
  runCommand(app)
def runGld():
  app = "glade"
  print app
  runCommand(app)
def runGvim():
  app = "gvim"
  print app
  runCommand(app)
def runVim():
  app = __terminal__ + " -e vim"
  print app
  runCommand(app)
def runDkn():
  app = __terminal__ + " -e diakonos"
  print app
  runCommand(app)
def runEmacs():
  app = "emacs"
  print app
  runCommand(app)
def runXmcs():
  app = __terminal__ + " -e xemacs"
  print app
  runCommand(app)
def runSub():
  app = "sublime"
  print app
  runCommand(app)
def runZed():
  app = __terminal__ + " -e /bin/env /bin/bash ~/opt/zed/zed"
  print app
  runCommand(app)
def runLighttable():
  app = "light"
  print app
  runCommand(app)
def runAtom():
  app = "atom"
  print app
  runCommand(app)

# Internet
def runFirefox():
  app = "firefox"
  print app
  runCommand(app)
def runFfde():
  app = "firefox-de"
  print app
  runCommand(app)
def runMozilla():
  app = "mozilla"
  print app
  runCommand(app)
def runFzl():
  app = "filezilla"
  print app
  runCommand(app)
def runVivaldi():
  app = "vivaldi"
  print app
  runCommand(app)
def runHexchat():
  app = "hexchat"
  print app
  runCommand(app)
def runQbt():
  app = "qbittorrent"
  print app
  runCommand(app)
def runRtr():
  app = __terminal__ + " -e rtorrent"
  print app
  runCommand(app)

# Multimedia
def runGimp():
  app = "gimp"
  print app
  runCommand(app)
def runInk():
  app = "inkscape"
  print app
  runCommand(app)
def runOsht():
  app = "openshot"
  print app
  runCommand(app)
def runQiv():
  app = "qiviewer"
  print app
  runCommand(app)
def runVnr():
  app = "viewnior"
  print app
  runCommand(app)
def runAudacity():
  app = "audacity"
  print app
  runCommand(app)
def runAudacious():
  app = "audacious"
  print app
  runCommand(app)
def runSmplay():
  app = "smplayer"
  print app
  runCommand(app)
def runXine():
  app = "xine"
  print app
  runCommand(app)
def runVLC():
  app = "vlc"
  print app
  runCommand(app)

# Office
def runOoff():
  app = "ooffice"
  print app
  runCommand(app)
def runLoff():
  app = "/opt/libreOffice"
  print app
  runCommand(app)
def runLcd():
  app = "librecad"
  print app
  runCommand(app)
def runScrib():
  app = "scribus"
  print app
  runCommand(app)
def runFrd():
  app = "~/bin/FoxitReader"
  print app
  runCommand(app)
def runEvc():
  app = "evince"
  print app
  runCommand(app)
def runGvw():
  app = "gv"
  print app
  runCommand(app)
def runMpf():
  app = "mupdf"
  print app
  runCommand(app)
def runQpv():
  app = "qpdfview"
  print app
  runCommand(app)

# Games
def runQ3a():
  app = "~/bin/ioq3"
  print app
  runCommand(app)
def runQ3ta():
  app = "~/bin/ioq3-ta"
  print app
  runCommand(app)
def runUt():
  app = "~/bin/ut42u"
  print app
  runCommand(app)
def runWar():
  app = "~/warsow_21/warsow"
  print app
  runCommand(app)

# Configuration
def runCcsm():
  app = 'ccsm'
  print app
  runCommand(app)
def runETM():
  app = "emerald-theme-manager"
  print app
  runCommand(app)
def runCon():
  app = __editor__ + " ~/.conky.conf/.conkyrc.left ~/.conky.conf/.conkyrc.middle ~/.conky.conf/.conkyrc.right ~/.conky.conf/.conkyrc.lxde.my ~/.conky.conf/.conkyrc.right.full"
  print app
  runCommand(app)
def runEfb():
  app = __editor__ + " ~/.backup.files.txt ~/.backup.themes.txt ~/.backup.git.txt"
  print app
  runCommand(app)
def runVlg():
  app = __editor__ + " /var/log/update.perl.log /var/log/rsync.data.log /var/log/portage.emerge.log"
  print app
  runCommand(app)
def runXss():
  app = "xscreensaver-demo"
  print app
  runCommand(app)
def runAmix():
  app = __terminal__ + " -e alsamixer"
  print app
  runCommand(app)

# Utilities
def runXfa():
  app = "xfce4-appfinder -c --disable-server"
  print app
  runCommand(app)
def runRnc():
  app = "runcmd.sh"
  print app
  runCommand(app)
def runXar():
  app = "xarchiver"
  print app
  runCommand(app)
def runPzp():
  app = "peazip"
  print app
  runCommand(app)
def runXfs():
  app = "xfce4-screenshooter"
  print app
  runCommand(app)
def runSg():
  app = "screengrab"
  print app
  runCommand(app)
def runSbg():
  app = "shutterbug"
  print app
  runCommand(app)
def runTks():
  app = "~/bin/imss.sh 2"
  print app
  runCommand(app)
def runCalc():
  app= "calculator"
  print app
  runCommand(app)
def runJCalc():
  app= "jCalculator.sh"
  print app
  runCommand(app)
def runJsCalc():
  app= __browser__ + " ~/git/fcc-app/front-end-cert/Javascript-Calculator/jsCalc.html"
  print app
  runCommand(app)

  # File system tools
def runTerminology():
  app = "terminology"
  print app
  runCommand(app)
def runXfce4t():
  app = "xfce4-terminal --disable-server --geometry=120x40"
  print app
  runCommand(app)
def runRxvt():
  app = "urxvt"
  print app
  runCommand(app)
def runMc():
  app = __terminal__ + " -e mc"
  print app
  runCommand(app)
def runRng():
  app = __terminal__ + " -e ranger.py"
  print app
  runCommand(app)
def runThu():
  app = "thunar"
  print app
  runCommand(app)
def runXfe():
  app = "xfe"
  print app
  runCommand(app)
def runGentoo():
  app = "gentoo"
  print app
  runCommand(app)

# Administration
def runAterm():
  app = __sudo_cmd__ + " " + __terminal__
  print app
  runCommand(app)
def runAed():
  app = __sudo_cmd__ + " " + __editor__
  print app
  runCommand(app)
def runAfm():
  app = __sudo_cmd__ + " " + __terminal__ + " -e mc"
  print app
  runCommand(app)
def runPort():
  app = __sudo_cmd__ + " porthole"
  print app
  runCommand(app)
def runDstat():
  app = __sudo_cmd__ + " " + __terminal__ + " -e dstat -fcdngy"
  print app
  runCommand(app)
def runAgl():
  app = __sudo_cmd__ + " " + __terminal__ + " -e glances"
  print app
  runCommand(app)
def runApt():
  app = __sudo_cmd__ + " " + __terminal__ + " -e powertop"
  print app
  runCommand(app)
def runAht():
  app = __sudo_cmd__ + " " + __terminal__ + " -e htop"
  print app
  runCommand(app)
def runAtp():
  app = __sudo_cmd__ + " " + __terminal__ + " -e top"
  print app
  runCommand(app)

# Compiz
def runCfl():
  app = "python /mnt/ELEMENTS/Documents/work/python/appMenu/compizFlipper.py"
  print app
  runCommand(app)
def runFlf():
  app = "xdotool key 'ctrl+alt+Left'"
  print app
  runCommand(app)
def runFrg():
    app = "xdotool key 'ctrl+alt+Right'"
    print app
    runCommand(app)

# PC
def runLogout():
  app = "kill -15 -1"
  print app
  runCommand(app)
def runReboot():
  app = __sudo_cmd__ + " shutdown -r now"
  print app
  runCommand(app)
def runShutdown():
  app = __sudo_cmd__ + " shutdown -h now"
  print app
  runCommand(app)

def setVlm(widget):
    app = "amixer cset numid=3 " + str(v.get()) + "%"
    print app
    runCommand(app)

root = Tk()
root.title("Root Menu")
#root.option_add('*tearOff', FALSE)
root.option_add('*resizable', TRUE)
root.geometry('110x75+0+0')
#root.minsize(width=120,height=40)
#root.maxsize(width=120,height=40)
#text=Text(root,width=400,height=400)
#text.pack()

r = Button(root, text=">>", width=10, command=runFrg)
l = Button(root, text="<<", width=10, command=runFlf)
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

menubar=Menu(root)

devmenu=Menu(menubar)
netmenu=Menu(menubar)
mmmenu=Menu(menubar)
#graphmenu=Menu(menubar)
#offmenu=Menu(menubar)
gammenu=Menu(menubar)
configmenu=Menu(menubar)
utilmenu=Menu(menubar)
toolsmenu=Menu(menubar)
adminmenu=Menu(menubar)
appsmenu=Menu(menubar)

devmenu.add_command(label="Eclipse", command=runEclipse)
devmenu.add_command(label="Netbeans", command=runNetbeans)
devmenu.add_command(label="KDevelop", command=runKdev)
devmenu.add_command(label="QtCreator", command=runQtc)
devmenu.add_command(label="QtDesigner",command=runQtd)
devmenu.add_command(label="Glade", command=runGld)
devmenu.add_command(label="GVim", command=runGvim)
devmenu.add_command(label="Vim", command=runVim)
devmenu.add_command(label="Diakonos", command=runDkn)
devmenu.add_command(label="Xemacs", command=runXmcs)
devmenu.add_command(label="Emacs", command=runEmacs)
devmenu.add_command(label="ZED", command=runZed)
devmenu.add_command(label="Sublime Text", command=runSub)
devmenu.add_command(label="LightTable", command=runLighttable)
devmenu.add_command(label="Atom", command=runAtom)

netmenu.add_command(label="Firefox", command=runFirefox)
netmenu.add_command(label="Firefox DE", command=runFfde)
netmenu.add_command(label="Mozilla", command=runMozilla)
netmenu.add_command(label="FileZilla", command=runFzl)
#netmenu.add_command(label="Vivaldi", command=runVivaldi)
netmenu.add_command(label="HexChat", command=runHexchat)
#netmenu.add_command(label="QbitTorrent", command=runQbt)
#netmenu.add_command(label="rTorrent", command=runRtr)

mmmenu.add_command(label="Gimp", command=runGimp)
#mmmenu.add_command(label="Inkscape", command=runInk)
mmmenu.add_command(label="Open Shot", command=runOsht)
#mmmenu.add_command(label="Audacity", command=runAudacity)
mmmenu.add_command(label="Audacious", command=runAudacious)
#mmmenu.add_command(label="SmPlayer", command=runSmplay)
#mmmenu.add_command(label="Xine", command=runXine)
mmmenu.add_command(label="VLC", command=runVLC)
mmmenu.add_command(label="Open Office", command=runOoff)
mmmenu.add_command(label="Libre Office", command=runLoff)
#mmmenu.add_command(label="LibreCAD", command=runLcd)
#mmmenu.add_command(label="Scribus", command=runScrib)
mmmenu.add_command(label="Foxit Reader", command=runFrd)
#mmmenu.add_command(label="Evince", command=runEvc)
mmmenu.add_command(label="Qpdf Viewer", command=runQpv)
#mmmenu.add_command(label="Mupdf Viewer", command=runMpf)
mmmenu.add_command(label="Ghost View", command=runGvw)

gammenu.add_command(label="Quake 3", command=runQ3a)
gammenu.add_command(label="Quake 3 TA", command=runQ3ta)
gammenu.add_command(label="Urban Terror", command=runUt)
gammenu.add_command(label="Warsow", command=runWar)

configmenu.add_command(label="Compiz settings manager", command=runCcsm)
configmenu.add_command(label="Emerald themes manager", command=runETM)
configmenu.add_command(label="Conky config", command=runCon)
configmenu.add_command(label="Edit backup files", command=runEfb)
configmenu.add_command(label="View Log files", command=runVlg)
configmenu.add_command(label="X Screen Saver", command=runXss)
configmenu.add_command(label="Alsamixer", command=runAmix)

utilmenu.add_command(label="App Runner", command=runRnc)
utilmenu.add_command(label="Xfce4 App Finder", command=runXfa)
utilmenu.add_command(label="Xarchiver", command=runXar)
utilmenu.add_command(label="PeaZip", command=runPzp)
utilmenu.add_command(label="Viewnior", command=runVnr)
#utilmenu.add_command(label="Qiviewer", command=runQiv)
utilmenu.add_command(label="Xfce4 Screenshot", command=runXfs)
#utilmenu.add_command(label="Screen Grab", command=runSg)
#utilmenu.add_command(label="ShutterBug", command=runSbg)
utilmenu.add_command(label="Take a shot now", command=runTks)
utilmenu.add_command(label="Calculator", command=runCalc)
utilmenu.add_command(label="jCalculator", command=runJCalc)
utilmenu.add_command(label="jsCalc", command=runJsCalc)

toolsmenu.add_command(label="Terminology", command=runTerminology)
toolsmenu.add_command(label="Xfce4 Terminal", command=runXfce4t)
toolsmenu.add_command(label="URXVT", command=runRxvt)
toolsmenu.add_command(label="Midnight Commander", command=runMc)
#toolsmenu.add_command(label="Ranger", command=runRng)
toolsmenu.add_command(label="Gentoo", command=runGentoo)
toolsmenu.add_command(label="Xfe", command=runXfe)
toolsmenu.add_command(label="Thunar", command=runThu)

adminmenu.add_command(label="Terminal", command=runAterm)
adminmenu.add_command(label="Text Editor", command=runAed)
adminmenu.add_command(label="File manager", command=runAfm)
adminmenu.add_command(label="Porthole", command=runPort)
adminmenu.add_command(label="DStat", command=runDstat)
adminmenu.add_command(label="Glances", command=runAgl)
adminmenu.add_command(label="PowerTop", command=runApt)
adminmenu.add_command(label="HTop", command=runAht)
adminmenu.add_command(label="Top", command=runAtp)

menubar.add_cascade(label="Root Menu", menu=appsmenu)

appsmenu.add_command(label="Terminal", command=runTerminal, accelerator="Ctrl+T")
appsmenu.add_command(label="Editor", command=runEditor, accelerator="Ctrl+E")
appsmenu.add_command(label="File Manager", command=runFileManager, accelerator="Ctrl+F")
appsmenu.add_command(label="Browser", command=runBrowser, accelerator="Ctrl+B")
appsmenu.add_separator()
appsmenu.add_cascade(label="Development", menu=devmenu)
appsmenu.add_cascade(label="Internet", menu=netmenu)
appsmenu.add_cascade(label="MultiMedia", menu=mmmenu)
#appsmenu.add_cascade(label="Office", menu=offmenu)
appsmenu.add_cascade(label="Games", menu=gammenu)
appsmenu.add_cascade(label="Config", menu=configmenu)
appsmenu.add_cascade(label="Utilities", menu=utilmenu)
appsmenu.add_cascade(label="File Managers", menu=toolsmenu)
appsmenu.add_cascade(label="Admin Tools", menu=adminmenu)
#appsmenu.add_separator()
#appsmenu.add_command(label="Compiz Flipper", command=runCfl)
#appsmenu.add_command(label="Flip Right", command=runFrg)
#appsmenu.add_command(label="Flip Left", command=runFlf)
appsmenu.add_separator()
appsmenu.add_command(label="Edit Menu", command=runEdt)
appsmenu.add_command(label="Refresh Menu", command=runRfs)
appsmenu.add_command(label="Close Menu", command=root.quit)
appsmenu.add_separator()
appsmenu.add_command(label="Logout", command=runLogout)
appsmenu.add_command(label="Reboot", command=runReboot)
appsmenu.add_command(label="Shutdown", command=runShutdown)

root.config(menu=menubar)

if __name__ == "__main__":
  root.mainloop()
