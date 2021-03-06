__sudo_cmd__ = "SUDO_ASKPASS=$(which x11-ssh-askpass||which ssh-askpass-fullscreen) sudo --login --askpass "
__terminal__ = "terminology"
__editor__ = "mxcl"
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
    ("Chromium", "chromium", "", 0),
    ("Google chrome", "google-chrome-stable", "", 0),
    ("Seamonkey", "seamonkey", "", 0),
    ("PaleMoon", "palemoon", "", 0),
    ("Opera","opera", "", 0),
    ("Seamonkey Mail", "seamonkey", "-mail", 0),
    ("Pidgin", "pidgin", "", 0),
    ("FileZilla", "filezilla", "", 0),
    ("puTTY", "putty", "", 0),
    ("Midori", "midori", "", 0),
    ("W3m", "w3m", "-v", 1),
    ("Lynx", "lynx", "", 1),
    ("Discord", "discord", "", 0),
    ("Skype", "skypeforlinux", "", 0),
    ("Zoom", "zoom", "", 0),
    ("Zoom", "/home/paperjam/opt/zoom/zoom.sh", "", 1),
    ("Quassel IRC", "quassel", "", 0),
    ("HexChat IRC", "hexchat", "", 0))

__dev__ = (
    ("Eclipse", "eclipse", "", 0),
    ("Netbeans", "netbeans", "", 0),
    ("KDevelop", "kdevelop", "", 0), # c/cpp based
    ("QtCreator", "qtcreator", "", 0),
    ("QtDesigner", "designer", "", 0),
    ("Glade", "glade", "", 0),
    ("Fltk", "fluid", "", 0),
    ("Code Blocks", "codeblocks", "", 0),
    ("Code Lite", "codelite", "", 0),
    ("Geany", "geany", "", 0),
    ("Yudit", "yudit", "", 0),
    ("NEdit", "nedit", "", 0), # Motif
    ("wxHexEditor", "wxHexEditor", "", 0), # Hex
    ("fpc Lazarus", "lazarus", "", 1),
    ("DrRacket", "drracket", "", 0), # lisp-scheme-racket
    ("Pharo", "pharo", "", 1),
    ("LiveCode", "livecodecommunity", "", 0),
    ("squirrelsql", "/home/paperjam/opt/squirrelsql/squirrel-sql.sh", "", 0), # SQL
    ("Argo UML", "argouml.sh", "", 1),
    ("Scite", "scite", "", 0), # Python based
    ("Idle", "idle", "", 0),
    ("JuPyter", "jupyter", "notebook", 1),
    ("Anaconda3", "conda-env.sh", "", 1),
    ("GVim", "gvim", "", 0),
    ("emacs", "emacs", "", 0), # Emacs
    ("emacsnox", "emacs", "-nw", 1),
    ("emacsclient", "emacsclient", "-c", 0),
    ("VSCodium", "codium", "", 0),
    ("Atom", "atom", "", 0))

__media__ = (
    ("Open Office", "ooffice", "", 0), # Office
    ("Libre Office", "loffice", "", 0),
    ("freeOffice text", "textmaker18free", "", 0),
    ("freeOffice calc", "planmaker18free", "", 0),
    ("freeOffice present", "presentations18free", "", 0),
    ("Calcurse", "calcurse", "", 1),
    ("Spredsheet Calculator Improvised", "sc-im", "", 1),
    ("Abi Word", "abiword", "", 0),
    ("GNU/Octave", "octave", "", 0), # Sci Math
    ("GNU/Plot", "gnuplot", "", 1),
    ("maxima", "maxima", "", 1),
    ("wxMaxima", "wxmaxima", "", 0),
    ("Dia", "dia", "", 0),
    ("Fade In", "fadein", "", 0), # Script
    ("DjVuSmooth", "djvusmooth", "", 0), # DjVu files
    ("Scribus", "scribus", "", 0),
    ("Inkscape", "inkscape", "", 0),
    ("XFig", "xfig", "", 0),
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
    ("ncmpcpp", "ncmpcpp", "", 1),
    ("Audacity", "audacity", "", 0),
    ("Qmmp", "qmmp", "", 0),
    ("Audacious", "audacious", "", 0))

__games__ = (
    ("GTypist", "gtypist", "", 1), # Touch Typing
    ("KLavaro", "klavaro", "", 0),
    ("Lutris", "lutris", "", 0),
    ("Gx Mame", "gxmame", "", 0), # MAME
    ("Advanced Mame Menu", "advmenu", "", 0),
    ("Snake 3D", "snake3d", "", 0), # Board
    ("Gnake", "gnake", "", 1),
    ("GNUbg", "gnubg", "", 0),
    ("XGammon", "xgammon", "", 0),
    ("XBoard", "xboard", "", 0),
    ("EBoard", "eboard", "", 0),
    ("ChessX", "chessx", "", 0),
    ("Xmahjongg","xmahjongg", "", 0),
    ("X Mah-jongg","xmj", "", 0),
    ("Super Tux Kart", "supertuxkart", "", 1), # 3D
    ("torcs", "torcs", "", 1), #
    ("Quake 3", "ioquake3", "", 1),
    ("Quake 3 TA", "ioquake3-ta", "", 1),
    ("NexUiz", "nexuiz", "", 1),
    ("Xonotic", "xonotic", "", 1),
    ("Urban Terror", "Quake3-UrT.x86_64", "", 1),
    ("warsow", "warsow", "", 1))

