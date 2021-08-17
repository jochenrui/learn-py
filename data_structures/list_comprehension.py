from enum import Enum, auto
from typing import Tuple


class Role(Enum):
    """Employee Roles"""
    DEV = auto()
    HR = auto()
    IT = auto()


employees = [
    {
        "name": "Jochen",
        "role": Role.DEV
    },
    {
        "name": "Tom",
        "role": Role.IT
    },
    {
        "name": "Martin",
        "role": Role.HR
    },
    {
        "name": "John",
        "role": Role.DEV
    },
    {
        "name": "Jenny",
        "role": Role.IT
    },
    {
        "name": "Jason",
        "role": Role.HR
    },
]

# List comprehension


def find_employees_by_role(role: Role) -> Tuple:
    return tuple([employee for employee in employees if employee["role"].lower() == role.lower()


results=find_employees_by_role(Role.DEV)
print(type(results))
