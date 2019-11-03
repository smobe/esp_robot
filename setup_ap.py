''' Set up esp as an access point '''
import network
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid = "robot1", password="password")

import webrepl_setup
