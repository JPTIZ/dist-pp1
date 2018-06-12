'''Simulation of mutual exclusion algorithms.'''
from carl import command, Arg

from algorithm import ALGORITHMS


@command
def main(algorithm: Arg(choices=['token_ring', 'server_based'],
                        help='Which algorithm to execute.') = 'token_ring',
         n_processes: int = 10):
    '''Initializes simulation.'''
    print('------------------------------------\n'
          'Mutual exclusion algorithm simulator\n'
          f'Using Algorithm: {algorithm}\n'
          '------------------------------------\n')

    ALGORITHMS[algorithm](n_processes=n_processes)


if __name__ == '__main__':
    main.run()
