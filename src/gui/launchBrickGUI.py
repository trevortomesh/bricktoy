#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gobject
import random
import os
import sys
import gtk
#EndImports

class iscApp1:
 iscVinitVelText = ""
 iscVangleText = ""
 iscVinitVel = 0
 iscVangle = 0
 iscWindow6Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow6Window1Fixed = gtk.Fixed()
 iscWindow6OKButton0 = gtk.Button("OK")
 iscWindow6cancelButton0 = gtk.Button("Cancel")
 iscWindow6initialVelocityLabel0 =gtk.Label("Initial Velocity")
 iscWindow6angleLabel0 =gtk.Label("Angle")
 iscWindow6initialVelocity0 = gtk.TextView(buffer=None)
 iscWindow6angle0 = gtk.TextView(buffer=None)

 #EndOfGlobalVariables

 def main(self):
  gtk.main()

 def destroy(self, widget, data=None):
  gtk.main_quit()

#EndOfClass

def iscWindow6():
 thisiscApp1.iscWindow6OKButton0 = gtk.Button("OK")
 thisiscApp1.iscWindow6cancelButton0 = gtk.Button("Cancel")
 thisiscApp1.iscWindow6initialVelocityLabel0 =gtk.Label("Initial Velocity")
 thisiscApp1.iscWindow6angleLabel0 =gtk.Label("Angle")
 thisiscApp1.iscWindow6initialVelocity0 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow6angle0 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow6Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow6Window1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow6Window1.set_title("Window")
 thisiscApp1.iscWindow6Window1.set_default_size(306, 157)
 thisiscApp1.iscWindow6Window1.add(thisiscApp1.iscWindow6Window1Fixed)
 thisiscApp1.iscWindow6Window1Fixed.width = 306
 thisiscApp1.iscWindow6Window1Fixed.height = 157
 thisiscApp1.iscWindow6Window1.connect("delete_event", iscWindow6Closed)
 thisiscApp1.iscWindow6Window1Fixed.show()
 thisiscApp1.iscWindow6Window1Fixed.put(thisiscApp1.iscWindow6OKButton0, 49, 100)
 thisiscApp1.iscWindow6OKButton0.set_size_request(80, 26)
 thisiscApp1.iscWindow6OKButton0.connect("clicked", iscWindow6OKButtonClicked)
 thisiscApp1.iscWindow6OKButton0.show()
 thisiscApp1.iscWindow6Window1Fixed.put(thisiscApp1.iscWindow6cancelButton0, 168, 100)
 thisiscApp1.iscWindow6cancelButton0.set_size_request(80, 26)
 thisiscApp1.iscWindow6cancelButton0.connect("clicked", iscWindow6cancelButtonClicked)
 thisiscApp1.iscWindow6cancelButton0.show()
 thisiscApp1.iscWindow6Window1Fixed.put(thisiscApp1.iscWindow6initialVelocityLabel0, 42, 24)
 thisiscApp1.iscWindow6initialVelocityLabel0.set_size_request(106, 19)
 thisiscApp1.iscWindow6initialVelocityLabel0.show()
 thisiscApp1.iscWindow6Window1Fixed.put(thisiscApp1.iscWindow6angleLabel0, 163, 24)
 thisiscApp1.iscWindow6angleLabel0.set_size_request(41, 19)
 thisiscApp1.iscWindow6angleLabel0.show()
 thisiscApp1.iscWindow6Window1Fixed.put(thisiscApp1.iscWindow6initialVelocity0, 49, 50)
 thisiscApp1.iscWindow6initialVelocity0.set_size_request(80, 22)
 thisiscApp1.iscWindow6initialVelocity0.show()
 thisiscApp1.iscWindow6Window1Fixed.put(thisiscApp1.iscWindow6angle0, 169, 50)
 thisiscApp1.iscWindow6angle0.set_size_request(80, 22)
 thisiscApp1.iscWindow6angle0.show()
 thisiscApp1.iscWindow6Window1.show()
 #iscWindow6Opened
 #iscWindow6Done


def iscWindow6Closed(self, other):
 pass
 iscAppQuit1()
 #iscWindow6Closed


def iscWindow6OKButtonClicked(self):
 pass
 iscGetTextField10()
 
 iscGetTextField14()

 vals = [thisiscApp1.iscVangle,thisiscApp1.iscVinitVel]
 print(vals)

 iscAppQuit1()
 #iscWindow6OKButtonClicked


def iscWindow6cancelButtonClicked(self):
 pass
 iscAppQuit1()
 #iscWindow6cancelButtonClicked


def iscConvertTextToNumber11():
 try:
  thisiscApp1.iscVinitVel = float(thisiscApp1.iscVinitVelText)
 except ValueError:
  thisiscApp1.iscVinitVel = 0
 #iscConvertTextToNumber11Done


def iscAppQuit1():
 thisiscApp1.destroy(None,None)
 #iscAppQuit1Done


def iscConvertTextToNumber13():
 try:
  thisiscApp1.iscVangle = float(thisiscApp1.iscVangleText)
 except ValueError:
  thisiscApp1.iscVangle = 0
 #iscConvertTextToNumber13Done


def iscGetTextField10():
 thisiscApp1.iscVinitVelText = thisiscApp1.iscWindow6initialVelocity0.get_buffer().get_text(thisiscApp1.iscWindow6initialVelocity0.get_buffer().get_start_iter(), thisiscApp1.iscWindow6initialVelocity0.get_buffer().get_end_iter())
 iscConvertTextToNumber11()
 #iscGetTextField10Done


def iscGetTextField14():
 thisiscApp1.iscVangleText = thisiscApp1.iscWindow6angle0.get_buffer().get_text(thisiscApp1.iscWindow6angle0.get_buffer().get_start_iter(), thisiscApp1.iscWindow6angle0.get_buffer().get_end_iter())
 iscConvertTextToNumber13()
 #iscGetTextField14Done


#EndOfFunctions

thisiscApp1 = iscApp1()

iscWindow6()
#iscApp1Launched
#EndOfStatements

thisiscApp1.main()
