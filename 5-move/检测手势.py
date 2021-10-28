"""
Author：Ethan
Date:2021/07/12
移动 microbit 来让其检测处于什么位置
向上(up)，向下(down)，向左(left)，向右(right)，正面朝上(face up)，正面朝下(face down)
自由落体(freefall)，3g(3g)，6g(6g)，8g(8g)，摇动(shake)
"""

from microbit import *

while True:
    gesture = accelerometer.current_gesture()
    # 如果 A 被按下，显示空，终止循环
    if button_a.is_pressed():
        display.clear()
        break
    else:
        if gesture == "face up":
            display.show(Image.HAPPY)
        else:
            display.show(Image.ANGRY)