__fs__ = (
    ("Midnight Commander", "mc", "-a", 1),
    ("Ranger", "ranger", "", 1),
    ("Rox filer", "rox", "", 0),
    ("ViFm", "vifm", "", 1),
    ("Gentoo", "gentoo", "", 0),
    ("Xfe", "xfe", "", 0),
    ("Double Commander", "doublecmd", "", 0),
    ("SpaceFM", "spacefm", "", 0),
    ("Thunar", "thunar", "", 0),
    ("Terminology", "terminology", "", 0),
    ("CRT", "cool-retro-term", "", 0),
    ("Xfce4 Terminal", "xfce4-terminal", "--disable-server", 0),
    ("URXvt", "urxvt", "-depth 32 -bg rgba:0000/0000/0000/aaaa", 0),
    ("XTerm", "xterm", "", 0),
    ("Hyper", "hyper", "", 0),
    ("QTerminal", "qterminal", "", 0),
    ("Sakura", "sakura", "", 0),
    ("bash", "bash", "", 1),
    ("KornSH", "ksh", "", 1),
    ("Zsh", "zsh", "", 1),
    ("Csh", "csh", "", 1),
    ("SH", "sh", "", 1),
    ("dash", "dash", "", 1),
    ("yash", "yash", "", 1),
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
    ("rofi", "rofi", "-show run", 0),
    ("Synapse", "synapse", "", 0),
    ("Xfce4 Screenshot", "xfce4-screenshooter", "", 0), # Image capture
    ("Screengrab", "screengrab", "", 0),
    ("Shutter","shutter", "", 0),
    ("X Snap","xsnap", "", 0),
    ("Take a shot now", "imss.sh", "2", 0),
    ("Simple Screen Recorder", "simplescreenrecorder", "", 0), # Video capture
    ("Viewnior", "viewnior", "", 0), # Image Viewers
    ("Ristretto", "ristretto", "", 0),
    ("Eye of Gnome", "eog", "", 0),
    ("PeaZip", "peazip", "", 0), # Compression
    ("Xarchiver", "xarchiver", "", 0),
    ("GNU Privacy Assistant", "gpa", "", 0), # PGP
    ("keepassxc", "keepassxc", "", 0),
    ("bashpass.sh", "bp-launch.sh", "tdm.db3", 0),
    ("Foxit Reader", "foxitreader", "", 0), # PDF
    ("FBreader", "fbreader", "", 0),
    ("QPdf View", "qpdfview", "", 0),
    ("Evince", "evince", "", 0),
    ("XPdf", "xpdf", "", 0),
    ("Ghost View", "gv", "", 0),
    ("Xv", "xv", "", 0),
    ("DjView", "djview", "", 0), # DjVu
    ("Fox Calc","calculator", "", 0), # Calc
    ("Galculator","galculator", "", 0),
    ("XCalc","xcalc", "", 0),
    ("Calcoo","calcoo", "", 0),
    ("BC", "bc", "", 1),
    ("Term Calc", "calc", "", 1),
    ("jCalc", "java", "-jar ~/bin/jCalc.jar", 0),
    ("jsCalculator", __browser__, "${HOME}/git/freeCodeCamp/01-front-end-cert/07-javascript-calculator/jc.html", 0))

__config__ = (
    ("Compiz settings manager", "ccsm", "", 0), # Compiz
    ("Emerald themes manager", "emerald-theme-manager", "", 0),
    ("xfce4-appearance-settings", "xfce4-appearance-settings", "", 0),
    ("Tint Wizard", "tintwizard", "", 0), # Tint
    ("Tint2 Config", "tint2conf", "", 0),
    ("OpenBox conf", "obconf", "", 0), # Openbox
    ("e16 Keyedit", "e16keyedit", "", 0), # e16
    ("e16 Menuedit", "e16menuedit2", "", 0),
    ("Qt Config", "qtconfig", "", 0), # Qt
    ("Qt 5 Config", "qt5ct", "", 0), # Qt
    ("X Screen Saver", "xscreensaver-demo", "", 0), # XScreenSaver
    ("X Screen Saver lockscreen", "xscreensaver-command", "-lock", 0), # XScreenSaver lock
    ("Wicd gtk", "wicd-gtk", "", 0), # Network
    ("Wicd curses", "wicd-curses", "", 1),
    ("Xfce4-alsa-control", "xfce4-alsa-control", "", 0), # Sound
    ("Alsamixer Gui", "alsamixergui", "", 0),
    ("Alsamixer", "alsamixer", "", 1),
    ("Xfce4 Mixer", "xfce4-mixer", "", 0),
    ("Volume Prefs", "paprefs", "", 0),
    ("Volume Controls", "pavucontrol", "-t 3", 0))

__help__ = (
    ("e16 Docs", "edox", "", 0),
    ("Bash Documentation", __browser__ , "http://tldp.org/LDP/abs/html/", 0),
    ("Shared Docs", __browser__ , "file:///usr/share/doc/", 0),
    ("TiddlyWiki", __browser__, "file:///mnt/data/Documents/TiddlyWiki/TiddlyWiki.html", 0),
    ("Git Root", __browser__, "file:///home/paperjam/git", 0),
    ("Docs Root", __browser__, "file:///mnt/data/Documents/DOCS/", 0))

__pc_options__ = (
    ("Logout", "kill", "-15 -1", 1, 0),
    ("Reboot", "shutdown", "-r now", 1, 1),
    ("Shutdown", "shutdown", "-h now", 1, 1))
