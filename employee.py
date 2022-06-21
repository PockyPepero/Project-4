class Employee:
    """Stores employee info: first name, last name, and salary.
    Also contains a method for giving an employee a raise, with a default of 5k."""
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = float(salary)
    
    def give_raise(self,raise_amt=float(5000)):
        self.salary = raise_amt + self.salary
        return f"{self.first_name} {self.last_name} now has a salary of: {self.salary}"



