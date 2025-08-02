#calculator script
#This script is a basic calculator that performs addition, subtraction, multiplication, and division.
# It prompts the user for two numbers and an operation, then displays the result.

  
#function to get user numbers and operation
def basic_calculator():
    try:
        #Get user input
        num1 = float(input("Enter your first number: "))
        num2 = float(input("enter your second number: "))
        operation = input("Enter your desired operation: (+, -, *, /): ")
        #Perform the selected operation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 + num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("error: Division by zero is not allowed.")
                return
        else:
            print("Invalid operation please enter a valid operation: (+, -, *, /) ")
            return
        #Display the result
        print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

#Run the calculator
basic_calculator() 
