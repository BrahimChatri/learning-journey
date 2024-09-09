class Employee:
    def __init__(self, emp_id, name, position, salary, hire_date) -> None:
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.hire_date = hire_date

    def update_salary(self, new_salary):
        if new_salary > self.salary:
            self.salary = new_salary
            print(f"Salary updated for {self.name}. New salary: {self.salary}")
        else:
            print("Error: New salary must be higher than the current salary.")

    def promote(self, new_position, salary_increase):
        self.position = new_position
        self.salary += salary_increase
        print(f"{self.name} has been promoted to {self.position} with a new salary of {self.salary}")

    def employee_details(self) -> None:
        print(f"Employee Details:\n"
              f"ID: {self.emp_id}\n"
              f"Name: {self.name}\n"
              f"Position: {self.position}\n"
              f"Salary: ${self.salary:,.2f}\n"
              f"Hire Date: {self.hire_date}")


class EmployeeManagement:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, position, salary, hire_date):
        if emp_id in self.employees:
            print(f"Employee ID {emp_id} already exists.")
        else:
            new_employee = Employee(emp_id, name, position, salary, hire_date)
            self.employees[emp_id] = new_employee
            print(f"Employee {name} added successfully.")

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            print(f"Employee ID {emp_id} removed successfully.")
        else:
            print(f"Employee ID {emp_id} not found.")

    def update_salary(self, emp_id, new_salary):
        if emp_id in self.employees:
            self.employees[emp_id].update_salary(new_salary)
        else:
            print(f"Employee ID {emp_id} not found.")

    def promote_employee(self, emp_id, new_position, salary_increase):
        if emp_id in self.employees:
            self.employees[emp_id].promote(new_position, salary_increase)
        else:
            print(f"Employee ID {emp_id} not found.")

    def show_employee_details(self, emp_id):
        if emp_id in self.employees:
            self.employees[emp_id].employee_details()
        else:
            print(f"Employee ID {emp_id} not found.")


def main():
    management = EmployeeManagement()
    
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Salary")
        print("4. Promote Employee")
        print("5. Show Employee Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            salary = float(input("Enter employee salary: "))
            hire_date = input("Enter hire date (YYYY-MM-DD): ")
            management.add_employee(emp_id, name, position, salary, hire_date)
        
        elif choice == '2':
            emp_id = input("Enter employee ID to remove: ")
            management.remove_employee(emp_id)
        
        elif choice == '3':
            emp_id = input("Enter employee ID to update salary: ")
            new_salary = float(input("Enter new salary: "))
            management.update_salary(emp_id, new_salary)
        
        elif choice == '4':
            emp_id = input("Enter employee ID to promote: ")
            new_position = input("Enter new position: ")
            salary_increase = float(input("Enter salary increase: "))
            management.promote_employee(emp_id, new_position, salary_increase)
        
        elif choice == '5':
            emp_id = input("Enter employee ID to show details: ")
            management.show_employee_details(emp_id)
        
        elif choice == '6':
            print("Exiting the Employee Management System.")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
