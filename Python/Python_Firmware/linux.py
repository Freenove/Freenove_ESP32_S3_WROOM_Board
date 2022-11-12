import os
import sys
import time

os.system("python3 esptool/esptool.py --chip esp32s3  erase_flash")

os.system("python3 esptool/esptool.py --chip esp32s3 --baud 2000000 write_flash -z 0 GENERIC_S3-20220618-v1.19.1.bin")

