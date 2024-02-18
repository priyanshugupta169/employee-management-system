

class Employee:
    """
    The Employee class defines attributes and methods to represent and display details of an employee.
    """
    def __init__(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def display_details(self):
        """
        The display_details method prints out the details of an employee including their name, ID,
        title, and department.
        """
        print("Employee Details:")
        print(f"Name: {self.name}")
        print(f"ID: {self.emp_id}")
        print(f"Title: {self.title}")
        print(f"Department: {self.department}")

    def __str__(self):
        return f"Name: {self.name}, ID: {self.emp_id}"