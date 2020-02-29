import time, struct, socket, threading, atexit

class MultiWii:
    
    MSP = {
        "ATTITUDE"      : 108,
        "SET_RAW_RC"    : 200,
        "ALTITUDE"      : 109
    }

    def __init__(self, UDP_IP, UDP_PORT):
        self.UDP_IP = UDP_IP
        self.UDP_PORT = UDP_PORT
        self.arm_data = [1500,1500,1000,1500,1300,1000,0,0]
        self.disarm_data = [1500,1500,1000,1500,1000,1000,0,0]
        self.safe_arm = [1500, 1500, 1000, 1500, 1000, 1000, 0, 0]
        self.channel = [1500,1500,1000,1500,1300,1300,0,0]
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.data = [0,0,0,0,0,0,0,0,0,0,0,0]
        # self.alt_hold_data = [1500,1500,1000,1500,1300,1300,0,0]
        self.threadLock = threading.Lock()
    #    atexit.register(self.disarm)
    # TODO: this can be reused
    def init_ping(self):
        self.ping = threading.Thread(target = self.__ping)
        self.ping.start()

    # TODO: def __ping(self): figure out with open UDP ports based on the give IP might have to use System modules
    # or else it affects the communication with the module
    
    def __ping(self):
        self.sock.settimeout(2)
        while True:
            self.sock.sendto("ping".encode(), (self.UDP_IP, self.UDP_PORT))
            try:
                data, addr = self.sock.recvfrom(4)
                if  data.decode() == "pong":
                    print("alive" + str(addr))
                    time.sleep(0.5)
            except:
                print("dead")
            #time.sleep(2)
    
    def init_alt(self):
        self.alt =  threading.Thread(target = self.get_alt)
        self.alt.start()

    def send_cmd(self, code, data):
        checksum = 0
        if len(data):
            data_= []
            for i in range(len(data)):
                tmp = int('{0:016b}'.format(data[i]), 2)
                MSB = tmp & 0x00FF
                LSB = tmp >> 8
                checksum = checksum ^ MSB
                checksum = checksum ^ LSB
                data_[len(data_):] = [MSB, LSB]
            data = data_

        checksum = checksum ^ len(data)
        checksum = checksum ^ code

        total_data = ['$'.encode('utf-8'), 'M'.encode('utf-8'), '<'.encode('utf-8'), len(data), code] + data

        total_data.append(checksum)
        self.sock.sendto(struct.pack('<3c2B'+ '%dB' % len(data) + 'B', *total_data), (self.UDP_IP, self.UDP_PORT))

    def arm(self):
        self.send_cmd(self.MSP["SET_RAW_RC"],self.safe_arm)
        time.sleep(0.25)
        self.send_cmd(self.MSP["SET_RAW_RC"],self.arm_data)
    
    def disarm(self):
        self.send_cmd(self.MSP["SET_RAW_RC"],self.disarm_data)

    def alt_hold(self):
        self.send_cmd(self.MSP["SET_RAW_RC"],self.alt_hold_data)

    def get_alt(self):
        while True:
            # self.threadLock.acquire()
            try:
                self.send_cmd(self.MSP["ATTITUDE"],[])
                self.data = self.sock.recv(12) # buffer size is 1024 bytes  
                alt_values = struct.unpack('hhh', self.data[5:11])
                print(alt_values)
            except:
                print("data error")
            time.sleep(0.5)
            
        # self.threadLock.release()

