'''Contains distributed system abstractions.'''
from collections import deque
from datetime import datetime
from enum import Enum
from typing import List, NamedTuple
import uuid

from dataclasses import dataclass


class Token:
    '''Token for aquiring access to resource in mutual-exclusion algorithms.'''
    def __init__(self):
        self.uuid = uuid.uuid4()

    def __repr__(self):
        return f'Token({self.uuid})'


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


@dataclass
class Process:
    '''Emulates a computer process.'''
    pid: int
    timestamp: datetime
    token: Token = None
    state: State = State.IDLE
    requests: deque = deque()

    def request(self):
        '''Request data in an array index.'''
        self.state = State.WAIT

    def waiting(self):
        '''Whether the process is waiting or not.'''
        return self.state == State.WAIT

    def receive(self, msg):
        '''Receives token message.'''
        if self.waiting():
            self.state = State.WORK
            self.token = msg.token

    def __repr__(self):
        return f'Process(PID={self.pid}, token={self.token})'


@dataclass
class Server:
    processes: List[Process]
