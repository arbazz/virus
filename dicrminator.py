from ast import Str
import os
import struct
import ctypes
import pathlib
import time
current_path = pathlib.Path().resolve() 
PATH = os.path.join(current_path,"androidparty.png")
SPI_SETDESKWALLPAPER = 20
print(PATH)


def is_64bit():
    return struct.calcsize("P") * 8 == 64


def changeBg(path):
    if is_64bit():
        ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER, 0, path, 3)

def startProgram():
    print("Runnig at " + str(time.time()))
    changeBg(PATH)

delay = 5000
wait = delay
t1 = time.time()

while True:
    t2 = time.time() - t1

    if t2 >= wait:
        wait += delay
        startProgram()

