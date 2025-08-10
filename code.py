from config import config
from meta_board import MetaLikeBoard
from meta_api import MetaApi, MetaApiOnFirException
import os
import busio
import board
from digitalio import DigitalInOut
import neopixel
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_wifimanager
import time 

import asyncio
# New network
esp32_cs = DigitalInOut(board.ESP_CS)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)
status_light = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)


ssid = os.getenv("WIFI_SSID")
password = os.getenv("WIFI_PASSWORD")
wifi = adafruit_esp32spi_wifimanager.WiFiManager(esp, ssid, password, status_pixel = status_light)


REFRESH_INTERVAL = config['refresh_interval']

api = MetaApi()
def refresh_board() -> [dict]:
    try:
        response = api.fetch_like_count(wifi)
    except MetaApiOnFirException:
        print('Meta API might be on fire. Resetting wifi ...')
        wifi.reset()
        return {}
    return response


meta_board = MetaLikeBoard()

async def scroll_text_task():
    while True:
        meta_board.update_header_scrolling()
        await asyncio.sleep(config["scroll_speed"])  # run every 50ms


async def update_like_count():
    while True:
        meta_data = refresh_board()
        meta_board.update_page_name(meta_data.get("name", None))
        meta_board.update_fan_count(meta_data.get("fan_count", None))
        await asyncio.sleep(30)  # wait 2 mins

async def main():
    await asyncio.gather(update_like_count(), scroll_text_task())




asyncio.run(main())
