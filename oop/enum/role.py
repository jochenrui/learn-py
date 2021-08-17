from enum import Enum, auto


class Role(Enum):
    """Enum for Employee Roles"""

    CEO = auto()
    LEAD = auto()
    SENIRODEV = auto()
    DEV = auto()
    JUNIORDEV = auto()
    HR = auto()
    # ...
