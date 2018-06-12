'''Simulation of mutual exclusion algorithms.'''
from algorithm import ALGORITHMS
from sys import argv


def main(algorithm: str = 'token_ring',
         n_processes: int = 10):
    '''Initializes simulation.'''
    print('------------------------------------\n'
          'Mutual exclusion algorithm simulator\n'
          f'Using Algorithm: {algorithm}\n'
          '------------------------------------\n')

    ALGORITHMS[algorithm](n_processes=n_processes)


if __name__ == '__main__':
    try:
        ALGORITHM = argv[1]
    except IndexError:
        ALGORITHM = 'token_ring'
    main(algorithm=ALGORITHM)
