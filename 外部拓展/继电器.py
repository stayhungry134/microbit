"""
Author：Ethan
Date:2021/07/13
DC+：正极，DC-：负极，IN：信号输入
NO：常开，COM：公共端，NC：常闭
"""

from microbit import *

while True:
    if button_a.is_pressed():
        display.show("R")
        pin0.write_digital(1)
    if button_b.is_pressed():
        pin0.write_digital(0)
        display.show("L")


# pin0.write_digital(1)