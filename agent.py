# Importing the Employe and IR classes
from employee import Employee
from ir import IR

# Defining the Agent class, which inherits from Employe and IR
class Agent(Employee, IR):
    def __init__(self, nom="AIT MELLOUK", dateNaissance="09/09/2002", dateEmbauche="09/09/2023", salaireBase=9000, primeResponsabilite=0):
        # Calling the constructor of the parent classes (Employe and IR)
        super().__init__(nom, dateNaissance, dateEmbauche, salaireBase)
        # Adding a new attribute specific to the Agent class
        self.primeResponsabilite = primeResponsabilite

    def getIR(self, salaire):
        # Calculating the income tax rate based on salary
        for i in range(0, len(IR._tranches), 2):
            if IR._tranches[i] <= salaire <= IR._tranches[i + 1]:
                y = int(i / 2)
                return IR._tauxIR[y]
        # If salary exceeds the last defined bracket, use the highest tax rate
        return IR._tauxIR[len(IR._tauxIR) - 1]

    def salaireAPayer(self):
        # Calculating the net salary to be paid
        return (self.getsalaireBase + self.primeResponsabilite) * (1 - self.getIR(self.getsalaireBase))
