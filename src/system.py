'''Contains distributed system abstractions.'''
from typing import NamedTuple
from datetime import datetime
from enum import Enum
import random


class Token:
    def __init__(self, seed:int = None):
        if seed is not None:
            random.seed(seed) # uses given seed for the randomizer
        else:
            random.seed() # uses system time as seed

        self.id = random.randint(0, 999999)


class State(Enum):
    IDLE = 0
    WAIT = 1
    WORK = 2




class MessageType(Enum):
    PASS = 0
    REQUEST = 1
    RECEIVED = 2


class Message(NamedTuple):
    index: Token
    type: MessageType


class Process(NamedTuple):
    pid: int
    timestamp: datetime = datetime.now()
    token: Token = 0 #TODO generate token later
    state: State = State.IDLE

    def request(self, index):
        self.state = State.WAIT
        self.token = index

    def waiting(self):
        return self.state == State.WAIT

    def receive(self, index):
        if self.waiting() and index == self.token:
            self.state = State.WORK
            return Message(index=index, type=MessageType.RECEIVED)

