__sudo_cmd__ = "SUDO_ASKPASS=`which x11-ssh-askpass||which ssh-askpass` sudo --login --askpass "
__terminal__ = "terminology"
__editor__ = "emacs"
__file_manager__ = "gentoo"
__browser__ = "firefox"

__basic__ = (
    ("Terminal", __terminal__, "ctl+t"),
    ("Browser", __browser__, "ctl+b"),
    ("Editor", __editor__, "ctl+e"),
    ("File Manager", __file_manager__, "ctl+f"))

__net__ = (
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
    ("Discord", "discord", "", 0),
    ("Skype", "skype", "", 0),
    ("Zoom", "zoom", "", 0),
    ("Quassel IRC", "quassel", "", 0),
    ("HexChat IRC", "hexchat", "", 0))

__dev__ = (
    ("Eclipse", "eclipse", "", 0), # Java Based
    ("Netbeans", "netbeans", "", 0),
    ("KDevelop", "kdevelop", "", 0), # c/cpp based
    ("QtCreator", "qtcreator", "", 0),
    ("QtDesigner", "designer", "", 0),
    ("QtCreator", "qtcreator.sh", "", 0),
    ("Code Blocks", "codeblocks", "", 0),
    ("Glade", "glade", "", 0),
    ("Pg Admin3", "pgadmin3", "", 0),
    ("Mousepad", "mousepad", "", 0), 
    ("Geany", "geany", "", 0),
    ("Blue Fish", "bluefish", "", 0),
    ("Tea", "tea", "", 0),
    ("Yudit", "yudit", "", 0),
    ("NEdit", "nedit", "", 0), # Motif
    ("Scite", "scite", "", 0), # Python based
    ("Idle", "idle", "", 0),
    ("JuPyter", "jupyter", "notebook", 1),
    ("Anaconda3", "anaconda-navigator", "", 0),
    ("Cuda Text", "cudatext", "", 0),
    ("Diakonos", "diakonos", "", 1), # CLI based
    ("Micro", "micro", "", 1),
    ("Kakoune", "kak", "", 1),
    ("Vim", "vim", "", 1), # Traditional
    ("emacs-nox", "emacs", "-nw", 1),
    ("GVim", "gvim", "", 0),
    ("XEmacs", "xemacs", "", 0),
    ("Emacs", "emacs", "", 0),
    ("ZED", "/home/paperjam/opt/zed/zed", "", 0), # JavaSctip Based
    ("Slap", "slap", "", 1),
    ("Just MarkDown", "justmd", "", 0),
    ("Komodo", "komodo", "", 0),
    ("Brackets", "brackets", "", 0),
    ("VSCode", "code", "", 0),
    ("VSCode", "vscode", "", 0),
    ("LightTable", "light", "", 0),
    ("LightTable", "lighttable", "", 0),
    ("Sublime Text", "sublime_text", "", 0),
    ("Atom", "atom", "", 0))

__media__ = (
    ("Open Office", "ooffice", "", 0), # Office
    ("Libre Office", "loffice", "", 0),
    ("Calcurse", "calcurse", "", 1),
    ("Abi Word", "abiword", "", 0),
    ("DjVuSmooth", "djvusmooth", "", 0), # DjVu files
    ("Scribus", "scribus", "", 0),
    ("Inkscape", "inkscape", "", 0),
    ("XFig", "xfig", "", 0),
    ("Dia", "dia", "", 0),
    ("GNU/Plot", "gnuplot", "", 1),
    ("FreeCAD", "freecad", "", 0),
    ("Blender", "blender", "", 0),
    ("XfBurn", "xfburn", "", 0),    # DVD/CD Burn
    ("X CD Roast", "xcdroast", "", 0),
    ("ACiDRip", "acidrip", "", 0),
    ("HandBrake", "ghb", "", 0),
    ("OBS Studio", "obs", "", 0), # Video broadcast
    ("Open Shot", "openshot", "", 0), # Video edit
    ("Kodi", "kodi", "", 0),    # Video Playback
    ("VLC", "vlc", "", 0),
    ("Dark Table", "darktable", "", 0), # Image Edit
    ("Gimp", "gimp", "", 0),
    ("Muse Score", "musescore", "", 0), # Sound
    ("Audacity", "audacity", "", 0),
    ("Audacious", "audacious", "", 0))

__games__ = (
    ("GTypist", "gtypist", "", 1), # Touch Typing
    ("KLavaro", "klavaro", "", 0),
    ("Lutris", "lutris", "", 0), 
    ("Gx Mame", "gxmame", "", 0), # MAME
    ("Advanced Mame Menu", "advmenu", "", 0),
    ("Snake 3D", "snake3d", "", 0), # Board
    ("Gnake", "gnake", "", 1),
    ("MyMan", "xterm", "-g 80x35 -e /home/paperjam/opt/myman-wip-2009-10-30/myman", 0),
    ("MSnake", "xterm", "-g 80x35 -e /home/paperjam/git/msnake/build/msnake", 0),
    ("GNUbg", "gnubg", "", 0),
    ("XGammon", "xgammon", "", 0),
    ("XBoard", "xboard", "", 0),
    ("ChessX", "chessx", "", 0),
    ("Xmahjongg","xmahjongg", "", 0),
    ("X Mah-jongg","xmj", "", 0),
    ("Quake 3", "ioq3", "", 1), # 3D
    ("Quake 3 TA", "ioq3-ta", "", 1),
    ("Urban Terror", "Quake3-UrT.x86_64", "", 1),
    ("Warsow", "warsow", "", 1))

