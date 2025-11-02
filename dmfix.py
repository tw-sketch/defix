#!/usr/bin/env python3
import subprocess
def reslight():
    subprocess.run(["sudo", "systemctl", "restart", "lightdm"])
    print("LightDM restarted")

def startlight():
    subprocess.run(["sudo", "systemctl", "start", "lightdm"])

def dislight():
    subprocess.run(["sudo", "systemctl", "disable", "lightdm"])
    print("LightDM disabled")

def enlight():
    subprocess.run(["sudo", "systemctl", "enable", "lightdm"])
    print("LightDM enabled")

print("Linux desktop debugger v--0.2")
print("Use 'help' to see the list of command lines")
while True:
    
    get = input("fixlight:")
    if get == "reslight":
        reslight()
        break
    elif get == "startlight":
        startlight()
    elif get == "dislight":
        dislight()
    elif get == "enlight":
        enlight()
        startlight()
    elif get == "help":
        list = ["reslight (restarts lightdm)", "dislight (disables lightdm)", "startlight (starts lightdm)",
                "enlight (enables lightdm)", "stop (closes the program)"]
        for item in list:
            print(item)
    elif get == "stop":
        break
    else:
        print("Invalid input")

