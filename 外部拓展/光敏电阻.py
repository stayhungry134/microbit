"""
Author：Ethan
Date:2021/07/12

"""

from microbit import *

# Write your code here :-)

while True:
    display.scroll(str(pin0.read_analog()))
