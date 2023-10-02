"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = False
        self.hourly = False
        self.monthly_salary = 0
        self.contract_hours = 0
        self.contract_pay = 0
        self.bContract_commission = False
        self.bContract_contracts = 0
        self.bContract_pay = 0
        self.bCommission = False
        self.bCommission_amt = 0
        match name:
            case 'Billie':
                self.salary = True
                self.monthly_salary = 4000
            case 'Charlie':
                self.hourly = True
                self.contract_hours = 100
                self.contract_pay = 25
            case 'Renee':
                self.salary = True
                self.monthly_salary = 3000
                self.bContract_commission = True
                self.bContract_contracts = 4
                self.bContract_pay = 200
            case 'Jan':
                self.hourly = True
                self.contract_hours = 150
                self.contract_pay = 25
                self.bContract_commission = True
                self.bContract_contracts = 3
                self.bContract_pay = 220
            case 'Robbie':
                self.salary = True
                self.monthly_salary = 2000
                self.bCommission = True
                self.bCommission_amt = 1500
            case 'Ariel':
                self.hourly = True
                self.contract_hours = 120
                self.contract_pay = 30
                self.bCommission = True
                self.bCommission_amt = 600
        

    def get_pay(self):
        self.total = 0
        if self.salary:
            self.total += self.monthly_salary
        if self.hourly:
            self.total += (self.contract_hours * self.contract_pay)
        if self.bContract_commission:
            self.total += (self.bContract_contracts * self.bContract_pay)
        if self.bCommission:
            self.total += self.bCommission_amt
        return self.total


    def __str__(self):
        self.get_pay()
        pay_str = f"{self.name} works on a "
        if self.salary:
            pay_str += f"monthly salary of {self.monthly_salary}"
        if self.hourly:
            pay_str += f"contract of {self.contract_hours} hours at {self.contract_pay}/hour"
        if self.bContract_commission:
            pay_str += f" and receives a commission for {self.bContract_contracts} contract(s) at {self.bContract_pay}/contract"
        if self.bCommission:
            pay_str += f" and receives a bonus commission of {self.bCommission_amt}"
        pay_str += f". Their total pay is {self.total}."
        return pay_str
        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')

print(renee)