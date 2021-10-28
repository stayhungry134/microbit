"""
Author：Ethan
Date:2021/07/12
microbit 自带的电子罗盘可以指出朝北的方向
"""

from microbit import *

# 使用之前需要校准
# 将 microbit 倾斜，直到它在显示屏的外缘绘制出一圈有效像素
compass.calibrate()

while True:
    # 应用数学公式，计算出显示的时针的数值，使其大致指向北方
    needle = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])
