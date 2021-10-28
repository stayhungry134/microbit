"""
Author：Ethan
Date:2021/07/12

用于模拟警车音效，播放指定频率的音
"""

import music

while True:
    # 880 到 1760 以步长为 16 生成数值
    for freq in range(880, 1760, 16):
        # music.pitch[频率，持续时间(毫秒为单位)]
        music.pitch(freq, 6)
    for freq in range(1760, 880, -16):
        music.pitch(freq, 6)
