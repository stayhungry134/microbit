"""
    使用pycharm编写microbit之前，需要安装 pseudo-microbit
    需要添加工具 external tool uflash，
        参数：
            name: uflash,
            Group: Externam Tools
            Description: The micro:bit file flash utility
            Program: uflash
            Arguments: $FileName$
            Working directory: $FileDir$
    同时 pip install --no-cache --upgrade uflash

"""
from microbit import *

display.scroll("love xy")
