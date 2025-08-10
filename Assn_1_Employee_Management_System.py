# Step 1: Sample Employee Data
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Ravi', 'age': 30, 'department': 'Finance', 'salary': 60000},
    103: {'name': 'Anita', 'age': 25, 'department': 'IT', 'salary': 55000}
}

# Step 2: Show Menu
def main_menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Step 3: Add Employee
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("This ID already exists. Try a different one.")
            return

        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }

        print("Employee added successfully!")

    except ValueError:
        print("Invalid input. Please enter numbers where needed.")


# Step 4: View All Employees
def view_employees():
    if not employees:
        print("No employees available.")
    else:
        print("\nList of Employees:")
        for emp_id in employees:
            emp = employees[emp_id]
            print(
                f"ID: {emp_id}, Name: {emp['name']}, Age: {emp['age']}, Department: {emp['department']}, Salary: {emp['salary']}")


# Step 5: Search Employee
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            emp = employees[emp_id]
            print(f"Employee found!")
            print(f"Name: {emp['name']}")
            print(f"Age: {emp['age']}")
            print(f"Department: {emp['department']}")
            print(f"Salary: {emp['salary']}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Please enter a valid Employee ID.")


# Run the program
main_menu()
