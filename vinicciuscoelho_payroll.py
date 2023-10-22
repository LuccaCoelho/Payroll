# Viniccius Lucca Florindo Coelho
# CS-1410
# 10/21/2023

""" This program is expected to take data from user input for a payroll.
    It takes employee name, classisfication, hours worked and hourly pay
    rate (if hourly employee). The program display a payroll with each
    employee's payment, total payroll, number of salaried employees,
    amount of regular and overtime hours (for hourly employee), and 
    average hours between the employees.
"""


class Employee:
    """
        It represents an employee with a name, rate of pay, and hours worked.
    """

    def __init__(self, name, rate_of_pay, hours):
        """It is an Employee object

        Args:
            name (str): Name of the employee
            rate_of_pay (float): The rate of pay for the employee
            hours (float): Hours the employee worked
        """
        # employee's information
        self.name = name
        self.rate_of_pay = rate_of_pay
        self.hours = hours


class SalariedEmployee(Employee):
    """Represents a salaried employee. Subclass of Employee.
    """

    def calculatepay(self):
        """Returns salaried employee pay

        Returns:
            float: Total pay for a salaried employee
        """
        # Don't need to do more then calculate the total pay
        return self.rate_of_pay


class HourlyEmployee(Employee):
    """Represents a hourly employee. Subclass of Employee.
    """

    def calculatepay(self):
        """Calculate total pay considering regular (< 40) and overtime (> 40) of hourly employees.

        Returns:
            float: Total pay of hourly employee. Any hour over 40 will be paid * 1.5.
        """
        # It makes sure that the regularf hours don't go over 40.
        regular_hours = min(self.hours, 40)

        # If the hours are more then 40, then we calculate the overtime hour
        if self.hours > 40:
            overtime_hours = self.hours - 40
        else:
            overtime_hours = 0

        # return total pay for regular and overtime hours (if any) * hour and a half
        return (regular_hours * self.rate_of_pay) + (overtime_hours * self.rate_of_pay * 1.5)

    def calculate_overtime(self):
        """Calculates regular (< 40) and overtime (> 40) hours for hourly employee.

        Returns:
            tuple: Contains regular hours (float) and overtime hours (float).
        """
        # make sure regular hour is not over 40
        regular_hours = min(self.hours, 40)

        # Calculate any overtime (over 40hrs)
        if self.hours > 40:
            overtime_hours = self.hours - 40
        else:
            overtime_hours = 0

        # return total of regular and overtime hours
        return regular_hours, overtime_hours


def employee_data():
    """Take user input for employee's name, classification and hours worked, and return the data.

    Returns:
        tuple: Contains employee name (str), classification (str) and hours worked (float) 
    """
    # User inputs for all employee's data needed
    name = input("\nEnter employee's name: ")
    classification = input(
        "Enter employee's classification (Salaried or Hourly): ")
    hours = float(input("Enter the number of hours worked: "))

    # Return user inputs
    return name, classification, hours


def create_employee(classification, name, rate_of_pay, hours):
    """Create and returns an Employee object based on classification.

    Args:
        classification (str): The employee's classification
        name (str): Employee's name
        rate_of_pay (float): Employee's pay rate
        hours (string): Number of hours worked

    Returns:
        subclass: Employee subclass
    """

    # Check Employee's classification to calculate the right pay
    if classification.lower() == "salaried":
        return SalariedEmployee(name, rate_of_pay, hours)

    # Hourly employee needs an hourly wage calculation
    elif classification.lower() == "hourly":
        hourly_wage = float(input("Enter hourly wage: "))
        return HourlyEmployee(name, hourly_wage, hours)


def calculate_total_payroll(employee_list):
    """Calculate the total payroll from a list of employees.

    Args:
        employee_list (list): A list of Employee objects
    Returns:
        float: Total payroll of employees
    """
    # total payroll will start at 0 so we can add to that
    total_payroll = 0

    # employee is our index for employee list and it will
    # go thorugh every employee added to the list
    for employee in employee_list:
        # will add the calculated payment for each employee to the total payroll
        total_payroll += employee.calculatepay()

    return total_payroll


