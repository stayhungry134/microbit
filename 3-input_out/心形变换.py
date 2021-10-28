from microbit import *

heart1 = Image("03030:"
               "30303:"
               "30003:"
               "03030:"
               "00300")

heart2 = Image("00300:"
               "03030:"
               "30003:"
               "30303:"
               "03030")

while True:
    # 当 P0 与 GND 接通的时候，显示 heart2
    if pin0.is_touched():
        display.show(heart2)
    else:
        display.show(heart1)
