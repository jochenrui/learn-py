from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self) -> None:
        self.description = "Unknown Beverage"

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass
