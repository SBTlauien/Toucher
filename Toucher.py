#!/usr/bin/env
import os, gtk, appindicator, subprocess, StringIO

def main():
    indicator = appindicator.Indicator("Toucher", '/home/me/py/toucher.png', appindicator.CATEGORY_APPLICATION_STATUS)
    indicator.set_status(appindicator.STATUS_ACTIVE)
    indicator.set_menu(build_menu())
    gtk.main()

def build_menu():
    menu = gtk.Menu()
    onItem = gtk.MenuItem("ON")
    onItem.connect("activate", on, "On")
    menu.append(onItem)
    offItem = gtk.MenuItem("OFF")
    offItem.connect("activate", off, "Off")
    menu.append(offItem)
    menu.show_all()
    return menu

def getInt():
    s = StringIO.StringIO(subprocess.check_output("xinput list", shell=True))
    for line in s:
        if "My-Laptops-Touch-Pad-Id" in line:
            return line.split('id=')[1].split('\t')[0]

def on(self, wtf):
    subprocess.call("xinput --enable " + getInt(), shell=True)

def off(self, wtf):
    subprocess.call("xinput --disable " + getInt(), shell=True)

if 1 == 1:main()
