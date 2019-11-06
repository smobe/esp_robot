# esp_robot
micro python libraries for using an esp8266 microcontroller to control camjam robot

https://camjam.me/?page_id=1035

# install thonny
sudo apt-get install thonny

# download firmware
mkdir ~/git

cd ~/git

https://micropython.org/download#esp8266

# download esptool
cd ~/git

git clone https://github.com/espressif/esptool.git

# upload firmware to esp
sudo python3 esptool.py  -p /dev/ttyUSB0 write_flash -fm dio -fs 32m 0x00000 ../esp_robot/esp8266-20190529-v1.11.bin

# log into esp over usb
picocom /dev/ttyUSB0 -b115200

# set up esp as wifi access point
cd ~/git

git clone https://github.com/smobe/esp_robot.git

cd esp_robot

run text from setup_ap.py on esp prompt

# download webrepl
cd ~/git

https://github.com/micropython/webrepl.git

cd webrepl

# connect to esp wifi access point
connect using credentials in the setup_ap.py file

# access esp via webrepl tool
open webrepl.html in browser

connect to esp using webrepl using password set up after the import webrepl_setup stage

# upload code to esp 
~/git/esp_robot/main.py 

~/git/esp_robot/robot.py 

main.py will auto run when the esp chip is reset robot.py is libraries to control the robot
