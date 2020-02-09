import time, struct, socket, threading
from getkey import getkey, keys

class MultiWii:
    
    MSP = {
        "ATTITUDE" : 108,
        "SET_RAW_RC" : 200
    }

    def __init__(self, UDP_IP, UDP_PORT):
        
        self.UDP_IP = UDP_IP
        self.UDP_PORT = UDP_PORT
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def init_ping(self):
        self.ping = threading.Thread(target = self.__ping)
        self.ping.start()

    def init_key_control(self):
        self.key_control = threading.Thread(target = self.__key_control)
        self.key_control.start()

    def __ping(self):
        self.sock.settimeout(1)
        while True:
            self.sock.sendto("ping".encode(), (self.UDP_IP, self.UDP_PORT))
            try:
                data, addr = self.sock.recvfrom(4)
                if  data.decode() == "pong":
                    print("alive" + str(addr))
                    time.sleep(0.5)
            except:
                print("dead")

    def __key_control(self):
        while True:
            key = getkey()
            if key == keys.UP:
                print("working")