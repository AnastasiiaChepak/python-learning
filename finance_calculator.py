#1
#print("Hello, world!")


#2
#print ("Hello, my name is Anastasiia")
#print ("I am learning Python.") 
#print ("I want to work in IT")


#3
#print ("My name is Anastasiia")
#print ("I am 25 years old")
#print ("I live in Ireland")
#print ("I am learning Python")
#print ("My goal is to get a remote IT job")


#4
#name = "Anastasiia"
#age = 26
#country = "Ireland"
#goal = "get a remote IT job"

#print ("My name is", name)
#print ("I am",age, "years old")
#print ("I live in", country)
#print ("I am learning Python")
#print("My goal is to", goal)


#5
#name = "Anastasiia"
#age = 26
#country = "Ireland"
#oal = "get a remote IT job"
#height = 1.65
#is_learning_python = True
#has_it_experience = False

#print ("My name is", name)
#print ("I am", age , "years old")
#print ("I live in", country)
#print ("I am learning Python")
#print ("My goal is to", goal)
#print (type(height))
#print (type(is_learning_python))
#print (type(has_it_experience))


#6
#monthly_salary = 2500
#months = 12
#monthly_expenses = 800
#remaining = (monthly_salary - monthly_expenses) * months * 2

#print ("Years salary: ", monthly_salary * months)
#print ("Slary for 2 years: ", monthly_salary * months * 2)
#print ("Remainder: ", remaining)


#7
#monthly_salary = int(input("Enter your monthly salary: "))
#months = 12
#monthly_expenses = int(input("Enter your monthly expenses: "))
#remaining = (monthly_salary - monthly_expenses) * months * 2

#print ("Years salary: ", monthly_salary * months)
#print ("Salary for 2 years: ", monthly_salary * months * 2)
#print ("Remainder: ", remaining)


#8
#monthly_salary = int(input("Enter your monthly salary: "))
#months = 12
#monthly_expenses = int(input("Enter your monthly expenses: "))
#remaining = (monthly_salary - monthly_expenses) * months * 2

#print ("Years salary: ", monthly_salary * months)
#print ("Salary for 2 years: ", monthly_salary * months * 2)
#print ("Remainder: ", remaining)

#if monthly_expenses < monthly_salary:
#    print ("You can save money!")
#else:
#    print ("Warning: your expenses are too high!")


#9
#monthly_salary = int(input("Enter your monthly salary: "))
#months = 12
#monthly_expenses = int(input("Enter your monthly expenses: "))
#remaining = (monthly_salary - monthly_expenses) * months * 2
#monthly_remaining = monthly_salary - monthly_expenses

#print ("Years salary: ", monthly_salary * months)
#print ("Salary for 2 years: ", monthly_salary * months * 2)
#print ("Remainder: ", remaining)

#if monthly_remaining >= 2000:
#    print ("Great! You can save a lot of money.")

#elif monthly_remaining >= 500 and monthly_remaining < 2000:
#    print ("Good! You can save some money.")

#elif monthly_remaining < 500 and monthly_remaining >= 0:
#    print ("You should watch your expenses.")

#elif monthly_remaining < 0:
#    print ("Warning! You are spending more than you earn.")   

#else:
#    print ("You don't have money")


#10
#for number in range (1,11):
#    print (number)


#11
#for number in range (1,11):
#   print (number*number)


#12
#monthly_salary = int(input("Enter your monthly salary: ")) 
#monthly_expenses = int(input("Enter your monthly expenses: ")) 
#monthly_remaining = monthly_salary - monthly_expenses 
 
#for month in range (1,13): 
#        saved = monthly_remaining * month 
#        print ("Month ", month,":", saved)

#13
#if monthly_remaining > 0:

#   for month in range (1,13):
#        saved = monthly_remaining * month
#        print ("Month ", month,":", saved)

#else:
#    print ("You can't save money. Your expenses are too high.")


#14
#monthly_salary = int(input("Enter your monthly salary: "))  
#monthly_expenses = int(input("Enter your monthly expenses: ")) 
#monthly_remaining = monthly_salary - monthly_expenses 
 
#if monthly_remaining > 0: 
#    print ("You can save money.")
#  
#elif monthly_remaining == 0: 
#   print ("Your income and expenses are equal.")
#  
#else: 
#    print ("You are spending more than you earn.")


#15
#def calculate_yearly_salary (salary):
#   return salary * 12

#yearly_salary = calculate_yearly_salary(2500)
#print(yearly_salary)


#16
#def calculate_remaining (salary, expenses):
#    return salary - expenses

#remaining = calculate_remaining(2500, 800)
#print(remaining)   


#17
#monthly_salary = int(input("Enter your monthly salary: ")) 
#monthly_expenses = int(input("Enter your monthly expenses: ")) 

#def calculate_remaining (salary, expenses): 
#    return salary - expenses 
 
#remaining = calculate_remaining(monthly_salary, monthly_expenses) 
#print("You have", remaining, "left per month.")    
 
#if remaining > 0: 
#    print ("You can save money.") 

#elif remaining == 0: 
#    print ("Your income and expenses are equal.") 

#else: 
#    print ("You are spending more than you earn.")


#18
#def calculate_remaining(salary, expenses):
#    return salary - expenses


#monthly_salary = int(input("Enter your monthly salary: "))

#if monthly_salary <= 0:
#    print("Salary must be greater than 0.")

#else:
#    monthly_expenses = int(input("Enter your monthly expenses: "))

#    remaining = calculate_remaining(monthly_salary, monthly_expenses)

#    print("You have", remaining, "left per month.")

#    if remaining > 0:
#        print("You can save money.")

#    elif remaining == 0:
#        print("Your income and expenses are equal.")

#    else:
#        print("You are spending more than you earn.")


#19
#while True:
#    try:
#        age = int(input ("Enter number: "))
#        print ("You entered:", age)
#        break
#   except ValueError:
#        print("Please enter a valid number.")


#20
#while True:
#    try:
#        age = int(input ("Enter your age: "))

#        if age <= 0 or age > 120:
#            print ("Age must be between 1 and 120.")
#        else:
#            print ("You entered: ", age)
#            break
#    except ValueError:
#        print("Please enter a valid number.")


#21
#def get_positive_number():
#    while True:
#        try:
#            salary = int(input ("Enter your salary: "))

#            if salary <= 0:
#                print ("Salary must be a positive number")
#            else:
#                return salary
#        except ValueError:
#            print ("Please enter a valid number.")

#salary = get_positive_number()
#print("Your salary is:", salary)


#22
#def get_positive_number(prompt):
#    while True:
#        try:
#            number = int(input(prompt))
#
#            if number <= 0:
#                print("Number must be greater than 0.")
#            else:
#                return number

#        except ValueError:
#            print("Please enter a valid number.")

#salary = get_positive_number("Enter your salary: ")
#expenses = get_positive_number("Enter your expenses: ")

#print("Salary:", salary)
#print("Expenses:", expenses)


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


