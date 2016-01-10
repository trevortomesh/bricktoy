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
 iscVangVelytext = ""
 iscVamptext = ""
 iscVangVely = 0
 iscVamplitude = 0
 iscWindow5Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 iscWindow5Window1Fixed = gtk.Fixed()
 iscWindow5amp0 = gtk.TextView(buffer=None)
 iscWindow5OK0 = gtk.Button(" OK")
 iscWindow5angVely0 = gtk.TextView(buffer=None)
 iscWindow5cancel0 = gtk.Button("Cancel")
 iscWindow5Amplitude3 =gtk.Label("Amplitude")
 iscWindow5AngVely4 =gtk.Label("Angular Velocity")

 #EndOfGlobalVariables

 def main(self):
  gtk.main()

 def destroy(self, widget, data=None):
  gtk.main_quit()

#EndOfClass

def iscConvertTextToNumber3():
 try:
  thisiscApp1.iscVamplitude = float(thisiscApp1.iscVamptext)
 except ValueError:
  thisiscApp1.iscVamplitude = 0
 #iscConvertTextToNumber3Done


def iscGetTextField4():
 thisiscApp1.iscVangVelytext = thisiscApp1.iscWindow5angVely0.get_buffer().get_text(thisiscApp1.iscWindow5angVely0.get_buffer().get_start_iter(), thisiscApp1.iscWindow5angVely0.get_buffer().get_end_iter())
 iscConvertTextToNumber1()
 #iscGetTextField4Done


def iscGetTextField7():
 thisiscApp1.iscVamptext = thisiscApp1.iscWindow5amp0.get_buffer().get_text(thisiscApp1.iscWindow5amp0.get_buffer().get_start_iter(), thisiscApp1.iscWindow5amp0.get_buffer().get_end_iter())
 iscConvertTextToNumber3()
 #iscGetTextField7Done


def iscAppQuit8():
 thisiscApp1.destroy(None,None)
 #iscAppQuit8Done


def iscConvertTextToNumber1():
 try:
  thisiscApp1.iscVangVely = float(thisiscApp1.iscVangVelytext)
 except ValueError:
  thisiscApp1.iscVangVely = 0
 #iscConvertTextToNumber1Done


def iscWindow5():
 thisiscApp1.iscWindow5amp0 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow5OK0 = gtk.Button(" OK")
 thisiscApp1.iscWindow5angVely0 = gtk.TextView(buffer=None)
 thisiscApp1.iscWindow5cancel0 = gtk.Button("Cancel")
 thisiscApp1.iscWindow5Amplitude3 =gtk.Label("Amplitude")
 thisiscApp1.iscWindow5AngVely4 =gtk.Label("Angular Velocity")
 thisiscApp1.iscWindow5Window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
 thisiscApp1.iscWindow5Window1Fixed = gtk.Fixed()
 thisiscApp1.iscWindow5Window1.set_title("OscBrick Properties")
 thisiscApp1.iscWindow5Window1.set_default_size(314, 233)
 thisiscApp1.iscWindow5Window1.add(thisiscApp1.iscWindow5Window1Fixed)
 thisiscApp1.iscWindow5Window1Fixed.width = 314
 thisiscApp1.iscWindow5Window1Fixed.height = 233
 thisiscApp1.iscWindow5Window1.connect("delete_event", iscWindow5Closed)
 thisiscApp1.iscWindow5Window1Fixed.show()
 thisiscApp1.iscWindow5Window1Fixed.put(thisiscApp1.iscWindow5amp0, 185, 82)
 thisiscApp1.iscWindow5amp0.set_size_request(100, 30)
 thisiscApp1.iscWindow5amp0.show()
 thisiscApp1.iscWindow5Window1Fixed.put(thisiscApp1.iscWindow5OK0, 45, 191)
 thisiscApp1.iscWindow5OK0.set_size_request(80, 26)
 thisiscApp1.iscWindow5OK0.connect("clicked", iscWindow5OKClicked)
 thisiscApp1.iscWindow5OK0.show()
 thisiscApp1.iscWindow5Window1Fixed.put(thisiscApp1.iscWindow5angVely0, 15, 82)
 thisiscApp1.iscWindow5angVely0.set_size_request(100, 30)
 thisiscApp1.iscWindow5angVely0.show()
 thisiscApp1.iscWindow5Window1Fixed.put(thisiscApp1.iscWindow5cancel0, 169, 191)
 thisiscApp1.iscWindow5cancel0.set_size_request(80, 26)
 thisiscApp1.iscWindow5cancel0.connect("clicked", iscWindow5cancelClicked)
 thisiscApp1.iscWindow5cancel0.show()
 thisiscApp1.iscWindow5Window1Fixed.put(thisiscApp1.iscWindow5Amplitude3, 10, 59)
 thisiscApp1.iscWindow5Amplitude3.set_size_request(91, 12)
 thisiscApp1.iscWindow5Amplitude3.show()
 thisiscApp1.iscWindow5Window1Fixed.put(thisiscApp1.iscWindow5AngVely4, 179, 59)
 thisiscApp1.iscWindow5AngVely4.set_size_request(115, 14)
 thisiscApp1.iscWindow5AngVely4.show()
 thisiscApp1.iscWindow5Window1.show()
 #iscWindow5Opened
 #iscWindow5Done


def iscWindow5Closed(self, other):
 pass
 iscAppQuit8()
 #iscWindow5Closed


def iscWindow5OKClicked(self):
 pass
 iscGetTextField7()
 iscGetTextField4()
 
 vals=[thisiscApp1.iscVangVely,thisiscApp1.iscVamplitude]
 print(vals)
 iscAppQuit8()





 #iscWindow5OKClicked


def iscWindow5cancelClicked(self):
 pass
 iscAppQuit8()
 #iscWindow5cancelClicked


#EndOfFunctions

thisiscApp1 = iscApp1()

iscWindow5()
#iscApp1Launched
#EndOfStatements

thisiscApp1.main()
