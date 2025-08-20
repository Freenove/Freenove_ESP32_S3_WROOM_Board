import os
import sys
import time

os.system("python3 esptool/esptool.py --chip esp32s3  erase_flash")

os.system("python3 esptool/esptool.py --chip esp32s3 --baud 2000000 write_flash -z 0 ESP32_GENERIC_S3-SPIRAM_OCT-20250809-v1.26.0.bin")

