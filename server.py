import socket

class Server():
    def __init__(self) -> None:
        self.address = self.get_ip()
        self.client_connected = False
        
        if self.address == None:
            self.address = self.get_ip

    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    # def start_server(self):
