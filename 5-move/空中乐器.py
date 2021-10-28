"""
Author：Ethan
Date:2021/07/12

通过改变 microbit 的位置来形成不同频率的音符并播放
"""

from microbit import *
import music

while True:
    # 分别获取 X, Y, Z 上面的数值, 如果为负值，会报错并停止播放
    x = abs(accelerometer.get_x())
    y = abs(accelerometer.get_y())
    z = abs(accelerometer.get_z())
    music.pitch((x * 1 + y * 2 + z * 3) // 6, 10)
    # 如果按下 A 键，停止循环
    if button_a.is_pressed():
        break
    # music.pitch(y, 10)