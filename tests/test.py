from MultiWii import MultiWii
from getkey import getkey, keys
import threading

def __key_control():
        while True:
            key = getkey()
            if key == 'l':
                board1.init_arm()
            if key == 'm':
                board1.init_disarm()
            if key == 'w':
                board1.channel[2] += 5
                print(board1.channel)
            if key == 's':
                board1.channel[2] -= 5
                print(board1.channel)
            if key == 'a':
                board1.channel[0] += 5
                print(board1.channel)
            if key == 'd':
                board1.channel[0] -= 5
                print(board1.channel)
            if key == 'y':
                board1.channel[1] += 5
                print(board1.channel)
            if key == 'h':
                board1.channel[1] -= 5
                print(board1.channel)
            if key == 'g':
                board1.channel[3] += 5
                print(board1.channel)
            if key == 'j':
                board1.channel[3] -= 5
                print(board1.channel)
            # channel_= []
            # for i in range(len(board1.channel)):
            #     binary = '{0:016b}'.format(board1.channel[i])
            #     channel_.append(int(binary[8:], 2))
            #     channel_.append(int(binary[:8], 2))
            # board1.send_cmd(16,board1.MSP["SET_RAW_RC"],channel_,'16B')

            # if key == 'L':
            #     board2.init_arm()
            # if key == keys.UP:
            #     board2.channel[2] += 5
            #     print(board2.channel)
            # if key == keys.DOWN:
            #     board2.channel[2] -= 5
            #     print(board2.channel)
            # if key == keys.LEFT:
            #     board2.channel[0] += 5
            #     print(board2.channel)
            # if key == keys.RIGHT:
            #     board2.channel[0] -= 5
            #     print(board2.channel)
            # if key == 'f':
            #     board2.channel[1] += 5
            #     print(board2.channel)
            # if key == 'v':
            #     board2.channel[1] -= 5
            #     print(board2.channel)
            # if key == 'c':
            #     board2.channel[3] += 5
            #     print(board2.channel)
            # if key == 'b':
            #     board2.channel[3] -= 5
            #     print(board2.channel)
            # channel_= []
            # for i in range(len(board2.channel)):
            #     binary = '{0:016b}'.format(board2.channel[i])
            #     channel_.append(int(binary[8:], 2))
            #     channel_.append(int(binary[:8], 2))
            # board2.send_cmd(16,board2.MSP["SET_RAW_RC"],channel_,'16B')

            

UDP_IP1 = "192.168.43.4"
UDP_PORT1 = 8888

# UDP_IP2 = "192.168.43.4"
# UDP_PORT2 = 8888l

board1 = MultiWii(UDP_IP1, UDP_PORT1)
board1.init_ping()

# board2 = MultiWii(UDP_IP2, UDP_PORT2)
# board2.init_ping()

key_control = threading.Thread(target = __key_control)
key_control.start()