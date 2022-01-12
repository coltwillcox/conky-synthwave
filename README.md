# conky-synthwave
Synthwave vibes for your Conky and desktop.

# Screenshot
![Screenshot](screenshot.jpg "Screenshot")

# Installation
* Copy **conky-synthwave** folder from this repository to **/home/user/.conky/** (your user home folder)
* Modify next files:
  * .conky_cal: replace **/home/user/** with your home folder.
  * .conky_gmail: replace **/home/user/** with your home folder.
  * .conky_speed: replace **/home/user/** with your home folder.
  * .conky_stod: replace **/home/user/** with your home folder.
  * .conky_weather: replace **/home/user/** with your home folder.
  * .conkyrc: replace **/home/user/** with your home folder.
  * .conkyrc: replace **/mnt/data** with your mounted partition (any drive you have access should work).
  * pygmail.py: replace **email** and **passwd** values with your Gmail **App passwords** (visit https://support.google.com/mail/answer/185833?hl=en or search for **Google App passwords**).
  * pyweath.py: replace **APPID** and **CITY** values with your OpenWeather App ID (visit https://openweathermap.org/ to create free account).
  * conky-startup.sh: replace **/home/user/** with your home folder.
  * all config files: remove line **xinerama_head=1** or experiment with other  values. (This is because I am displaying Conky on secondary monitor. You will **MOST PROBABLY** need to delete this variable in every file.)

# Optional installation steps
* Add **conky-startup.sh** to your OS autostart items.
* Install **Luculent** font (visit http://eastfarthing.com/luculent/). Try "Prehinted" version with your DPI first. It's my favourite monospace font. :)
* Install **Speedtest** CLI tool (visit https://www.speedtest.net/apps/cli).
* Modify **.conky_mpd** to use real data from Music Player Daemon (mpd). I am not using it, so I have just some static info there.
* Modify **.shitstodo** content with your TODO data.
* Set **conky-synthwave/synthwave.jpg** as desktop wallpaper.
* Play with **gap_x** and **gap_y** values in config files. Positions are fixed for 1920x1080 resolution.

# Notes
* This conky config is using **gcal**, **sensors**, **sed**, **tail**, **awk**. Check from terminal that you have them installed.
* Config files are in **Lua** syntax.
* **python3** needs to be instaled. Tested with 3.9.2.
* Tested on **MX Linux 21 Wildflower**.

# Credits
* Original sources:
  * **slacker conky config** by **0x6c756b65** (https://www.deviantart.com/0x6c756b65/art/slacker-conky-config-207760045)
  * **haxOS Conky** by **DavidDavioBlue** (https://www.deviantart.com/daviddavioblue/art/haxOS-Conky-454353060)
  * **conky config** by **Joschka Köster** (https://github.com/hringriin/conky)