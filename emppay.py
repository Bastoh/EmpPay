EMPLOYEES = []


def add_employees():
    """This function adds employees to the employee list"""
    new_employee = {}

    while True:
        try:
            name = input("\nEnter employee's name: ")
            if not name.replace(" ", "").isalpha():
                print("Name can only contain letters.")
            else:
                new_employee["emp_name"] = name
                break
        except TypeError:
            print("This field can only contain letters.")


    while True:
        try:
            id = input("\nEnter employee's ID: ")
            if len(id) > 3:
                print("ID can't be greater than 3 characters.")
            elif not id.isdigit():  #
                print("ID can only be numbers.")
            elif any(emp["emp_id"] == int(id) for emp in EMPLOYEES):
                print("Employee ID already exists.")
            else:
                new_employee["emp_id"] = int(id)
                break
        except ValueError:
            print("This field can only contain numbers.")


    while True:
        try:
            dept = input("\nEnter employee's department: ")
            if not dept.replace(" ", "").isalpha():
                print("This field can only contain letters.")
            else:
                new_employee["emp_dept"] = dept
                break
        except TypeError:
            print("This field can only contain letters.")


    while True:
        try:
            base_salary = float(input("\nEnter employee's base salary: "))
            if base_salary < 0:
                print("Base salary must be positive.")
            else:
                new_employee["emp_base"] = base_salary
                break
        except ValueError:
            print("This field can only contain floating point numbers.")


    while True:
        try:
            bonus = int(input("\nEnter employee's bonus: "))
            if bonus < 0:
                print("Bonus must be positive.")
            else:
                new_employee["emp_bonus"] = bonus
                break
        except ValueError:
            print("This field can only contain numbers.")

    EMPLOYEES.append(new_employee)
    print(f"Employee {new_employee['emp_name']} added successfully!")


def apply_bonus():
    """This function applies bonus based on the input"""
    try:
        emp_id = int(input("Enter employee's ID: "))
    except ValueError:
        print("Please enter a valid ID number.")
        return

    if len(EMPLOYEES) == 0:
        print("No employees found.")
        return

    found = False
    for i in EMPLOYEES:
        if i["emp_id"] == emp_id:
            i["emp_base"] += i["emp_base"] * (i["emp_bonus"] / 100)
            print(f"Successfully applied bonus to ID {emp_id}")
            found = True
            break

    if not found:
        print("Error, ID not found")


def calculate_net_salary(b_slry):
    """This function takes the base salary as input and returns the net salary"""
    if b_slry > 30000.0:
        tax_rate = 0.1
    else:
        tax_rate = 0.05
    return b_slry * (1 - tax_rate)


def generate_single_payslip():
    try:
        emp_id = int(input("Enter employee's ID: "))
    except ValueError:
        print("Please enter a valid ID number.")
        return

    if len(EMPLOYEES) == 0:
        print("No employees found.")
        return

    found = False
    for i in EMPLOYEES:
        if i["emp_id"] == emp_id:
            if i["emp_base"] > 30000.0:
                tax_amount = i["emp_base"] * 0.1
            else:
                tax_amount = i["emp_base"] * 0.05

            print("\n=== Payslip ===")
            print(f"Name: {i['emp_name']}")
            print(f"Department: {i['emp_dept']}")
            print(f"Base Salary: {i['emp_base']}")
            print(f"Tax Deducted: {tax_amount}")
            print(f"Net Salary: {calculate_net_salary(i['emp_base'])}")
            print("================")
            found = True
            break

    if not found:
        print("Employee ID not found.")


def generate_payslips():
    if len(EMPLOYEES) == 0:
        print("No employees found.")
        return

    for i in EMPLOYEES:
        if i["emp_base"] > 30000.0:
            tax_amount = i["emp_base"] * 0.1
        else:
            tax_amount = i["emp_base"] * 0.05

        print("\n=== Payslip ===")
        print(f"Name: {i['emp_name']}")
        print(f"Department: {i['emp_dept']}")
        print(f"Base Salary: {i['emp_base']}")
        print(f"Tax Deducted: {tax_amount}")
        print(f"Net Salary: {calculate_net_salary(i['emp_base'])}")
        print("================")

def main():
    menu_options = {
        1: add_employees,
        2: apply_bonus,
        3: generate_single_payslip,
        4: generate_payslips,
        5: None
    }

    while True:
        print("""
        \nEmployee Payroll System
        1. Add Employee
        2. Apply Bonus
        3. Generate Single Payslip (by ID)
        4. Generate All Payslips
        5. Exit
        """)

        try:
            case = int(input("Your choice: "))
            if case in menu_options:
                if case == 5:
                    print("Thank you for using EmpPay. See you soon!")
                    break
                else:
                    menu_options[case]()
            else:
                print("Invalid option. Please choose between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")


main()
