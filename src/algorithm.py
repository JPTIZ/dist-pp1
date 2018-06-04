'''Handles different mutual-exclusion algorithms.'''


def token_ring():
    '''Starts token ring algorithm.'''
    print("Now we enter the token ring zone")

def server_based():
    '''Starts server-based algorithm.'''
    print("Now we enter the server based distribution zone")

def multicast():
    '''Starts multicast algorithm.'''
    print("Now we enter the multicast zone")


ALGORITHMS = {
    'token_ring': token_ring,
    'server_based': server_based,
    'multicast': multicast
}
