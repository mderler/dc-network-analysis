from raylibpy import Vector2
from dataclasses import dataclass

@dataclass
class Resistor:
    name: str
    resistance: float
    position: Vector2
    is_horizontal: bool = True
