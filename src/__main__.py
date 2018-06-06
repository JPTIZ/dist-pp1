'''Simulation of mutual exclusion algorithms.'''
from sys import argv

from algorithm import ALGORITHMS
# from carl import command

def main(algorithm: str = 'token_ring',
         n_processes: int = 10):
    '''Initializes simulation.'''
    print(f'Using Algorithm: {algorithm}')
    ALGORITHMS[algorithm]()


if __name__ == '__main__':
    try:
        ALGORITHM = argv[1]
    except IndexError:
        ALGORITHM = 'token_ring'
    main(algorithm=ALGORITHM)
