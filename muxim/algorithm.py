'''Handles different mutual-exclusion algorithms.'''
from itertools import cycle
from typing import NamedTuple
import itertools
import random

from system import Message, MessageType, Process, Server, Token


DEFAULT_PROCESS_COUNT = 10


def random_free_process(server: Server):
    '''
    Chooses random process that does not contains a token. Returns `None` if no
    process is free.
    '''
    try:
        return random.choice([p for p in server.processes
                              if p is not server.leader and p.token is None])
    except IndexError as e:
        print('indexerror: {e}')
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
    '''
    Generates `n_processes` random processes.
    '''
    return[Process(pid=i, timestamp=0)
           for i in range(n_processes)]


def token_ring(n_processes: int = DEFAULT_PROCESS_COUNT):
    print('------------------------------------'
          '\nStarting Token Ring simulation:\n'
          '------------------------------------')

    server = Server(processes=generate_processes(n_processes))
    processes = server.processes

    message = ''

    for process in processes:
        process.token = Token()
        print(f'Initialized process PID {process.pid:04}')

    processes[0].token = Token()
    print(f'Generated token {processes[0].token.uuid}'
          f' for process PID {processes[0].pid:04}')
    current_token = processes[0].token

    ring = cycle(processes)

    done = False
    current_proc = next(ring)
    iteractions = 0

    while not done:
        # a random process tries to do some work
        rand_proc = random.choice(processes)
        print(f'Process {rand_proc.pid:04}'
              f' is trying to access the critical section.\n')

        if rand_proc.token is None:
            print(f'Process {rand_proc.pid:04}: access denied')
        elif rand_proc.token == current_token:
            print(f'Process {rand_proc.pid:04} token verified,'
                  f' access granted.')
            message += f'Proccess {rand_proc.pid:04} was here!\n'
            print(f'Process {rand_proc.pid:04} leaves the critical section\n')
            iteractions += 1
        else:
            print(f'Process {rand_proc.pid:04}: invalid token')

        # cycle the token through processes
        if current_proc.token is not None:
            print(f'{current_proc.pid:04} has token {current_proc.token.uuid}')
            token = current_proc.token
            current_proc.token = None

            current_proc = next(ring)
            current_proc.token = token
            print(f'Passing token to {current_proc.pid:04}')

        else:
            print('THE TOKEN HAS BEEN LOST.')
            done = True

        if iteractions > 30:
            done = True
    print('Final result: \n'
          '-------------------------------------------------------------\n')
    print(message)


def server_based(n_processes: int = DEFAULT_PROCESS_COUNT,
                 random_execution: bool = False):
    '''Starts server-based algorithm.'''
    def elect_leader(server: Server):
        '''Elects a random process as server's leader.'''
        leader = random.randint(0, len(server.processes) - 1)
        server.processes[leader].token = token
        return server.processes[leader]

    def make_request(requester, index, receiver=None):
        '''Makes process request access to specified index.'''
        if requester not in receiver.requests:
            print(f'{requester} is requesting access to index {index}')
            requester.request()
            receiver.requests.append(requester)

    def update(server):
        '''Updates server processes.'''
        leader = server.leader
        if random_execution:
            random.shuffle(server.processes)
        processes = server.processes

        for process in processes:
            print(f'\nUpdating {process}')
            if process in leader.requests:
                print('    Waiting for token')
                continue

            if process == leader and process.token is not None:
                print('    Leader is going to pass token forward')
                try:
                    requester = leader.requests.popleft()
                    requester.receive(Message(type=MessageType.RECEIVED,
                                              token=token))
                    leader.token = None
                    print(f'    Passed token to PID {requester.pid}')
                except IndexError:
                    print('    No one to give token')
                continue

            if process.token:
                if process.used_token and random.random() > 0.5:
                    print('    Done! Giving token back.')
                    leader.token, process.token = process.token, None
                    process.used_token = False
                else:
                    print('    Working with token')
                    process.used_token = True
            else:
                print('    Just working')
        print()

    def print_iter(i: int):
        '''Prints iteration heading.'''
        title = f'Iteration {i+1}'
        print('-'*80 + '\n' +
              f'{title:^80}' + '\n' +
              '-'*80)

    def print_requests(server: Server):
        '''Shows leader's requests.'''
        requests = server.leader.requests
        print(f'Leader (PID {server.leader.pid}) requests: '
              f'{[f"PID {request.pid}" for request in requests]}')

    print('Now we enter the server-based distribution zone')
    token = Token()
    server = Server(processes=generate_processes(n_processes))
    server.leader = elect_leader(server)

    for process in server.processes:
        process.used_token = False

    print(f'Leader: {server.leader}.\n')

    for i in itertools.count():
        print_iter(i)

        for _ in range(random.randint(0, 3)):
            make_request(random_free_process(server),
                         random.randint(1, 10),
                         receiver=server.leader)

        print_requests(server)
        update(server)

        if random_execution:
            server.processes.sort(key=lambda p: p.pid)
        print_requests(server)
        print('PID: | ' + ' | '.join(f'{proc.pid!s:^3.3}'
                                     for proc in server.processes) + ' | ')
        print('Tok: | ' + ' | '.join(f'{proc.token.uuid!s:^3.3}'
                                     if proc.token else f'{"-":^3.3}'
                                     for proc in server.processes) + ' | ')

        while True:
            try:
                ans = input('\n(C)ontinue or (q)uit: ').lower()
            except EOFError:
                print()
                ans = 'q'

            if not ans or ans == 'c':
                break
            elif ans == 'q':
                print('End of simulation.')
                return
            else:
                print(f'Unknown command {ans}')


def multicast(n_processes: int = DEFAULT_PROCESS_COUNT):
    '''Starts multicast algorithm.'''
    print('Now we enter the multicast zone')
    print(n_processes)


ALGORITHMS = {
    'token_ring': token_ring,
    'server_based': server_based,
    'multicast': multicast
}
