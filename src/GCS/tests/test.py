#!/usr/bin/env python3

"""test.py: To test the MultiWii package."""

__author__ = "B Krishnan Iyer, Meher Madhu"
__copyright__ = "Copyright 2020 HackDrones"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "B Krishnan Iyer"
__email__ = "krishnaniyer97@gmail.com"
__status__ = "Development"

from MultiWii import MultiWii
from getkey import getkey, keys
import time
import threading

def __key_control():
    while True:
        key = getkey()
        if key == 'l':
            board1.arm()
            # board2.init_arm()
            board1.channel = [1500,1500,1000,1500,1300,0,0,0]
            # board2.channel = [1500,1500,1000,1500,1300,0,0,0]
        if key == 'q':
            board1.disarm()
        if key == 'h':
            board1.channel[5] = 1300
        if key == 'w':
            board1.channel[2] += 10
            # board2.channel[2] += 5
            print(board1.channel)
        if key == 's':
            board1.channel[2] -= 10
            # board2.channel[2] -= 5
            print(board1.channel)
        if key == keys.UP:
            board1.channel[1] += 1
            # board2.channel[0] += 5
            print(board1.channel)
        if key == keys.DOWN:
            board1.channel[1] -= 1
            # board2.channel[0] -= 5
            print(board1.channel)
        if key == keys.RIGHT:
            board1.channel[0] += 1
            # board2.channel[0] += 5
            print(board1.channel)
        if key == keys.LEFT:
            board1.channel[0] -= 1
            # board2.channel[0] -= 5
        elif key != 'q' and key != 'l' and key != 'h':
            board1.send_cmd(board1.MSP["SET_RAW_RC"], board1.channel)
            # board2.__send_cmd(# board2.MSP["SET_RAW_RC"],# board2.channel)

UDP_IP1 = "192.168.43.4"
UDP_PORT1 = 8888

# UDP_IP2 = "192.168.43.3"
# UDP_PORT2 = 8888


board1 = MultiWii(UDP_IP1, UDP_PORT1)

# # board2 = MultiWii(UDP_IP2, UDP_PORT2)
# # board2.init_ping()
# board1.arm()

key_control = threading.Thread(target = __key_control)
key_control.start()

# board1.init_alt()
