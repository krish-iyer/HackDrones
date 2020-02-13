import time, struct, socket, threading

class MultiWii:
    
    MSP = {
        "ATTITUDE" : 108,
        "SET_RAW_RC" : 200
    }

    def __init__(self, UDP_IP, UDP_PORT):
        self.UDP_IP = UDP_IP
        self.UDP_PORT = UDP_PORT
        self.data_arm = [1500,1500,1000,1500, 1000,0,0,0]
        self.data_disarm = [1500,1500,1000,1500,1300,0,0,0]
        self.data_disarm_test = [1500,1500,1000,1500,1000,0,0,0]
        self.channel = [1500,1500,1000,1500,1300,0,0,0]
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def init_ping(self):
        self.ping = threading.Thread(target = self.__ping)
        self.ping.start()

    def init_arm(self):
            
        self.__arm(self.data_arm)
        print ("Board is armed now!")
        print ("In 3 seconds it will disarm...")
        self.__arm(self.data_disarm)

    def init_disarm(self):
        self.__arm(self.data_disarm_test)

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

    def send_cmd(self, code, data):
        checksum = 0
        if len(data):
            data_= []
            for i in range(len(data)):
                binary = '{0:016b}'.format(data[i])
                data_.append(int(binary[8:], 2))
                data_.append(int(binary[:8], 2))
            data = data_
        total_data = ['$'.encode('utf-8'), 'M'.encode('utf-8'), '<'.encode('utf-8'), len(data), code] + data
        for i in struct.pack('<2B' + '%dB' % len(data), *total_data[3:len(total_data)]):
            checksum = checksum ^ i
        total_data.append(checksum)
        self.sock.sendto(struct.pack('<3c2B'+ '%dB' % len(data) + 'B', *total_data), (self.UDP_IP, self.UDP_PORT))

    def __arm(self, data):
        timer = 0
        start = time.time()
        while timer < 0.25:
            self.send_cmd(self.MSP["SET_RAW_RC"],data)
            time.sleep(1)
            timer = timer + (time.time() - start)
            start =  time.time()
