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

heart3 = Image("07070:"
               "77777:"
               "77777:"
               "07770:"
               "00700")

hearts = [heart1, heart2, heart3]
display.show(hearts, loop=True, delay=500)
