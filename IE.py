from abc import ABCMeta, abstractmethod

class IEmployee(metaclass=ABCMeta):
    """
    Abstract Base Class (ABC) for representing an employee.
    This class defines three abstract methods that any concrete class
    inheriting from it must implement: Age, Seniority, and RetirementDate.
    """

    @abstractmethod
    def Age(self):
        """
        Abstract method to calculate the age of the employee.
        """
        pass

    @abstractmethod
    def Seniority(self):
        """
        Abstract method to calculate the years of service of the employee.
        """
        pass

    @abstractmethod
    def RetirementDate(self, retirement_age):
        """
        Abstract method to calculate the retirement date of the employee.
        :param retirement_age: The age at which the employee will retire.
        """
        pass