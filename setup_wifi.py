import webrepl_setup

import network

station = network.WLAN(network.STA_IF)

station.active(True)

station.connect("ssid", "pwd")

station.isconnected()

station.ifconfig()
