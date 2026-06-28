
from dataclasses import dataclass


@dataclass
class Player:

    name: str = "Shashank"

    money: int = 5000

    land: float = 0.50

    popularity: int = 5

    trust: int = 10

    supporters: int = 20

    year: int = 2002

    stage: str = "Student Union Election"

    turn: int = 1
