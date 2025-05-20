from enum import Enum, auto


class SpacecraftStatus(Enum):
    IDLE = auto()
    IN_TRANSIT = auto()
    DOCKED = auto()
    DESTROYED = auto()

