class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename
    def add_employee(self, employee):
        if self.is_employee_id_unique(employee.employee_id):
            with open(self.filename, "a") as file:
                file.write(str(employee) + "\n")
            print("Employee added successfully!")
        else:
            print("Employee ID already exists. Please use a unique Employee ID.")
    def is_employee_id_unique(self, employee_id):
        try:
            with open(self.filename, "r") as file:
                employees = file.readlines()
                for emp in employees:
                    emp_data = emp.strip().split(", ")
                    if emp_data[0] == employee_id:
                        return False
        except FileNotFoundError:
            pass
        return True
    def sort_employees(self, employees, sort_by):
        if sort_by == "name":
            return sorted(employees, key=lambda emp: emp.split(", ")[1])
        elif sort_by == "salary":
            return sorted(employees, key=lambda emp: int(emp.split(", ")[3]))
        return employees
    def view_all_employees(self, sort_by=None):
        try:
            with open(self.filename, "r") as file:
                employees = file.readlines()
                if employees:
                    if sort_by:
                        employees = self.sort_employees(employees, sort_by)
                    print("Employee Records:")
                    for emp in employees:
                        print(emp.strip())
                else:
                    print("No employee records found.")
        except FileNotFoundError:
            print("No employee records found.")
    def search_employee(self, employee_id):
        try:
            with open(self.filename, "r") as file:
                employees = file.readlines()
                for emp in employees:
                    emp_data = emp.strip().split(", ")
                    if emp_data[0] == employee_id:
                        print("Employee Found:")
                        print(emp.strip())
                        return
                print("Employee not found.")
        except FileNotFoundError:
            print("No employee records found.")
    def update_employee(self, employee_id, name=None, position=None, salary=None):
        try:
            with open(self.filename, "r") as file:
                employees = file.readlines()
            with open(self.filename, "w") as file:
                for emp in employees:
                    emp_data = emp.strip().split(", ")
                    if emp_data[0] == employee_id:
                        if name:
                            emp_data[1] = name
                        if position:
                            emp_data[2] = position
                        if salary:
                            emp_data[3] = salary
                        emp = ", ".join(emp_data) + "\n"
                        print("Employee updated successfully!")
                    file.write(emp)
        except FileNotFoundError:
            print("No employee records found.")
    def delete_employee(self, employee_id):
        try:
            with open(self.filename, "r") as file:
                employees = file.readlines()
            with open(self.filename, "w") as file:
                for emp in employees:
                    emp_data = emp.strip().split(", ")
                    if emp_data[0] != employee_id:
                        file.write(emp)
                print("Employee deleted successfully!")
        except FileNotFoundError:
            print("No employee records found.")
    def menu(self):
        print("Welcome to the Employee Records Manager!")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        while True:
            print()
            choice = input("Enter your choice: ")
            if choice == "1":
                employee_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                try:
                    salary = int(salary)
                    employee = Employee(employee_id, name, position, salary)
                    self.add_employee(employee)
                except ValueError:
                    print("Invalid salary. Please enter a numeric value.")
            elif choice == "2":
                sort_by = input("Sort by (name or salary or leave blank): ").strip().lower()
                if sort_by not in ["name", "salary", "none", ""]:
                    print("Invalid sort option. Showing unsorted records.")
                    sort_by = None
                self.view_all_employees(sort_by if sort_by != "none" else None)
            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ")
                self.search_employee(employee_id)
            elif choice == "4":
                employee_id = input("Enter Employee ID to update: ")
                name = input("Enter new Name (leave blank to keep current): ")
                position = input("Enter new Position (leave blank to keep current): ")
                salary = input("Enter new Salary (leave blank to keep current): ")
                try:
                    salary = int(salary) if salary else None
                    self.update_employee(employee_id, name, position, salary)
                except ValueError:
                    print("Invalid salary. Please enter a numeric value.")
            elif choice == "5":
                employee_id = input("Enter Employee ID to delete: ")
                self.delete_employee(employee_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

manager = EmployeeManager()
manager.menu()