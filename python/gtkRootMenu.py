#!/usr/bin/python2

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import os

__terminal__ = "terminology"
__editor__ = "atom"
__file_manager__ = "xfe"
__browser__ = "firefox"
__sudo_cmd__ = "SUDO_ASKPASS=/usr/bin/x11-ssh-askpass &&sudo --askpass "
#__sudo_cmd__ = "SUDO_ASKPASS=/usr/bin/ssh-askpass-fullscreen &&sudo --askpass "
#__sudo_cmd__ = "sudo --askpass "
# Get stuff done
def runCommand(app):
  os.system(app + " &")
# Compiz
def runFlf(wdgt):
  app = "xdotool key 'ctrl+alt+Left'"
  print (app)
  runCommand(app)
def runFrg(wdgt):
  app = "xdotool key 'ctrl+alt+Right'"
  print (app)
  runCommand(app)
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

UI_INFO = """
<ui>
  <menubar name='MenuBar'>
    <menu action='FileMenu'>
      <menu action='FileNew'>
        <menuitem action='FileNewStandard' />
        <menuitem action='FileNewFoo' />
        <menuitem action='FileNewGoo' />
      </menu>
      <separator />
      <menuitem action='FileQuit' />
    </menu>
    <menu action='EditMenu'>
      <menuitem action='EditCopy' />
      <menuitem action='EditPaste' />
      <menuitem action='EditSomething' />
    </menu>
    <menu action='RootMenu'>
      <menuitem action='Browse' />
      <menuitem action='Term' />
      <menuitem action='FM' />
      <menuitem action='Editor' />
      <menu action='Dev'>
        <menuitem action='Editor' />
      </menu>
      <menu action='Internet'>
        <menuitem action='Firefox' />
      </menu>
      <menu action='Multimedia'>
        <menuitem action='VLC' />
      </menu>
      <menu action='Games'>
        <menuitem action='FileNewStandard' />
      </menu>
      <menu action='Config'>
        <menuitem action='FileNewStandard' />
      </menu>
      <menu action='Utilities'>
        <menuitem action='Term' />
      </menu>
      <menu action='File Tools'>
        <menuitem action='FM' />
      </menu>
      <menu action='Admin Tools'>
        <menuitem action='Term' />
      </menu>
    </menu>
    <menu action='ChoicesMenu'>
      <menuitem action='ChoiceOne'/>
      <menuitem action='ChoiceTwo'/>
      <separator />
      <menuitem action='ChoiceThree'/>
    </menu>
  </menubar>
  <toolbar name='ToolBar'>
    <toolitem action='FileNewStandard' />
    <toolitem action='FileQuit' />
  </toolbar>
  <popup name='PopupMenu'>
    <menuitem action='EditCopy' />
    <menuitem action='EditPaste' />
    <menuitem action='EditSomething' />
  </popup>
</ui>
"""

class MenuExampleWindow(Gtk.Window):

  def __init__(self):
    Gtk.Window.__init__(self, title="Root Menu")

    #self.set_default_size(200, 200)

    action_group = Gtk.ActionGroup("my_actions")

    self.add_file_menu_actions(action_group)
    self.add_edit_menu_actions(action_group)
    self.add_root_menu_actions(action_group)
    #self.add_choices_menu_actions(action_group)

    uimanager = self.create_ui_manager()
    uimanager.insert_action_group(action_group)

    menubar = uimanager.get_widget("/MenuBar")

    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    box.pack_start(menubar, False, False, 0)

    #toolbar = uimanager.get_widget("/ToolBar")
    #box.pack_start(toolbar, False, False, 0)

    eventbox = Gtk.EventBox()
    eventbox.connect("button-press-event", self.on_button_press_event)
    box.pack_start(eventbox, True, True, 0)

    #label = Gtk.Label("Right-click to see the popup menu.")
    #eventbox.add(label)

    #self.popup = uimanager.get_widget("/PopupMenu")

#
    #self.set_border_width(10)

    #hbox = Gtk.Box(spacing=6)
    #self.add(hbox)

    button = Gtk.Button.new_with_mnemonic("Flip _Right")
    button.connect("clicked", runFrg)
    box.pack_start(button, True, True, 0)

    button = Gtk.Button.new_with_mnemonic("Flip L_eft")
    button.connect("clicked", runFlf)
    box.pack_start(button, True, True, 0)

