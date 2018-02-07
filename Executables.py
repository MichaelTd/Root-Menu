__sudo_cmd__ = "SUDO_ASKPASS=`which x11-ssh-askpass||which ssh-askpass` sudo --login --askpass "
__terminal__ = "terminology"
__editor__ = "atom"
__file_manager__ = "gentoo"
__browser__ = "firefox"

__basic_apps__ = (
    ("Terminal", __terminal__, "ctl+t"),
    ("Editor", __editor__, "ctl+e"),
    ("File Manager", __file_manager__, "ctl+f"),
    ("Browser", __browser__, "ctl+b"))

__net_apps__ = (
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

__dev_apps__ = (
    ("Eclipse", "eclipse", "", 0),
    ("Netbeans", "netbeans", "", 0),
    ("KDevelop", "kdevelop", "", 0),
    ("QtCreator", "qtcreator.sh", "", 0),
    ("QtDesigner", "designer", "", 0),
    ("QtCreator", "qtcreator.sh", "", 0),
    ("Code Blocks", "codeblocks", "", 0),
    ("Glade", "glade", "", 0),
    ("Pg Admin3", "pgadmin3", "", 0),
    ("Scite", "scite", "", 0),
    ("Idle", "idle", "", 0),
    ("Diakonos", "diakonos", "", 1),
    ("Slap", "slap", "", 1),
    ("Micro", "micro", "", 1),
    ("Vim", "vim", "", 1),
    ("emacs-nox", "emacs", "-nw", 1),
    ("Mousepad", "mousepad", "", 0),
    ("Cuda Text", "cudatext", "", 0),
    ("NEdit", "nedit", "", 0),
    ("Tea", "tea", "", 0),
    ("Yudit", "yudit", "", 0),
    ("JuPyter", "jupyter", "notebook", 1),
    ("GVim", "gvim", "", 0),
    ("XEmacs", "xemacs", "", 0),
    ("Emacs", "emacs", "", 0),
    ("Geany", "geany", "", 0),
    ("Blue Fish", "bluefish", "", 0),
    ("ZED", "zed", "", 1),
    ("Just MarkDown", "justmd", "", 0),
    ("Komodo", "komodo", "", 0),
    ("Brackets", "brackets", "", 0),
    ("VSCode", "code", "", 0),
    ("VSCode", "vscode", "", 0),
    ("LightTable", "light", "", 0),
    ("LightTable", "lighttable", "", 0),
    ("Sublime Text", "sublime_text", "", 0),
    ("Atom", "atom", "", 0))

__media_apps__ = (
    ("Open Office", "ooffice", "", 0),
    ("Libre Office", "loffice", "", 0),
    ("Calcurse", "calcurse", "", 1),
    ("Abi Word", "abiword", "", 0),
    ("Scribus", "scribus", "", 0),
    ("Inkscape", "inkscape", "", 0),
    ("XFig", "xfig", "", 0),
    ("Dia", "dia", "", 0),
    ("GNU/Plot", "gnuplot", "", 1),
    ("FreeCAD", "freecad", "", 0),
    ("Open Shot", "openshot", "", 0),
    ("Blender", "blender", "", 0),
    ("XfBurn", "xfburn", "", 0),
    ("X CD Roast", "xcdroast", "", 0),
    ("Kodi", "kodi", "", 0),
    ("VLC", "vlc", "", 0),
    ("Dark Table", "darktable", "", 0),
    ("Gimp", "gimp", "", 0),
    ("Audacity", "audacity", "", 0),
    ("Audacious", "audacious", "", 0))

__game_apps__ = (
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

__fs_apps__ = (
    ("Terminology", "terminology", "", 0),
    ("CRT", "cool-retro-term", "", 0),
    ("Xfce4 Terminal", "xfce4-terminal", "--disable-server", 0),
    ("uRXVT", "urxvt", "", 0),
    ("uXTerm", "uxterm", "", 0),
    ("XTerm", "xterm", "", 0),
    ("Hyper", "hyper", "", 0),
    ("Midnight Commander", "mc", "-a", 1),
    ("Ranger", "ranger", "", 1),
    ("Rox filer", "rox", "", 0),
    ("ViFm", "vifm", "", 1),
    ("Gentoo", "gentoo", "", 0),
    ("Xfe", "xfe", "", 0),
    ("SpaceFM", "spacefm", "", 0),
    ("Thunar", "thunar", "", 0))

__shells__ = (
    ("bash", "bash", "", 1),
    ("KornSH", "ksh", "", 1),
    ("Zsh", "zsh", "", 1),
    ("Csh", "csh", "", 1),
    ("SH", "sh", "", 1),
    ("Fish", "fish", "", 1))

__admin_apps__ = (
    ("Terminal", __terminal__, "", 0),
    ("Text Editor", __editor__, "", 0),
    ("File manager", __file_manager__, "", 0),
    ("Midnight Commander", "mc", "-a", 1),
    ("Ranger", "ranger", "", 1),
    ("Porthole", "porthole", "", 0),
    ("Synaptic", "synaptic", "", 0),
    ("gtk PartEd", "gparted", "", 0),
    ("cli PartEd", "parted", "", 1),
    ("Wireshark", "wireshark", "", 0),
    ("DStat", "dstat", "-fcdngy", 1),
    ("C Sys Dig", "csysdig", "", 1),
    ("Glances", "glances", "", 1),
    ("PowerTop", "powertop", "", 1),
    ("HTop", "htop", "", 1),
    ("Top", "top", "", 1))

__util_apps__ = (
    ("App Runner", "/home/paperjam/bin/runcmd.sh", "", 1),
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
    ("jsCalculator", __browser__, "${HOME}/git/freeCodeCamp/01-front-end-cert/07-javascript-calculator/jc.html", 0))

__config_apps__ = (
    ("Compiz settings manager", "ccsm", "", 0),
    ("Emerald themes manager", "emerald-theme-manager", "", 0),
    ("Tint Wizard", "tintwizard", "", 0),
    ("Tint2 Config", "tint2conf", "", 0),
    ("OpenBox conf", "obconf", "", 0),
    ("e16 Keyedit", "e16keyedit", "", 0),
    ("e16 Menuedit", "e16menuedit2", "", 0),
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

__pc_options__ = (
    ("Logout", "kill", "-15 -1", 0, 0),
    ("Reboot", "shutdown", "-r now", 0, 1),
    ("Shutdown", "shutdown", "-h now", 0, 1))

__help__ = (
    ("e16 Docs", "edox", "", 0),
    ("Bash Documentation", __browser__ , "http://tldp.org/LDP/abs/html/", 0),
    ("Shared Docs", __browser__ , "file:///usr/share/doc/", 0),
    ("TiddlyWiki", __browser__, "file:///mnt/data/Documents/TiddlyWiki/TiddlyWiki.html", 0),
    ("TiddlyWiki5", __browser__, "file:///mnt/data/Documents/TiddlyWiki/TiddlyWiki5.html", 0),
    ("Git Root", __browser__, "file:///home/paperjam/git", 0),
    ("Docs Root", __browser__, "file:///mnt/data/Documents/docs/", 0))
