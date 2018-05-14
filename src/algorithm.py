from enum import Enum

class Algorithm:
    def __init__(self):
        self.algorithms = {'token_ring': self.token_ring,
                    'server_based': self.server_based,
                    'multicast': self.multicast}
    
    def token_ring(self):
        print("Now we enter the token ring zone")
        pass
    def server_based(self):
        print("Now we enter the server based distribution zone")
        pass 
    def multicast(self):
        print("Now we enter the multicast zone")
        pass    

    