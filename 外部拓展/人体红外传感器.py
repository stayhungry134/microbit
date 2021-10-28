"""
Author：Ethan
Date:2021/07/14

"""

from microbit import *


def alarm():
    for i in range(10):
        pin1.write_digital(1)
        sleep(100)
        pin1.write_digital(0)
        sleep(100)


while True:
    ana = pin0.read_analog()
    display.show(str(ana))
    display.show('-')
    if ana > 100:
        alarm()
    else:
        pass
    sleep(500)