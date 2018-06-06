'''Handles different mutual-exclusion algorithms.'''
from typing import NamedTuple
import random

from system import Message, MessageType, Process, Server, Token


DEFAULT_PROCESS_COUNT = 10


def random_free_process(server: Server):
    '''Chooses random process that does not contains a token. Returns `None` if
    no process is free.'''
    try:
        return random.choice([p for p in server.processes if p.token is None])
    except IndexError:
        return None


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
    def make_request(requester, index, receiver=None):
        '''Makes process request access to specified index.'''
        print(f'{requester} is requesting access to index {index}')
        if receiver is not None:
            requester.request()
            receiver.requests.append(requester)
        else:
            for _ in server.processes:
                pass

    def update(server, leader):
        '''Updates server processes.'''
        print('-'*80)
        for process in server.processes:
            print(f'Updating {process}')
            if process == leader and process.token is not None:
                try:
                    requester = process.requests.popleft()
                    requester.receive(Message(type=MessageType.RECEIVED,
                                              token=token))
                    requester.token = None
                except IndexError:
                    pass


    print('Now we enter the server based distribution zone')
    token = Token()
    server = Server(processes=generate_processes(n_processes))

    leader = random.randint(0, len(server.processes) - 1)
    server.processes[leader] = Process(pid=leader, timestamp=0, token=token)
    leader = server.processes[leader]
    print(f'Leader: {leader}.')

    make_request(random_free_process(server),
                 random.randint(1, 10),
                 leader)

    update(server, leader)

    for proc in server.processes:
        print(proc)

    make_request(random_free_process(server),
                 random.randint(1, 10),
                 leader)

    print(f'Leader requests: {leader.requests}')

    update(server, leader)

    for proc in server.processes:
        print(proc)


def multicast(n_processes: int = DEFAULT_PROCESS_COUNT):
    '''Starts multicast algorithm.'''
    print('Now we enter the multicast zone')
    print(n_processes)


ALGORITHMS = {
    'token_ring': token_ring,
    'server_based': server_based,
    'multicast': multicast
}
