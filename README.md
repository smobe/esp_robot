# Esp Robot Library
Micro python libraries for using an esp8266 microcontroller to control camjam robot.

The camjam kit is designed to use a raspberry pi but these are relatively expensive. 

This library allows us to use a much cheaper ESP8266 chip bringing the cost of a robot to £30 (including power bank battery) from £50 for a raspberry pi version.

https://camjam.me/?page_id=1035

# Install thonny
sudo apt-get install thonny

# Download firmware
mkdir ~/git

cd ~/git

Download relevant micro python firmware file for the ESP chip you have from
https://micropython.org/download#esp8266

# Download esptool
cd ~/git

git clone https://github.com/espressif/esptool.git

# Upload firmware to esp
sudo python3 esptool.py  -p /dev/ttyUSB0 write_flash -fm dio -fs 32m 0x00000 ../esp_robot/esp8266-20190529-v1.11.bin

# Log into esp over usb
picocom /dev/ttyUSB0 -b115200

# Set up esp as wifi access point
cd ~/git

git clone https://github.com/smobe/esp_robot.git

cd esp_robot

run text from setup_ap.py on esp prompt

make sure you also setup webrepl and make a password

# Download webrepl
cd ~/git

https://github.com/micropython/webrepl.git

cd webrepl

# Connect to esp wifi access point
search wifi networks and there should be one now with the name from the setup_ap.py file.

connect using password in the setup_ap.py file

# Access esp via webrepl tool
open webrepl.html in browser

connect to esp using webrepl using password set up after the import webrepl_setup stage

# Upload code to esp 
~/git/esp_robot/main.py 

~/git/esp_robot/robot.py 

main.py will auto run when the esp chip is reset robot.py is libraries to control the robot
