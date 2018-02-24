# -*- coding: utf-8 -*-

# Dropzone Action Info
# Name: Fingerprint
# Description: Drag and Drop Fingerprint Creator
# Handles: Files
# Creator: Mesut Yılmaz
# URL: yoursite.com
# Events: Clicked, Dragged
# KeyModifiers: Command, Option, Control, Shift
# SkipConfig: No
# RunsSandboxed: Yes
# Version: 1.0
# MinDropzoneVersion: 3.5

import os
import subprocess
import time

def dragged():
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    current = subprocess.Popen("pwd", stdout=subprocess.PIPE)
    current = current.communicate()[0].replace("\n","")
    filePath = items[0]
    file = open(current + "/amdb/fml.txt", "w")
    file.write(filePath)
    file.close()
    command = "cd " + current.replace(" ", "\ ") + "/amdb/ && "
    command = command + "./amdbBuilder -i fml.txt -c config.config -o " 
    command = command + filePath[:filePath.rfind("/")]
    command = command + "/film.amdb && say -v Yelda 'parmak izi işlemi tamamlandı'"

    print(command)
    dz.begin("Started")

    dz.determinate(True)

    dz.percent(25)

    if os.system(command) == 0:
        dz.percent(100)

    dz.finish("Task Complete")

    # If you don't want to place anything on the clipboard you should still call dz.url(false)
    dz.text(False)

def clicked():
    print(desktop)
    dz.finish(current)
    dz.url(False)
