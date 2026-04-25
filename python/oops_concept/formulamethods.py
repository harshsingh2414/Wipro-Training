from abc import ABC, abstractmethod


class FM(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimetre(self):
        pass