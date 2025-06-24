#V2.0
import time
from machine import Pin
from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/Timnjr/OTA-Test/"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

led = Pin(2, Pin.OUT) #Pin 2 als Ausgang setzen

while True:
    ota_updater.download_and_install_update_if_available()
    
    for i in range(5):
        led.value(1)
        time.sleep(2)
        led.value(0)
        time.sleep(1)