"""
Author：Ethan
Date:2021/07/13
接线：- 极接 GND，另一端接 pin n，中间不接

经过测试，600及以上 七色 LED 灯所有灯都亮，400 及一下会在七色中不断闪烁
"""
from microbit import *

pin0.write_analog(1000)
pin1.write_analog(800)
pin2.write_analog(600)
pin3.write_analog(400)
pin4.write_analog(200)