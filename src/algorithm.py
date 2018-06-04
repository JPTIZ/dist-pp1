'''Handles different mutual-exclusion algorithms.'''
from typing import NamedTuple
import random

from system import Process, Server


DEFAULT_PROCESS_COUNT = 10


class Simulation(NamedTuple):
    '''Contains simulation parameters.'''

    n_processes: int = DEFAULT_PROCESS_COUNT
    algorithm: str = 'token_ring'

    def start(self):
        '''Starts simulation.'''
        ALGORITHMS[self.algorithm](n_processes=self.n_processes)

    def halt(self):
        '''Halts simulation and returns data.'''
        return {'params': self, 'data': 'No data'}


def generate_processes(n_processes):
    '''Generates `n_processes` random processes.'''
    return[Process(pid=i, timestamp=0)
           for i in range(n_processes)]



def token_ring(n_processes: int = DEFAULT_PROCESS_COUNT):
    '''Starts token ring algorithm.'''
    print('Now we enter the token ring zone')
    print(n_processes)

def server_based(n_processes: int = DEFAULT_PROCESS_COUNT):
    '''Starts server-based algorithm.'''
    print('Now we enter the server based distribution zone')
    server = Server(processes=generate_processes(n_processes))
    leader = random.choice(server.processes)
    print(f'Leader PID: {leader.pid}.')


def multicast(n_processes: int = DEFAULT_PROCESS_COUNT):
    '''Starts multicast algorithm.'''
    print('Now we enter the multicast zone')
    print(n_processes)


ALGORITHMS = {
    'token_ring': token_ring,
    'server_based': server_based,
    'multicast': multicast
}
