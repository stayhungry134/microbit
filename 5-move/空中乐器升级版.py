"""
Author：Ethan
Date:2021/07/12
通过选取音符的格式来播放音乐
"""

from microbit import *
import music

# C#:F
# 音符
note = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']
# 音高
pitch = ['2', '3', '4', '5', '6']
# 音长
length = ['2', '3', '4', '5']

# 开始空中乐器
while True:
    # 获取 X, Y, Z 轴的数值
    x = abs(accelerometer.get_x())
    y = abs(accelerometer.get_y())
    z = abs(accelerometer.get_z())
    # X 轴控制音符，Y 轴控制音高，Z 轴控制音长
    tune = '{}{}:{}'.format(note[x % 9], pitch[y % 5], length[z % 4])
    # 为保证音符正常播放，每次循环停顿 1 秒
    # sleep(100)
    # 如果按下 A 键，循环停止
    if button_a.is_pressed():
        break
    music.play(tune)
