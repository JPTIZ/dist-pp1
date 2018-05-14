'''Contains distributed system abstractions.'''
from typing import NamedTuple
from datetime import datetime
from enum import Enum


class Token(int):
    pass


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
    token: Token
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
