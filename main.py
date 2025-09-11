#!/usr/bin/env python3
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
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Dan_Da_Dan_1_dark.png"], check=True)
                subprocess.run(["matugen", "image", "/home/ranger/wallpaper-script/Wallpapers/Dan_Da_Dan_1.png", "-p" , "hyprland"], check=True)
                subprocess.run(["wal","-i", "/home/ranger/wallpaper-script/Wallpapers/Dan_Da_Dan_1.png"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
                rofi_config = '/home/ranger/.config/rofi/config.rasi'
                with open(rofi_config, 'r') as rofi_file:
                    the_full_rofi_config = rofi_file.readlines()

                the_full_rofi_config[38] = f' background-image: url("/home/ranger/wallpaper-script/Wallpapers/Dan_Da_Dan_1.png",width);' + '\n'

                with open(rofi_config, 'w') as rofi_file:
                    rofi_file.writelines(the_full_rofi_config)
                
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
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Demon_Slayer_1_dark.jpg"], check=True)
                subprocess.run(["matugen", "image", "/home/ranger/wallpaper-script/Wallpapers/Demon_Slayer_1.jpg", "-p" , "hyprland"], check=True)
                subprocess.run(["wal","-i", "/home/ranger/wallpaper-script/Wallpapers/Demon_Slayer_1.jpg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
                rofi_config = '/home/ranger/.config/rofi/config.rasi'
                with open(rofi_config, 'r') as rofi_file:
                    the_full_rofi_config = rofi_file.readlines()

                the_full_rofi_config[38] = f' background-image: url("/home/ranger/wallpaper-script/Wallpapers/Demon_Slayer_1.jpg",width);' + '\n'

                with open(rofi_config, 'w') as rofi_file:
                    rofi_file.writelines(the_full_rofi_config)
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
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/JJK_1_dark.jpeg"], check=True)
                subprocess.run(["matugen", "image", "/home/ranger/wallpaper-script/Wallpapers/JJK_1.jpeg", "-p" , "hyprland"], check=True)
                subprocess.run(["wal","-i", "/home/ranger/wallpaper-script/Wallpapers/JJK_1.jpeg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
                rofi_config = '/home/ranger/.config/rofi/config.rasi'
                with open(rofi_config, 'r') as rofi_file:
                    the_full_rofi_config = rofi_file.readlines()

                the_full_rofi_config[38] = f' background-image: url("/home/ranger/wallpaper-script/Wallpapers/JJK_1.jpeg",width);' + '\n'

                with open(rofi_config, 'w') as rofi_file:
                    rofi_file.writelines(the_full_rofi_config)
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
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/JJK_2_dark.jpeg"], check=True)
                subprocess.run(["matugen", "image", "/home/ranger/wallpaper-script/Wallpapers/JJK_2.jpeg", "-p" , "hyprland"], check=True)
                subprocess.run(["wal","-i", "/home/ranger/wallpaper-script/Wallpapers/JJK_2.jpeg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
                rofi_config = '/home/ranger/.config/rofi/config.rasi'
                with open(rofi_config, 'r') as rofi_file:
                    the_full_rofi_config = rofi_file.readlines()

                the_full_rofi_config[38] = f' background-image: url("/home/ranger/wallpaper-script/Wallpapers/JJK_2.jpeg",width);' + '\n'

                with open(rofi_config, 'w') as rofi_file:
                    rofi_file.writelines(the_full_rofi_config)
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
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/JJK_3_dark.jpeg"], check=True)
                subprocess.run(["matugen", "image", "/home/ranger/wallpaper-script/Wallpapers/JJK_3.jpeg", "-p" , "hyprland"], check=True)
                subprocess.run(["wal","-i", "/home/ranger/wallpaper-script/Wallpapers/JJK_3.jpeg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
                rofi_config = '/home/ranger/.config/rofi/config.rasi'
                with open(rofi_config, 'r') as rofi_file:
                    the_full_rofi_config = rofi_file.readlines()

                the_full_rofi_config[38] = f' background-image: url("/home/ranger/wallpaper-script/Wallpapers/JJK_3.jpeg",width);' + '\n'

                with open(rofi_config, 'w') as rofi_file:
                    rofi_file.writelines(the_full_rofi_config)
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
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Kaiju_1_dark.jpg"], check=True)
                subprocess.run(["matugen", "image", "/home/ranger/wallpaper-script/Wallpapers/Kaiju_1.jpg", "-p" , "hyprland"], check=True)
                subprocess.run(["wal","-i", "/home/ranger/wallpaper-script/Wallpapers/Kaiju_1.jpg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
                rofi_config = '/home/ranger/.config/rofi/config.rasi'
                with open(rofi_config, 'r') as rofi_file:
                    the_full_rofi_config = rofi_file.readlines()

                the_full_rofi_config[38] = f' background-image: url("/home/ranger/wallpaper-script/Wallpapers/Kaiju_1.jpg",width);' + '\n'

                with open(rofi_config, 'w') as rofi_file:
                    rofi_file.writelines(the_full_rofi_config)
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
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Kaimen_riders_1_dark.png"], check=True)
                subprocess.run(["matugen", "image", "/home/ranger/wallpaper-script/Wallpapers/Kaimen_riders_1.png", "-p" , "hyprland"], check=True)
                subprocess.run(["wal","-i", "/home/ranger/wallpaper-script/Wallpapers/Kaimen_riders_1.png"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
                rofi_config = '/home/ranger/.config/rofi/config.rasi'
                with open(rofi_config, 'r') as rofi_file:
                    the_full_rofi_config = rofi_file.readlines()

                the_full_rofi_config[38] = f' background-image: url("/home/ranger/wallpaper-script/Wallpapers/Kaimen_riders_1.png",width);' + '\n'

                with open(rofi_config, 'w') as rofi_file:
                    rofi_file.writelines(the_full_rofi_config)
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
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Kill_La_Kill_1_dark.webp"], check=True)
                subprocess.run(["matugen", "image", "/home/ranger/wallpaper-script/Wallpapers/Kill_La_Kill_1.webp", "-p" , "hyprland"], check=True)
                subprocess.run(["wal","-i", "/home/ranger/wallpaper-script/Wallpapers/Kill_La_Kill_1.webp"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
                rofi_config = '/home/ranger/.config/rofi/config.rasi'
                with open(rofi_config, 'r') as rofi_file:
                    the_full_rofi_config = rofi_file.readlines()

                the_full_rofi_config[38] = f' background-image: url("/home/ranger/wallpaper-script/Wallpapers/Kill_La_Kill_1.webp",width);' + '\n'

                with open(rofi_config, 'w') as rofi_file:
                    rofi_file.writelines(the_full_rofi_config)
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
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Naruto_1_dark.jpeg"], check=True)
                subprocess.run(["matugen", "image", "/home/ranger/wallpaper-script/Wallpapers/Naruto_1.jpeg", "-p" , "hyprland"], check=True)
                subprocess.run(["wal","-i", "/home/ranger/wallpaper-script/Wallpapers/Naruto_1.jpeg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
                rofi_config = '/home/ranger/.config/rofi/config.rasi'
                with open(rofi_config, 'r') as rofi_file:
                    the_full_rofi_config = rofi_file.readlines()

                the_full_rofi_config[38] = f' background-image: url("/home/ranger/wallpaper-script/Wallpapers/Naruto_1.jpeg",width);' + '\n'

                with open(rofi_config, 'w') as rofi_file:
                    rofi_file.writelines(the_full_rofi_config)
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
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Pokemon_1_dark.jpg"], check=True)
                subprocess.run(["matugen", "image", "/home/ranger/wallpaper-script/Wallpapers/Pokemon_1.jpg", "-p" , "hyprland"], check=True)
                subprocess.run(["wal","-i", "/home/ranger/wallpaper-script/Wallpapers/Pokemon_1.jpg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
                rofi_config = '/home/ranger/.config/rofi/config.rasi'
                with open(rofi_config, 'r') as rofi_file:
                    the_full_rofi_config = rofi_file.readlines()

                the_full_rofi_config[38] = f' background-image: url("/home/ranger/wallpaper-script/Wallpapers/Pokemon_1.jpg",width);' + '\n'

                with open(rofi_config, 'w') as rofi_file:
                    rofi_file.writelines(the_full_rofi_config)
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
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Pokemon_2_dark.jpg"], check=True)
                subprocess.run(["matugen", "image", "/home/ranger/wallpaper-script/Wallpapers/Pokemon_2.jpg", "-p" , "hyprland"], check=True)
                subprocess.run(["wal","-i", "/home/ranger/wallpaper-script/Wallpapers/Pokemon_2.jpg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
                rofi_config = '/home/ranger/.config/rofi/config.rasi'
                with open(rofi_config, 'r') as rofi_file:
                    the_full_rofi_config = rofi_file.readlines()

                the_full_rofi_config[38] = f' background-image: url("/home/ranger/wallpaper-script/Wallpapers/Pokemon_2.jpg",width);' + '\n'

                with open(rofi_config, 'w') as rofi_file:
                    rofi_file.writelines(the_full_rofi_config)
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
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Pokemon_3_dark.jpg"], check=True)
                subprocess.run(["matugen", "image", "/home/ranger/wallpaper-script/Wallpapers/Pokemon_3.jpg", "-p" , "hyprland"], check=True)
                subprocess.run(["wal","-i", "/home/ranger/wallpaper-script/Wallpapers/Pokemon_3.jpg"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
                rofi_config = '/home/ranger/.config/rofi/config.rasi'
                with open(rofi_config, 'r') as rofi_file:
                    the_full_rofi_config = rofi_file.readlines()

                the_full_rofi_config[38] = f' background-image: url("/home/ranger/wallpaper-script/Wallpapers/Pokemon_3.jpg",width);' + '\n'

                with open(rofi_config, 'w') as rofi_file:
                    rofi_file.writelines(the_full_rofi_config)
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
                subprocess.run(["swww", "img", "/home/ranger/wallpaper-script/Wallpapers/Solo_leveling_1_dark.png"], check=True)
                subprocess.run(["matugen", "image", "/home/ranger/wallpaper-script/Wallpapers/Solo_leveling_1.png", "-p" , "hyprland"], check=True)
                subprocess.run(["wal","-i", "/home/ranger/wallpaper-script/Wallpapers/Solo_leveling_1.png"],check=True)
                subprocess.run(["hyprctl", "reload"],check=True)
                rofi_config = '/home/ranger/.config/rofi/config.rasi'
                with open(rofi_config, 'r') as rofi_file:
                    the_full_rofi_config = rofi_file.readlines()

                the_full_rofi_config[38] = f' background-image: url("/home/ranger/wallpaper-script/Wallpapers/Solo_leveling_1.png",width);' + '\n'

                with open(rofi_config, 'w') as rofi_file:
                    rofi_file.writelines(the_full_rofi_config)
            except:
                stdscr.clear()
                stdscr.addstr(0, 0,"Sorry this wallpaper is unavailable ,")
                stdscr.addstr(2,0,"check the path to your image.")
                stdscr.refresh()
                time.sleep(5)
                choosing_wallpaper(stdscr)
       
        else:
            choosing_wallpaper(stdscr)


def get_colors(stdscr):
    pywal_colors_config = '/home/ranger/.cache/wal/colors.json'
    with open(pywal_colors_config, 'r+') as pywal_colors_file:
        pywal_formatted_data = json.load(pywal_colors_file)
        background = pywal_formatted_data["special"]["background"]
        foreground = pywal_formatted_data["special"]["foreground"]
        cursor = pywal_formatted_data["special"]["cursor"]
        color0 = pywal_formatted_data["colors"]["color0"]
        color1 = pywal_formatted_data["colors"]["color1"]
        color2 = pywal_formatted_data["colors"]["color2"]
        color3 = pywal_formatted_data["colors"]["color3"]
        color4 = pywal_formatted_data["colors"]["color4"]
        color5 = pywal_formatted_data["colors"]["color5"]
        color6 = pywal_formatted_data["colors"]["color6"]
        color7 = pywal_formatted_data["colors"]["color7"]
        color8 = pywal_formatted_data["colors"]["color8"]
        color9 = pywal_formatted_data["colors"]["color9"]
        color10 = pywal_formatted_data["colors"]["color10"]
        color11 = pywal_formatted_data["colors"]["color11"]
        color12 = pywal_formatted_data["colors"]["color12"]
        color13 = pywal_formatted_data["colors"]["color13"]
        color14 = pywal_formatted_data["colors"]["color14"]
        color15 = pywal_formatted_data["colors"]["color15"]



    hyprpanel_config = '/home/ranger/.config/hyprpanel/config.json'
    with open(hyprpanel_config, 'r+') as hyprpanel_json_file:
        hyprpanel_formatted_data = json.load(hyprpanel_json_file)
        
        #Bar
        hyprpanel_formatted_data["theme.bar.background"] =  background
        hyprpanel_formatted_data["theme.bar.border.color"] = color1
       
        #Dashboard
        hyprpanel_formatted_data["theme.bar.buttons.dashboard.background"] = color4
        hyprpanel_formatted_data["theme.bar.buttons.dashboard.icon"] = color7
        hyprpanel_formatted_data["theme.bar.buttons.dashboard.border"] = color4

        #Cava
        hyprpanel_formatted_data["theme.bar.buttons.modules.cava.text"] = color7
        hyprpanel_formatted_data["theme.bar.buttons.modules.cava.background"] = color4
        hyprpanel_formatted_data["theme.bar.buttons.modules.cava.border"] = color4

        #Bluetooth
        hyprpanel_formatted_data["theme.bar.buttons.bluetooth.border"] = color1
        hyprpanel_formatted_data["theme.bar.buttons.bluetooth.background"] = color1
        hyprpanel_formatted_data["theme.bar.buttons.bluetooth.text"] = color7
        hyprpanel_formatted_data["theme.bar.buttons.bluetooth.icon"] = color7

        #Clock
        hyprpanel_formatted_data["theme.bar.buttons.clock.border"] = color1
        hyprpanel_formatted_data["theme.bar.buttons.clock.background"] = color1
        hyprpanel_formatted_data["theme.bar.buttons.clock.text"] = color7

        #Volume
        hyprpanel_formatted_data["theme.bar.buttons.volume.text"] = color7
        hyprpanel_formatted_data["theme.bar.buttons.volume.icon"] = color7
        hyprpanel_formatted_data["theme.bar.buttons.volume.border"] = color5
        hyprpanel_formatted_data["theme.bar.buttons.volume.background"] = color5
     
        #Music
        hyprpanel_formatted_data["theme.bar.buttons.media.background"] = color5
        hyprpanel_formatted_data["theme.bar.buttons.media.text"] = color7
        hyprpanel_formatted_data["theme.bar.buttons.media.icon"] = color7
        hyprpanel_formatted_data["theme.bar.buttons.media.icon_background"] = color5
        hyprpanel_formatted_data["theme.bar.buttons.media.border"] = color5

        #Workspaces
        hyprpanel_formatted_data["theme.bar.buttons.workspaces.border"] = color5
        hyprpanel_formatted_data["theme.bar.buttons.workspaces.background"] = color5
        hyprpanel_formatted_data["theme.bar.buttons.workspaces.hover"] = color14
        hyprpanel_formatted_data["theme.bar.buttons.workspaces.available"] = color10
        hyprpanel_formatted_data["theme.bar.buttons.workspaces.occupied"] = color7

        #Ram
        hyprpanel_formatted_data["theme.bar.buttons.modules.ram.background"] = color1
        hyprpanel_formatted_data["theme.bar.buttons.modules.ram.text"] = color7
        hyprpanel_formatted_data["theme.bar.buttons.modules.ram.icon"] = color7
        hyprpanel_formatted_data["theme.bar.buttons.modules.ram.border"] = color1

        #CPU
        hyprpanel_formatted_data["theme.bar.buttons.modules.cpu.background"] = color4
        hyprpanel_formatted_data["theme.bar.buttons.modules.cpu.text"] = color7
        hyprpanel_formatted_data["theme.bar.buttons.modules.cpu.icon"] = color7
        hyprpanel_formatted_data["theme.bar.buttons.modules.cpu.border"] = color4

    with open(hyprpanel_config, 'w' ) as f:
        json.dump(hyprpanel_formatted_data , f, indent=4)




    


    
def main(stdscr):
        greet(stdscr)
        choosing_wallpaper(stdscr)
        get_colors(stdscr)
       
       
if __name__ == "__main__":
    wrapper(main)