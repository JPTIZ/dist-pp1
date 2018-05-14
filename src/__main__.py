'''Simulation of mutual exclusion algorithms.'''
import re
# from carl import command
from sys import argv

from system import Process


def main(algorithm: str='ring',
         n_processes: int=10):
    processes = [Process(pid=i, timestamp=0)
                 for i in range(n_processes)]

    head = '|'
    for process in processes:
        head += f' PID {process.pid:04} |'
    line = re.sub(r'(?!\|).', '-', head)

    print(line)
    print(head)
    print(line)

    while True:
        for process in processes:
            for process in processes:
                print(f'| {process.state} '.replace('State.', ''), end='')
            print('|')
            pass
            # print(f'Updating process (PID={process.pid})')


if __name__ == '__main__':
    try:
        algorithm = argv[1]
    except IndexError:
        algorithm = 'ring'
    main(algorithm=algorithm)
