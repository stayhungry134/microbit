from microbit import *

# 创建三个心形图形
heart1 = Image("01010:"
               "10101:"
               "10001:"
               "01010:"
               "00100")

heart2 = Image("04040:"
               "44444:"
               "44044:"
               "04440:"
               "00400")

heart3 = Image("07070:"
               "77777:"
               "77777:"
               "07770:"
               "00700")
# is_pressed，was_pressed,
# get_presses，获取按下的次数
while True:
    # 如果 a 键被按下，显示心2
    if button_a.is_pressed():
        display.show(heart2)
    # 如果 b 键被按下，显示心3
    if button_b.is_pressed():
        display.show(heart3)
    else:
        display.show(heart1)
