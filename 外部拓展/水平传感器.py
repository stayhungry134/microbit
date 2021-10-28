"""
Author：Ethan
Date:2021/07/13
VCC 3.3V，GND 接地，DO 接 pin n

读取获得的值，如果前面的传感器水平，显示 1，如果前面的传感器倾斜，显示 0
"""

from microbit import *

while True:
    img = pin5.read_digital()
    display.show(str(img))
