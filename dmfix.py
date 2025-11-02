#!/usr/bin/env python3
import subprocess

def control_lightdm(action):
    try:
        subprocess.run(["sudo", "systemctl", action, "lightdm"])
        print(f"LightDM {action}")
    except subprocess.CalledProccessError:
        print(f"Error: Falled to {action} LightDM. Check your permisions or system status.")

def reslight():
    control_lightdm("restart")

def startlight():
    control_lightdm("start")

def dislight():
    control_lightdm("disable")

def enlight():
    control_lightdm("enable")

print("Linux desktop debugger v--0.3")
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

