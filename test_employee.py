import unittest
from employee import Employee

class TestEmployeeRaise(unittest.TestCase):
    """Testing the give_raise method for the Employee class."""
    
    def setUp(self):
        """Create an employee for use in all test methods."""
        self.my_employee = Employee('John','Smith',50000)

    def test_give_default_raise(self):
        self.assertEqual(self.my_employee.give_raise(),f"John Smith now has a salary of: {float(55000)}")

    def test_give_custom_raise(self):
        self.assertEqual(self.my_employee.give_raise(10000),f"John Smith now has a salary of: {float(60000)}")
        
if __name__ == '__main__':
    unittest.main()


