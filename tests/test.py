from MultiWii import MultiWii
from getkey import getkey, keys
import threading

def __key_control():
        while True:
            key = getkey()
            if key == 'l':
                board1.init_arm()
                board2.init_arm()
            if key == 'm':
                board1.init_disarm()
            if key == 'p':
                board2.init_disarm()
            if key == 'w':
                board1.channel[2] += 5
                board2.channel[2] += 5
                print(board1.channel)
            if key == 's':
                board1.channel[2] -= 5
                board2.channel[2] -= 5
                print(board1.channel)
            if key == 'a':
                board1.channel[0] += 5
                board2.channel[0] += 5
                print(board1.channel)
            if key == 'd':
                board1.channel[0] -= 5
                board2.channel[0] -= 5
                print(board1.channel)
            if key == 'y':
                board1.channel[1] += 5
                board2.channel[1] += 5
                print(board1.channel)
            if key == 'h':
                board1.channel[1] -= 5
                board2.channel[1] -= 5
                print(board1.channel)
            if key == 'g':
                board1.channel[3] += 5
                board2.channel[3] += 5
                print(board1.channel)
            if key == 'j':
                board1.channel[3] -= 5
                board2.channel[3] -= 5
                print(board1.channel)
            elif key != 'p' and key != 'm':
                board1.send_cmd(board1.MSP["SET_RAW_RC"],board1.channel)
                board2.send_cmd(board2.MSP["SET_RAW_RC"],board2.channel)
            

UDP_IP1 = "192.168.43.4"
UDP_PORT1 = 8888

UDP_IP2 = "192.168.43.3"
UDP_PORT2 = 8888

board1 = MultiWii(UDP_IP1, UDP_PORT1)
board1.init_ping()

board2 = MultiWii(UDP_IP2, UDP_PORT2)
board2.init_ping()

key_control = threading.Thread(target = __key_control)
key_control.start()