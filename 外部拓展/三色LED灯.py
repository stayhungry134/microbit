"""
Author：Ethan
Date:2021/07/13
三色LED灯有四个接口，R，G，B，GND，分别表示红，绿，蓝三个通道和接地
通过控制三个通道输入的电压来控制各通道的亮度
"""

from microbit import *

pin0.write_analog(1000)
pin1.write_analog(1000)
pin2.write_analog(1000)