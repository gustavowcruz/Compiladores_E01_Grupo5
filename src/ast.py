from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Program:
    name: str
    commands: List['Command']


class Command:
    pass


@dataclass
class Move(Command):
    axis: str
    distance: float
    unit: str


@dataclass
class Turn(Command):
    degrees: float


@dataclass
class Speed(Command):
    value: float


@dataclass
class Wait(Command):
    duration: float
    ms: bool = False


@dataclass
class Repeat(Command):
    count: int
    commands: List[Command]


@dataclass
class Distance:
    value: float
    unit: str


@dataclass
class Angle:
    value: float
