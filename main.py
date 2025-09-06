import os
import subprocess
import time
import sys

def main():
    subprocess.run(["swww" ,  "kill"], check=False)
    subprocess.Popen(["swww-daemon"])
    subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/ds.jpg"], check=True)
    subprocess.run(["hyprctl", "reload"],check=True)
if __name__ == "__main__":
    main()