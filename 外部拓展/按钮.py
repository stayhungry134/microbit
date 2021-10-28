"""
Author：Ethan
Date:2021/07/13
 外部按钮，按钮 VCC 接正极，GND 接 GND，OUT 接 p5(按钮A) 或者 p11(按钮B)
"""

from microbit import *

while True:
    if button_a.is_pressed():
        display.show("B")
    if button_b.is_pressed():
        display.show("G")
