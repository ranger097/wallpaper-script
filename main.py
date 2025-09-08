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
        stdscr.addstr(1,0,"(a) . Dan Da Dan 1")
        stdscr.addstr(2,0,"(b) . Demon Slayer 1")
        stdscr.addstr(3,0,"(c) . Jujustu Kaisen 1")
        stdscr.addstr(4,0,"(d) . Jujustu Kaisen 2")
        stdscr.addstr(5,0,"(e) . Jujustu Kaisen 3")
        stdscr.addstr(6,0,"(f) . Kaiju 1")
        stdscr.addstr(7,0,"(g) . Kaimen Riders 1")
        stdscr.addstr(8,0,"(h) . Kill La Kill 1")
        stdscr.addstr(9,0,"(i) . Naruto 1")
        stdscr.addstr(10,0,"(j) . Pokemon 1")
        stdscr.addstr(11,0,"(k) . Pokemon 2")
        stdscr.addstr(12,0,"(l) . Pokemon 3")
        stdscr.addstr(13,0,"(m) . Solo Leveling 1")
        stdscr.refresh()
        pick_wallpaper = stdscr.getch()
        if pick_wallpaper == ord("a"):
            try: 
                subprocess.run(["swww" ,  "kill"], check=False)
                subprocess.Popen(["swww-daemon"])
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Dan_Da_Dan_1.png"], check=True)
                subprocess.run(["wal", "-i", "/home/ranger/wallpaper-script/Wallpapers/Dan_Da_Dan_1.png"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
            except:
                stdscr.clear()
                stdscr.addstr(0, 0,"Sorry this wallpaper is unavailable ,")
                stdscr.addstr(2,0,"check the path to your image.")
                stdscr.refresh()
                time.sleep(5)
                choosing_wallpaper(stdscr)
                
        elif pick_wallpaper == ord("b"):
            try: 
                subprocess.run(["swww" ,  "kill"], check=False)
                subprocess.Popen(["swww-daemon"])
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Demon_Slayer_1.jpg"], check=True)
                subprocess.run(["wal", "-i", "/home/ranger/wallpaper-script/Wallpapers/Demon_Slayer_1.jpg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
            except:
                stdscr.clear()
                stdscr.addstr(0, 0,"Sorry this wallpaper is unavailable ,")
                stdscr.addstr(2,0,"check the path to your image.")
                stdscr.refresh()
                time.sleep(5)
                choosing_wallpaper(stdscr)

        elif pick_wallpaper == ord("c"):
            try: 
                subprocess.run(["swww" ,  "kill"], check=False)
                subprocess.Popen(["swww-daemon"])
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/JJK_1.jpeg"], check=True)
                subprocess.run(["wal", "-i", "/home/ranger/wallpaper-script/Wallpapers/JJK_1.jpeg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
            except:
               stdscr.clear()
               stdscr.addstr(0, 0,"Sorry this wallpaper is unavailable ,")
               stdscr.addstr(2,0,"check the path to your image.")
               stdscr.refresh()
               time.sleep(5)
               choosing_wallpaper(stdscr)

        elif pick_wallpaper == ord("d"):
            try: 
                subprocess.run(["swww" ,  "kill"], check=False)
                subprocess.Popen(["swww-daemon"])
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/JJK_2.jpeg"], check=True)
                subprocess.run(["wal", "-i", "/home/ranger/wallpaper-script/Wallpapers/JJK_2.jpeg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
            except:
                stdscr.clear()
                stdscr.addstr(0, 0,"Sorry this wallpaper is unavailable ,")
                stdscr.addstr(2,0,"check the path to your image.")
                stdscr.refresh()
                time.sleep(5)
                choosing_wallpaper(stdscr)

        elif pick_wallpaper == ord("e"):
            try: 
                subprocess.run(["swww" ,  "kill"], check=False)
                subprocess.Popen(["swww-daemon"])
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/JJK_3.jpeg"], check=True)
                subprocess.run(["wal", "-i", "/home/ranger/wallpaper-script/Wallpapers/JJK_3.jpeg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
            except:
                stdscr.clear()
                stdscr.addstr(0, 0,"Sorry this wallpaper is unavailable ,")
                stdscr.addstr(2,0,"check the path to your image.")
                stdscr.refresh()
                time.sleep(5)
                choosing_wallpaper(stdscr)

        elif pick_wallpaper == ord("f"):
            try: 
                subprocess.run(["swww" ,  "kill"], check=False)
                subprocess.Popen(["swww-daemon"])
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Kaiju_1.jpg"], check=True)
                subprocess.run(["wal", "-i", "/home/ranger/wallpaper-script/Wallpapers/Kaiju_1.jpg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
            except:
                stdscr.clear()
                stdscr.addstr(0, 0,"Sorry this wallpaper is unavailable ,")
                stdscr.addstr(2,0,"check the path to your image.")
                stdscr.refresh()
                time.sleep(5)
                choosing_wallpaper(stdscr)

        elif pick_wallpaper == ord("g"):
            try: 
                subprocess.run(["swww" ,  "kill"], check=False)
                subprocess.Popen(["swww-daemon"])
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Kaimen_riders_1.png"], check=True)
                subprocess.run(["wal", "-i", "/home/ranger/wallpaper-script/Wallpapers/Kaimen_riders_1.png"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
            except:
                stdscr.clear()
                stdscr.addstr(0, 0,"Sorry this wallpaper is unavailable ,")
                stdscr.addstr(2,0,"check the path to your image.")
                stdscr.refresh()
                time.sleep(5)
                choosing_wallpaper(stdscr)

        elif pick_wallpaper ==ord("h"):
            try: 
                subprocess.run(["swww" ,  "kill"], check=False)
                subprocess.Popen(["swww-daemon"])
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Kill_La_Kill_1.webp"], check=True)
                subprocess.run(["wal", "-i", "/home/ranger/wallpaper-script/Wallpapers/Kill_La_Kill_1.webp"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
            except:
                stdscr.clear()
                stdscr.addstr(0, 0,"Sorry this wallpaper is unavailable ,")
                stdscr.addstr(2,0,"check the path to your image.")
                stdscr.refresh()
                time.sleep(5)
                choosing_wallpaper(stdscr)

        elif pick_wallpaper == ord("i"):
            try: 
                subprocess.run(["swww" ,  "kill"], check=False)
                subprocess.Popen(["swww-daemon"])
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Naruto_1.jpeg"], check=True)
                subprocess.run(["wal", "-i", "/home/ranger/wallpaper-script/Wallpapers/Naruto_1.jpeg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
            except:
               stdscr.clear()
               stdscr.addstr(0, 0,"Sorry this wallpaper is unavailable ,")
               stdscr.addstr(2,0,"check the path to your image.")
               stdscr.refresh()
               time.sleep(5)
               choosing_wallpaper(stdscr)
               
        elif pick_wallpaper == ord("j"):
            try: 
                subprocess.run(["swww" ,  "kill"], check=False)
                subprocess.Popen(["swww-daemon"])
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Pokemon_1.jpg"], check=True)
                subprocess.run(["wal", "-i", "/home/ranger/wallpaper-script/Wallpapers/Pokemon_1.jpg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
            except:
                stdscr.clear()
                stdscr.addstr(0, 0,"Sorry this wallpaper is unavailable ,")
                stdscr.addstr(2,0,"check the path to your image.")
                stdscr.refresh()
                time.sleep(5)
                choosing_wallpaper(stdscr)

        elif pick_wallpaper == ord("k"):
            try: 
                subprocess.run(["swww" ,  "kill"], check=False)
                subprocess.Popen(["swww-daemon"])
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Pokemon_2.jpg"], check=True)
                subprocess.run(["wal", "-i", "/home/ranger/wallpaper-script/Wallpapers/Pokemon_2.jpg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
            except:
                stdscr.clear()
                stdscr.addstr(0, 0,"Sorry this wallpaper is unavailable ,")
                stdscr.addstr(2,0,"check the path to your image.")
                stdscr.refresh()
                time.sleep(5)
                choosing_wallpaper(stdscr)
        elif pick_wallpaper == ord("l"):
            try: 
                subprocess.run(["swww" ,  "kill"], check=False)
                subprocess.Popen(["swww-daemon"])
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Pokemon_3.jpg"], check=True)
                subprocess.run(["wal", "-i", "/home/ranger/wallpaper-script/Wallpapers/Pokemon_3.jpg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
            except:
                stdscr.clear()
                stdscr.addstr(0, 0,"Sorry this wallpaper is unavailable ,")
                stdscr.addstr(2,0,"check the path to your image.")
                stdscr.refresh()
                time.sleep(5)
                choosing_wallpaper(stdscr)
        elif pick_wallpaper == ord("m"):
            try: 
                subprocess.run(["swww" ,  "kill"], check=False)
                subprocess.Popen(["swww-daemon"])
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Solo_leveling_1.png"], check=True)
                subprocess.run(["wal", "-i", "/home/ranger/wallpaper-script/Wallpapers/Solo_leveling_1.png"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
            except:
                stdscr.clear()
                stdscr.addstr(0, 0,"Sorry this wallpaper is unavailable ,")
                stdscr.addstr(2,0,"check the path to your image.")
                stdscr.refresh()
                time.sleep(5)
                choosing_wallpaper(stdscr)
       
        else:
            choosing_wallpaper(stdscr)




def main(stdscr):
        greet(stdscr)
        choosing_wallpaper(stdscr)
    
        
       



   
   
if __name__ == "__main__":
    wrapper(main)