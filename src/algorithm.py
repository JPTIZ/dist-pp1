'''Handles different mutual-exclusion algorithms.'''
class Algorithm:
    '''A single algorithm.'''

    def __init__(self):
        self.algorithms = {'token_ring': self.token_ring,
                           'server_based': self.server_based,
                           'multicast': self.multicast}

    def token_ring(self):
        '''Starts token ring algorithm.'''
        print("Now we enter the token ring zone")

    def server_based(self):
        '''Starts server-based algorithm.'''
        print("Now we enter the server based distribution zone")

    def multicast(self):
        '''Starts multicast algorithm.'''
        print("Now we enter the multicast zone")
