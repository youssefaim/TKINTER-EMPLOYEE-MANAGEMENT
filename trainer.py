from employee import Employee  # Assuming the correct filename is "employee.py"
from ir import IR

class Trainer(Employee, IR):
    """
    Class representing a Trainer, inheriting from Employee and IR.
    """

    def __init__(self, nom="AIT MELLOUK", dateNaissance="09/09/2002", dateEmbauche="09/09/2023", salaireBase=9000):
        """
        Constructor for the Trainer class.
        Initializes the Trainer with specified parameters and sets default values for overtime hours and hourly rate.
        """
        super().__init__(nom, dateNaissance, dateEmbauche, salaireBase)
        self.__heureSup = 0
        self.__tarifHsup = 70
    
    @property
    def getheureSup(self):
        """
        Getter method for the number of overtime hours.
        """
        return self.__heureSup
    
    @property
    def gettarifHsup(self):
        """
        Getter method for the overtime hourly rate.
        """
        return self.__tarifHsup
    
    def setheureSup(self, hs1):
        """
        Setter method for the number of overtime hours.
        """
        self.__heureSup = hs1
    
    def settarifHsup(self, ths1):
        """
        Setter method for the overtime hourly rate.
        """
        self.__tarifHsup = ths1
    
    def __str__(self):
        """
        String representation of the Trainer.
        Combines the string representation of the base Employee class with additional Trainer-specific information.
        """
        return super().__str__() + f"Number of overtime hours per month: {self.getheureSup} - Remuneration per overtime hour: {self.gettarifHsup}"

    def getIR(self, salaire):
        """
        Method to calculate the income tax rate based on the salary.
        """
        for i in range(0, len(IR._tranches), 2):
            if IR._tranches[i] <= salaire <= IR._tranches[i + 1]:
                y = int(i / 2)
                return IR._tauxIR[y]
        return IR._tauxIR[len(IR._tauxIR) - 1]

    def salaireAPayer(self):
        """
        Method to calculate the total salary to be paid, including overtime and considering income tax.
        """
        return (self.getsalaireBase + self.getheureSup * self.gettarifHsup) * (1 - self.getIR(self.getsalaireBase))
