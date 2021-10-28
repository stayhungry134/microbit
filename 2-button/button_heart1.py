from microbit import *

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
while True:
    if button_a.was_pressed():
        display.show(heart1)
    if button_b.was_pressed():
        display.show(heart2)
