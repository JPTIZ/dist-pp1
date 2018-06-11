'''Contains distributed system abstractions.'''
from typing import NamedTuple
from datetime import datetime
from enum import Enum
import random
import uuid


class Token:
    '''Token for aquiring access to resource in mutual-exclusion algorithms.'''
    def __init__(self):
        self.uuid = uuid.uuid4()

class State(Enum):
    '''A process's current state.'''
    IDLE = 0
    WAIT = 1
    WORK = 2


class MessageType(Enum):
    '''Type of message passed between processes.'''
    PASS = 0
    REQUEST = 1
    RECEIVED = 2


class Message(NamedTuple):
    '''Message passed between processes.'''
    token: Token
    type: MessageType


class Process:
    '''Emulates a computer process.'''
    def __init__(self, pid, timestamp):
        self.pid = pid
        self.timestamp = datetime.now()
        self.token = Token()
        self.state = State.IDLE

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