def payroll_summary(employee_list, total_payroll, salaried_count):
    """Display all the data collected for employees in a payroll format.

    Args:
        employee_list (list): A list of Employee objects
        total_payroll (float): Total payroll for all employees
        salaried_count (int): Number of salaried employees
    """

    print("\nPayroll information:")

    # Employee is our index and will go throught all employees in employee list.
    for employee in employee_list:
        # isintance check if the respective employee in part of the HourlyEmployee class.
        if isinstance(employee, HourlyEmployee):
            # if employee is part of the class it runs the hourly display.
            # call regular and overtime hours and make them equal to the class
            regular_hours, overtime_hours = employee.calculate_overtime()

            # Print employee's name, total pay, amount of regular and overtime hours.
            print(f"{employee.name.title().strip()}: ${employee.calculatepay():.2f}" +
                   f"(Regular Hours: {regular_hours:.1f}, Overtime Hours: {overtime_hours:.1f}).")
        else:
            # If employee is not part of HourlyEmployee class it will display salaried employee data
            print(f"{employee.name}: ${employee.calculatepay():.1f}.")

    # Print the total number of employees
    print(f"Number of employees: {len(employee_list)}.")

    # Print Total number of salaried employees
    print(f"Number of salaried employees: {salaried_count}.")

    # Print total amount of payroll
    print(f"Total payroll: ${total_payroll:.2f}.")

    # We set total hours to be the sum of every employee hours inside the employee list
    # calculate average and print it
    total_hours = sum(employee.hours for employee in employee_list)
    average_hours = total_hours / len(employee_list)
    print(
        f"Average number of hours worked per employee: {average_hours:.2f} Hours.")


def check_error(employee_list, salaried_count):
    """Validate user input and add it to the employee list.

    Args:
        employee_list (list): List of Employee objects
        salaried_count (int): Number of salaried employees

    Returns:
        int: Number of salaried employees
    """

    # While loop to make sure we get every employee until stopped by user
    while True:

        # Try for extra ValueError handling
        try:
            name, classification, hours = employee_data()

            # Will check for digits in the employee's name
            if any(character.isdigit() for character in name):
                print("\nError: Can't use numbers on name.")
                continue

            # Check if any data was not inserted
            elif name == "" or classification == "" or hours == "":
                print('\nError: Some of the variables were not computated.')
                continue

            # If employee is salaried will ask user for data we need and validade the input
            if classification.lower() == "salaried":
                while True:
                    try:

                        weekly_salary = float(input("Enter weekly salary: "))
                        break
                    except (ValueError, SyntaxError):
                        print(
                            "Error: Something Went Wrong. Make sure everything is typed correctly.")
                employee = create_employee(
                    classification, name, weekly_salary, hours)

                # Add amount of salaried employee to the count
                salaried_count += 1

            elif classification.lower() == "hourly":
                employee = create_employee(classification, name, 0, hours)
            else:
                print("\nError: Invalid classification. Please enter 'Salaried' or 'Hourly.'")
                continue

            # After validating input, it will add to the employee list
            employee_list.append(employee)

        except (ValueError, TypeError):
            print("\nError: Something Went Wrong. Make sure everything is typed correctly.")
            continue

        # This while loop will make sure the user insert either Y or N
        while True:

            # Ask user input, and make sure is either Y or N.
            continue_input = input(
                "Do you want to continue (Y/N)? ").strip().upper()
            if continue_input == "N":
                break
            elif continue_input == "Y":
                break
            else:
                print("Error: Invalid input.")
                continue

        # Break from the whole function if it's N
        if continue_input == "N":
            break

    return salaried_count


def main():
    """Main function of this payroll system
    """
    # Set our employee list (empty at first)
    employee_list = []

    # Start salaried employee count
    salaried_count = 0

    # Call functions
    salaried_count = check_error(employee_list, salaried_count)
    total_payroll = calculate_total_payroll(employee_list)
    payroll_summary(employee_list, total_payroll, salaried_count)


if __name__ == "__main__":
    main()