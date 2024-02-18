import json
from employee import Employee
from department import Department

FILE = "company_data.json"


def add_department(company, department):
    """
    The method add_department adds a department to a company dictionary if it does not already
    exist.
    The method checks if a department with the same name already exists in the company dictionary.
    
    Args:
        company: dictionary where the keys represent department names and the values are the serialized department objects
        department: An object representing a department within a company.
    """
    if department.name not in company:
        company[department.name] = department
    else:
        print(f"{department.name} department already exists.")

def remove_department(company, department_name):
    """
    The method `remove_department` removes a specified department from a company dictionary if it
    exists.
    
    Args:
        company: dictionary representing the company's departments.
        department_name: name of the department that you want to remove
    """
    if department_name in company:
        del company[department_name]
    else:
        print(f"{department_name} department does not exist.")

def display_departments(company):
    """
    The method display_departments takes a company dictionary as input and prints out the list of
    department names.
    
    Args:
        company: dictionary representing the company's departments. 
    Returns:
        The method will then print out the list of departments.
    """
    print("List of Departments:")
    for department_name in company:
        print(department_name)

def display_menu():
    """
    This method prints out a menu for an Employee Management System.
    """
    print("\nEmployee Management System Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. List Employees in Department")
    print("4. Add Department")
    print("5. Remove Department")
    print("6. Display Departments")
    print("7. Exit")

def save_company_data(company):
    """
    The method save_company_data saves the company data to a JSON file.
    The method uses the json.dump() method to write the company data to the file
    
    Args:
        company: dictionary representing the company's departments. 
    """
    json_data = {}
    for (dep, obj) in company.items():
        data = {}
        data['name'] = obj.name
        data['employees'] = [emp.__dict__ for emp in obj.employees]
        json_data[dep] = data
    with open(FILE, "w") as file:
        json.dump(json_data, file)

def load_company_data():
    """
    The method load_company_data reads and returns JSON data from a file, or an empty dictionary if
    the file is not found.
    Returns:
        A dictionary is being returned if the file is found
    """
    try:
        with open(FILE, "r") as file:
            loaded_data = json.load(file)
            loaded_objects = {}
            for (dep_name, obj) in loaded_data.items():
                print(obj['name'])
                department = Department(obj['name'])
                department.employees = [
                    Employee(emp['name'], emp['emp_id'], emp['title'], emp['department'] ) 
                        for emp in obj['employees']
                    ]
                loaded_objects[dep_name] = department
            return loaded_objects
    except FileNotFoundError:
        return {}

def main():
    company = {}
    company = load_company_data()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Employee
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            department_name = input("Enter department name: ")

            if department_name in company:
                employee = Employee(name, emp_id, title, department_name)
                company[department_name].add_employee(employee)
                print("Employee added successfully.")
            else:
                print(f"{department_name} department does not exist.")

        elif choice == "2":
            # Remove Employee
            department_name = input("Enter department name: ")
            emp_id = input("Enter employee ID: ")

            if department_name in company:
                employees = company[department_name].employees
                found = False
                for employee in employees:
                    if employee.emp_id == emp_id:
                        company[department_name].remove_employee(employee)
                        print("Employee removed successfully.")
                        found = True
                        break
                if not found:
                    print(f"Employee with ID {emp_id} not found in {department_name} department.")
            else:
                print(f"{department_name} department does not exist.")

        elif choice == "3":
            # List Employees in Department
            department_name = input("Enter department name: ")

            if department_name in company:
                company[department_name].list_employees()
            else:
                print(f"{department_name} department does not exist.")

        elif choice == "4":
            # Add Department
            department_name = input("Enter department name: ")
            department = Department(department_name)
            print(company)
            add_department(company, department)
            print("Department added successfully.")

        elif choice == "5":
            # Remove Department
            department_name = input("Enter department name: ")
            remove_department(company, department_name)
            print("Department removed successfully.")

        elif choice == "6":
            # Display Departments
            display_departments(company)

        elif choice == "7":
            # Exit
            save_company_data(company)
            print("Exiting Employee Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
