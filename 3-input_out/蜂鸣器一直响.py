"""
Author：Ethan
Date:2021/07/12
引脚 0 的电线接到有源蜂鸣器的正极，引脚 GND 的电线连接到负极
有源蜂鸣器和无源蜂鸣器的区别是，
    有源蜂鸣器接通电源就能够发声音
    无源蜂鸣器需要不断的改变电位
"""

from microbit import *
# 1 代表启动，0 代表关闭
pin0.write_digital(1)
