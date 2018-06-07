'''Simulation of mutual exclusion algorithms.'''
import re
import random
# from carl import command
from sys import argv

from system import Process
from system import Token 
from itertools import cycle 





def token_ring(processes:list, current_token, message):
    print('------------------------------------')
    print('\nStarting Token Ring simulation:\n')
    print('------------------------------------')

    processes[0].generateNewToken()
    print(f'Generated token {processes[0].token.uuid} for process PID {processes[0].pid:04}')
    current_token = processes[0].token 

    ring = cycle(processes)

   
    done = False 
    current_proc = next(ring)
    iteractions = 0
    while not done:

        # a random process tries to do some work 
        rand_proc = random.choice(processes)
        print(f'Process {rand_proc.pid:04} is trying to access the critical section.\n')
        if rand_proc.token is None:
            print(f'Process {rand_proc.pid:04}: access denied')
        elif rand_proc.token == current_token:
            print(f'Process {rand_proc.pid:04} token verified, access granted.')
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
    print('Final result: ')
    print('-------------------------------------------------------------\n')        
    print(message)


def main(algorithm: str = 'token_ring',
         n_processes: int = 10):
    '''Initializes simulation.'''
    print('------------------------------------')
    print('Mutual exclusion algorithm simulator')
    print(f'Using Algorithm: {algorithm}')
    print('------------------------------------\n')

    current_token = None
    message = ""

    processes = [Process(pid=i, timestamp=0)
                 for i in range(n_processes)]

    for process in processes:
        print(f'Initialized process PID {process.pid:04}')
    
    if algorithm == 'token_ring':
        token_ring(processes, current_token, message)

    # head = '|'
    # for process in processes:
    #     head += f' PID {process.pid:04} |'
    # line = re.sub(r'(?!\|).', '-', head)

    # print(line)
    # print(head)
    # print(line)



    # while True:
    #     for process in processes:
    #         print(f'| {process.state} '.replace('State.', ''), end='')
    #     print('|')
    #     # print(f'Updating process (PID={process.pid})')


if __name__ == '__main__':
    try:
        ALGORITHM = argv[1]
    except IndexError:
        ALGORITHM = 'token_ring'
    main(algorithm=ALGORITHM)
