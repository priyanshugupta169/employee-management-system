
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        """
        The method add_employee appends a new employee to a list of employees.
        The add_employee method is used to add a new employee to a list of employees
        within a class instance. 
        
        Args:
            employee: employee object that you want to add to the list
        """
        self.employees.append(employee)

    def remove_employee(self, employee):
        """
        The method remove_employee removes a specified employee from a department's list of
        employees if the employee is present, otherwise it prints a message indicating that the employee
        is not in the department.
        
        Args:
            employee: employee object that you want to remove from the department's list of employees
        """
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print(f"{employee.name} is not in {self.name} department.")

    def list_employees(self):
        """
        The list_employees method prints the employees in a specific department.
        """
        print(f"Employees in {self.name} department:")
        for employee in self.employees:
            print(employee.display_details())