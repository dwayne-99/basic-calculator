def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

# ^ Creates the functions for each operation 

operations = {
    "+" : add, 
    "-" : subtract, 
    "*" : multiply,
    "/" : divide, 
}

# ^ Stores each operation in a dictionary, with they key being the symbol and the value being the function

def calculator():
  
  num1 = float(input("What's the first number?: "))
# ^ Asks user for the first number
  
  for key in operations:
    print(key)

# ^ Prints the operations the user can choose from

  should_continue = True
# ^ Creates a variable aka a flag to control the loop
  
  while should_continue:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))

# ^ Asks user for the operation symbol and the second number

    calculation_function = operations[operation_symbol]
# ^ Gets the operation function from the dictionary

    answer = calculation_function(num1, num2)
# ^ Performs the operation an stores the answer
      
    print(f"{num1} {operation_symbol} {num2} = {answer}")
# ^ Prints the answer
      
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' start a new calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

# ^ Prompts the user if they want to continue their caluclations using the result of the previous calculation
# ^ If the user types 'y' it will continue the loop using the result of the previous calculation as the new 'num1' in the calculation function
# ^ If the user types 'n' it will start a new calculation by exiting the loop (line 55), and starting the program again (line 56)

calculator() 
# ^ Starts the calculator