__fs__ = (
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

__admin__ = (
    ("Terminal", __terminal__, "", 0),
    ("Terminology", "terminology", "", 0),
    ("Text Editor", __editor__, "", 0),
    ("Atom", "atom", "", 0),
    ("File manager", __file_manager__, "", 0),
    ("Xfe", "xfe", "--root-ok", 0),
    ("Midnight Commander", "mc", "-a", 1),
    ("Ranger", "ranger", "", 1),
    ("Porthole", "porthole", "", 0),
    ("Synaptic", "synaptic", "", 0),
    ("gtk PartEd", "gparted", "", 0),
    ("cli PartEd", "parted", "", 1),
    ("Wireshark", "wireshark", "", 0),
    ("ZenMap", "zenmap", "", 0),
    ("DStat", "dstat", "-fcdngy", 1),
    ("C Sys Dig", "csysdig", "", 1),
    ("Glances", "glances", "", 1),
    ("PowerTop", "powertop", "", 1),
    ("HTop", "htop", "", 1),
    ("Top", "top", "", 1))

__utils__ = (
    ("App Runner", "/home/paperjam/bin/runcmd.sh", "", 1), # App finders
    ("Xfce4 App Finder", "xfce4-appfinder", "--collapsed --disable-server", 0),
    ("Synapse", "synapse", "", 0),
    ("Xfce4 Screenshot", "xfce4-screenshooter", "", 0), # Image capture
    ("Screengrab", "screengrab", "", 0),
    ("Shutter","shutter", "", 0),
    ("Take a shot now", "imss.sh", "2", 0),
    ("Simple Screen Recorder", "simplescreenrecorder", "", 0), # Video capture
    ("Viewnior", "viewnior", "", 0), # Image Viewers
    ("Ristretto", "ristretto", "", 0),
    ("PeaZip", "peazip", "", 0), # Compression
    ("Xarchiver", "xarchiver", "", 0),
    ("GNU Privacy Assistant", "gpa", "", 0), # PGP
    ("Foxit Reader", "foxitreader", "", 0), # PDF
    ("QPdf View", "qpdfview", "", 0),
    ("Evince", "evince", "", 0),
    ("XPdf", "xpdf", "", 0),
    ("Ghost View", "gv", "", 0),
    ("Xv", "xv", "", 0),
    ("DjView", "djview", "", 0), # DjVu
    ("Fox Calc","calculator", "", 0), # Calc
    ("XCalc","xcalc", "", 0),
    ("Calcoo","calcoo", "", 0),
    ("BC", "bc", "", 1),
    ("Term Calc", "calc", "", 1),
    ("jCalc", "java", "-jar ~/bin/jCalc.jar", 0),
    ("jsCalculator", __browser__, "${HOME}/git/freeCodeCamp/01-front-end-cert/07-javascript-calculator/jc.html", 0))

__config__ = (
    ("Compiz settings manager", "ccsm", "", 0), # Compiz
    ("Emerald themes manager", "emerald-theme-manager", "", 0),
    ("Tint Wizard", "tintwizard", "", 0), # Tint
    ("Tint2 Config", "tint2conf", "", 0),
    ("OpenBox conf", "obconf", "", 0), # Openbox
    ("e16 Keyedit", "e16keyedit", "", 0), # e16
    ("e16 Menuedit", "e16menuedit2", "", 0),
    ("Qt Config", "qtconfig", "", 0), # Qt
    ("X Screen Saver", "xscreensaver-demo", "", 0), # XScreenSaver
    ("Wicd gtk", "wicd-gtk", "", 0), # Network
    ("Wicd curses", "wicd-curses", "", 1),
    ("Xfce4-alsa-control", "xfce4-alsa-control", "", 0), # Sound
    ("Alsamixer Gui", "alsamixergui", "", 0),
    ("Alsamixer", "alsamixer", "", 1),
    ("Xfce4 Mixer", "xfce4-mixer", "", 0),
    ("Volume Prefs", "paprefs", "", 0),
    ("Volume Controls", "pavucontrol", "-t 3", 0))

__pc_options__ = (
    ("Logout", "kill", "-15 -1", 1, 0),
    ("Reboot", "shutdown", "-r now", 0, 1),
    ("Shutdown", "shutdown", "-h now", 0, 1))

__help__ = (
    ("e16 Docs", "edox", "", 0),
    ("Bash Documentation", __browser__ , "http://tldp.org/LDP/abs/html/", 0),
    ("Shared Docs", __browser__ , "file:///usr/share/doc/", 0),
    ("TiddlyWiki", __browser__, "file:///mnt/data/Documents/TiddlyWiki/TiddlyWiki.html", 0),
    ("Git Root", __browser__, "file:///home/paperjam/git", 0),
    ("Docs Root", __browser__, "file:///mnt/data/Documents/DOCS/", 0))
