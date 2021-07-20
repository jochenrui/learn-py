from abc import ABC, abstractmethod


class Pizza(ABC):
    def __init__(self):
        self.description = "Unknown Pizza"

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass
