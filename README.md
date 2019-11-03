# esp_robot
micro python libraries for esp camjam robot

# install thonny
sudo apt-get install thonny

mkdir ~/git

# download firmware
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
cd cd esp_robot
python3 setup_ap.py

# download webrepl
cd ~/git
https://github.com/micropython/webrepl.git
cd webrepl

# access esp via webrepl tool
open webrepl.html


# put code in ~/git/esp_robot/main.py and robot.py onto esp
