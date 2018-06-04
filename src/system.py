'''Contains distributed system abstractions.'''
from datetime import datetime
from enum import Enum
from typing import Callable, List, NamedTuple
import random


class Token:
    '''Token for aquiring access to resource in mutual-exclusion algorithms.'''
    def __init__(self, seed: int = None):
        if seed is not None:
            random.seed(seed) # uses given seed for the randomizer
        else:
            random.seed() # uses system time as seed

        self.token_id = random.randint(0, 999999)


class State(Enum):
    '''A process's current state.'''
    IDLE = 0
    WAIT = 1
    WORK = 2


class MessageType(Enum):
    '''Type of message passed between processes.

    PASS: Just passing token forward.
    REQUEST: Requesting to enter critical region.
    RECEIVED: Received access to critical region.
    '''
    PASS = 0
    REQUEST = 1
    RECEIVED = 2


class Message(NamedTuple):
    '''Message passed between processes.'''
    token: Token
    type: MessageType


class Process(NamedTuple):
    '''Emulates a computer process.'''
    pid: int
    timestamp: datetime = datetime.now()
    token: Token = 0 # TODO generate token later
    state: State = State.IDLE

    def request(self, index):
        '''Request data in an array index.'''
        self.state = State.WAIT
        self.token = index

    def waiting(self):
        '''Whether the process is waiting or not.'''
        return self.state == State.WAIT

    def receive(self, msg):
        '''Receives token message.'''
        if self.waiting() and msg.token == self.token:
            self.state = State.WORK
            return Message(token=msg.token, type=MessageType.RECEIVED)
        return msg


class Server(NamedTuple):
    processes: List[Process]
