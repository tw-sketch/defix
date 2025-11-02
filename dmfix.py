#!/usr/bin/env python3
import subprocess
def reslight():
    subprocess.run(["sudo", "systemctl", "restart", "lightdm"])
    print("LightDM restarted")
    command()

def startlight():
    subprocess.run(["sudo", "systemctl", "start", "lightdm"])

def dislight():
    subprocess.run(["sudo", "systemctl", "disable", "lightdm"])
    print("LightDM disabled")
    command()

def enlight():
    subprocess.run(["sudo", "systemctl", "enable", "lightdm"])
    print("LightDM enabled")
    command()

def command():
    get = input("fixlight:")
    if get == "reslight":
        reslight()
    elif get == "startlight":
        startlight()
    elif get == "dislight":
        dislight()
    elif get == "enlight":
        enlight()
        startlight()
    elif get == "fix":
        dislight()
        enlight()
    elif get == "help":
        print("""reslight(restarts LightDM) startlight(starts LightDM) dislight(disables LightDM) enlight(enables LightDM)""")
        command()
    else:
        print("Invalid input")
        command()

print("Linux desktop rebooter v--0.1")
print("Use 'help' to see the list of command lines")
command()
