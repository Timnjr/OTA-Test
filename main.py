import time
from machine import Pin
from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/Timnjr/OTA-Test/"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

led = Pin(2, Pin.OUT) #Pin 2 als Ausgang setzen

while True:
    
    ota_updater.download_and_install_update_if_available()
    
    led.value(1)  #LED einschalten
    time.sleep(10) #1 Sekunde warten
    led.value(0)  #LED ausschalten
    time.sleep(1) #1 Sekunde warten