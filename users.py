"""User, Privileges, and Admin classes for a user database."""

class User:
    """Collects and prints data about users."""

    def __init__(self, first_name, last_name, username, join_date, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.join_date = join_date
        self.age = age
        self.isAdmin = False

    def describe_user(self):
        print(f"The user {self.username} joined on {self.join_date}. ")
        print(f"Their name is {self.first_name} {self.last_name}. ")
        print(f"They are {self.age} years old. \n")

    def greet_user(self):
        print(f"Hello {self.first_name}, how are you today?\n")

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"This user is an admin. They have the following admin privileges: {self.privileges}")

class Admin(User):
    def __init__(self, first_name, last_name, username, join_date, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.join_date = join_date
        self.age = age
        self.privileges = Privileges(['can add post','can delete post','can ban user'])