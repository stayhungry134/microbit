"""
Author：Ethan
Date:2021/07/13
双色 LED 灯，负极接到 GND
"""

from microbit import *

while True:
    # 写入数字信号，1 代表启动，3.3V，0 表示关闭
    # pin0.write_digital(1)
    # pin1.write_digital(0)
    # sleep(1000)
    # pin1.write_digital(1)
    # pin0.write_digital(0)
    # sleep(1000)

    # 写入的信号不同，表示电压不同，LED 的亮度也会不同
    pin0.write_analog(100)
    pin1.write_analog(0)
    sleep(1000)
    pin1.write_analog(100)
    pin0.write_analog(0)
    sleep(1000)
