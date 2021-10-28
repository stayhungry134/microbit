"""
Author：Ethan
Date:2021/07/12
用于测试 microbit 的移动
x 轴：左右倾斜
y 轴：前后倾斜
z 轴：上下移动

每个轴返回一个正数或负数，表示 1‰ * g（重力），当读书为 0 时，该轴为 leavel 状态
"""

from microbit import *

while True:
    # 运用 get_x 来测量该设备沿 X 轴的水平程度
    reading = accelerometer.get_x()
    if reading > 20:
        display.show("R")
    elif reading < -20:
        display.show("L")
    else:
        display.show("-")
