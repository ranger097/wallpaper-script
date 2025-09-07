import os
import subprocess
import time
import sys
import json
from curses import wrapper
import curses



def greet(stdscr):
    stdscr.clear()
    stdscr.addstr(0,0,"HI, welcome to my wallpaper-script - ranger097")
    stdscr.addstr(2,0,"Press Enter to continue")
    stdscr.refresh()
    


def choosing_wallpaper(stdscr):
    pressed_enter = stdscr.getch()
    stdscr.refresh()
    if pressed_enter == ord("\n"):
        stdscr.clear()
        stdscr.addstr(0,0,"Please choose a wallpaper :")
        stdscr.addstr(2,0,"1. Solo Leveling")
        stdscr.addstr(4,0,"2. Demon Slayer")
        stdscr.addstr(6,0,"3. Naruto")
        stdscr.refresh()
        pick_wallpaper = stdscr.getch()
        if pick_wallpaper == ord("1"):
            try: 
                subprocess.run(["swww" ,  "kill"], check=False)
                subprocess.Popen(["swww-daemon"])
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/solo-leveling.png"], check=True)
                subprocess.run(["wal", "-i", "/home/ranger/wallpaper-script/ds.jpg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
            except:
                stdscr.clear()
                stdscr.addstr(0, 0,"Sorry this wallpaper is unavailable ,")
                stdscr.addstr(2,0,"check the path to your image.")
                stdscr.refresh()
                time.sleep(5)
                choosing_wallpaper()
                
        elif pick_wallpaper == ord("2"):
            try: 
                subprocess.run(["swww" ,  "kill"], check=False)
                subprocess.Popen(["swww-daemon"])
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/demonslayer.jpg"], check=True)
                subprocess.run(["wal", "-i", "/home/ranger/wallpaper-script/demonslayer.jpg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
            except:
                subprocess.run(["swww" ,  "kill"], check=False)
                subprocess.Popen(["swww-daemon"])
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/demonslayer.jpg"], check=True)
                subprocess.run(["wal" , "-i" , "/home/ranger/wallpaper-script/demonslayer.jpg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
        else:
            choosing_wallpaper()




def main(stdscr):
        greet(stdscr)
        choosing_wallpaper(stdscr)
    
        
       



   
   
if __name__ == "__main__":
    wrapper(main)