#

    self.add(box)

  def add_file_menu_actions(self, action_group):
    action_filemenu = Gtk.Action("FileMenu", "File", None, None)
    action_group.add_action(action_filemenu)

    action_filenewmenu = Gtk.Action("FileNew", None, None, Gtk.STOCK_NEW)
    action_group.add_action(action_filenewmenu)

    action_new = Gtk.Action("FileNewStandard", "_New", "Create a new file", Gtk.STOCK_NEW)
    action_new.connect("activate", self.on_menu_file_new_generic)
    action_group.add_action_with_accel(action_new, None)

    action_group.add_actions([
      ("FileNewFoo", None, "New Foo", None, "Create new foo",self.on_menu_file_new_generic),
      ("FileNewGoo", None, "_New Goo", None, "Create new goo",self.on_menu_file_new_generic),
      ])

    action_filequit = Gtk.Action("FileQuit", None, None, Gtk.STOCK_QUIT)
    action_filequit.connect("activate", self.on_menu_file_quit)
    action_group.add_action(action_filequit)

  def add_edit_menu_actions(self, action_group):
    action_group.add_actions([
      ("EditMenu", None, "Edit"),
      ("EditCopy", Gtk.STOCK_COPY, None, None, None,self.on_menu_others),
      ("EditPaste", Gtk.STOCK_PASTE, None, None, None,self.on_menu_others),
      ("EditSomething", None, "Something", "<control><alt>S", None, self.on_menu_others)
      ])

  def add_root_menu_actions(self, action_group):
    action_group.add_actions([
      ("RootMenu", None, "Root"),
      ("Browse", None, "Browse", "<control><alt>B", None, self.on_menu_Browse),
      ("Term", None, "Term", "<control><alt>T", None, self.on_menu_Term),
      ("FM", None, "FM", "<control><alt>F", None, self.on_menu_FM),
      ("Editor", None, "Editor", "<control><alt>E", None, self.on_menu_Editor)
      ])

#  def add_choices_menu_actions(self, action_group):
#    action_group.add_action(Gtk.Action("ChoicesMenu", "Choices", None,None))

#    action_group.add_radio_actions([
#      ("ChoiceOne", None, "One", None, None, 1),
#      ("ChoiceTwo", None, "Two", None, None, 2)
#      ], 1, self.on_menu_choices_changed)

#    three = Gtk.ToggleAction("ChoiceThree", "Three", None, None)
#    three.connect("toggled", self.on_menu_choices_toggled)
#    action_group.add_action(three)

  def create_ui_manager(self):
    uimanager = Gtk.UIManager()
    # Throws exception if something went wrong
    uimanager.add_ui_from_string(UI_INFO)
    # Add the accelerator group to the toplevel window
    accelgroup = uimanager.get_accel_group()
    self.add_accel_group(accelgroup)
    return uimanager

  def on_menu_file_new_generic(self, widget):
    print("A File|New menu item was selected.")

  def on_menu_file_quit(self, widget):
    Gtk.main_quit()

  def on_menu_others(self, widget):
    print("Menu item " + widget.get_name() + " was selected")

  def on_menu_Browse(self, widget):
    print("Menu item " + widget.get_name() + " was selected")
    runBrowser()

  def on_menu_Term(self, widget):
    print("Menu item " + widget.get_name() + " was selected")
    runTerminal()

  def on_menu_FM(self, widget):
    print("Menu item " + widget.get_name() + " was selected")
    runFileManager()

  def on_menu_Editor(self, widget):
    print("Menu item " + widget.get_name() + " was selected")
    runEditor()

#  def on_menu_choices_changed(self, widget, current):
#    print(current.get_name() + " was selected.")

#  def on_menu_choices_toggled(self, widget):
#    if widget.get_active():
#      print(widget.get_name() + " activated")
#    else:
#      print(widget.get_name() + " deactivated")

  def on_button_press_event(self, widget, event):
    # Check if right mouse button was preseed
    if event.type == Gdk.EventType.BUTTON_PRESS and event.button == 3:
      self.popup.popup(None, None, None, None, event.button, event.time)
      return True # event has been handled

window = MenuExampleWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
