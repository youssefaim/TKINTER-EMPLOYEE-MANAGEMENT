from abc import ABCMeta, abstractmethod

class IR(metaclass=ABCMeta):
    """
    Abstract Base Class (ABC) representing Income Tax (IR).
    This class defines income tax brackets and rates, as well as an abstract method to calculate income tax.

    Attributes:
    _tranches: List of income tax brackets. Each pair of elements represents the lower and upper limits of a bracket.
    _tauxIR: List of corresponding income tax rates for each bracket.

    Methods:
    getIR: Abstract method to calculate income tax based on the provided salary.
    """

    _tranches = [0, 30000, 30001, 50000, 50001, 60000, 60001, 80000, 80001, 180000]
    _tauxIR = [0, 10, 20, 30, 34, 38]

    @classmethod
    @abstractmethod
    def getIR(cls, salaire):
        """
        Abstract method to calculate income tax based on the provided salary.

        Args:
        salaire: The salary for which income tax needs to be calculated.

        Returns:
        The calculated income tax.
        """
        pass
