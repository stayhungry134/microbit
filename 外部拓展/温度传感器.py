"""
Author：Ethan
Date:2021/07/13
通过温度传感器读取数据，并用四位数码管展示，
温度传感器上面 AO 表示 模拟信号，DO 表示数字信号
"""
from microbit import *
import math


while True:
    analogVal = pin0.read_analog()
    Vr = 3.3 * float(analogVal)/1023
    Rt = 10000 * Vr / (3.3-Vr)
    temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
    tem = temp - 273.15
    display.show('{:.2f}'.format(tem))
    sleep(1000)
    display.show('-')
    sleep(1000)