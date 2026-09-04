#23 Personal Finance Calculator
def get_positive_number(prompt):
    while True:
        try:
            number = int(input(prompt))

            if number <= 0:
                print("Number must be greater than 0.")
            else:
                return number

        except ValueError:
            print("Please enter a valid number.")

def calculate_remaining(salary, expenses):
    return salary - expenses

if __name__ == "__main__":
    salary = get_positive_number("Enter your monthly salary: ")
    expenses = get_positive_number("Enter your monthly expenses: ")

    remaining = calculate_remaining(salary, expenses)
    print("You have", remaining, "left per month.")

    if remaining > 0:
        print("You can save money.")

        for month in range(1, 13):
            saved = remaining * month
            print("Month ", month, ": ", saved)

    elif remaining == 0:
        print("Your income and expenses are equal.")

    else:
        print("You are spending more than you earn.")


