"""
Author：Ethan
Date:2021/07/13
microbit 下部的接口的函数和方法

模拟信号和数字信号的区别：数字信号是离散型的，模拟信号是连续性的
read_digital: 读取数字信号 1 和 0（高电位或低电位）
read_analog：读取模拟信号 0 - 1023

write_digital()：写入信号，1 代表启动，0 代表 关闭
write_analog()：写入信号，0-1023，1023 代表 3.3 V

更多请自行查看文档
"""

from microbit import *

pin0.read_analog()