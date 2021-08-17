"""
Very advanced Employee management system.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class Comission:
    """
    Class to represent Comissions
    """
    commission: float = 100
    contracts_landed: float = 0

    def calculate_comissions(self) -> float:
        return self.commission * self.contracts_landed


class Contract(ABC):
    """
    Class to represent Contracts
    """

    @abstractmethod
    def get_payment(self) -> float:
        """Compute payment for employee """


@dataclass
class HourlyContract(Contract):
    """
    Class to represent Contracts with hourly pay
    """

    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def get_payment(self) -> float:
        return self.employer_cost + self.hours_worked * self.pay_rate


@dataclass
class SalariedContract(Contract):
    """
    Class to represent Contracts with a fixed salary
    """
    percentage: float = 1
    monthly_salary: float = 0

    def get_payment(self) -> float:
        return self.monthly_salary * self.percentage


@dataclass
class FreelancerContract(Contract):
    """
    Class to represent Freelancer Contracts
    """
    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked


@dataclass
class Employee():
    """
    Class to represent Employees
    """
    name: str
    id: str
    contract: Contract
    # comission is optional
    comission: Optional[Comission] = None


def main() -> None:
    """Main function."""

    henry_contract = HourlyContract(
        pay_rate=15, hours_worked=80, employer_cost=300)
    henry_employee = Employee(
        name="Henry T.", id="000000", contract=henry_contract)

    print(henry_employee.contract.get_payment())


if __name__ == "__main__":
    main()
