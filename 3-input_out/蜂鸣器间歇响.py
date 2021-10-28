"""
Author：Ethan
Date:2021/07/12

通过给 microbit 休眠循环，以达到蜂鸣器间歇响的效果
"""

from microbit import *

while True:
    # pin0 启动
    pin0.write_digital(1)
    # 休眠20毫秒
    sleep(20)
    # pin0 关闭
    pin0.write_digital(0)
    # 休眠 480 毫秒（加上上面的 20 毫秒，500 毫秒，一秒钟响两次）
    sleep(480)
