from microbit import *

while True:
    if pin1.is_touched():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)