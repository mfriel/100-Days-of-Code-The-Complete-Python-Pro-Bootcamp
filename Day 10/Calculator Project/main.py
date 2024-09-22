from art import logo
print(logo)
#todo create 4 different mathematical operations functions
def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1, n2):
    return n1 - n2

#todo add the functions to a dict as the values. "+", "-" etc will be the keys, add() will be the values
operations ={
    "+": add, #no brackets as storing the values, rather than triggering the function
    "-": subtract,
    "*": multiply,
    "/": divide,
}
#todo: get input from user
def calculator():
    should_accumulate = True
    first_number = float(input("what's  the first number? "))  # first number, needs to be outside loop so not to overwrite line 41

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation: " ) #pick the operator
        second_number = float(input("what's  the next number? ")) #second number
        #print(f"{first_number} + {second_number} = {operations[operator](first_number, second_number)}")
        result = operations[operator](first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {result}")

        more_calculations = input(f"type 'y' to continue calculating with {result} or 'n' to start a new calculation: ").lower()
        if more_calculations == "y":
            first_number = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()

#todo do the calculations
#todo output the result to the user

# while True:
#     if operator == "+":
#         addition_result = operations["+"](first_number, second_number)
#         final_result = addition_result
#         #addition_result = add(first_number, second_number) #= add(first_number, second_number)
#         print(f"{first_number} + {second_number} = {addition_result}")
#     elif operator == "-":
#         subtraction_result = operations["-"](first_number, second_number)
#         final_result = subtraction_result
#
#         #subtraction_result = subtract(first_number, second_number)
#         print(f"{first_number} - {second_number} = {subtraction_result}")
#     elif operator == "*":
#         multiplication_result = operations["*"](first_number, second_number)
#         final_result = multiplication_result
#         #multiplication_result = multiply(first_number, second_number)
#         print(f"{first_number} * {second_number} = {multiplication_result}")
#     elif operator == "/":
#         division_result = operations["/"](first_number, second_number)
#         final_result = division_result
#
#         # division_result = divide(first_number, second_number)
#         print(f"{first_number} / {second_number} = {division_result}")





