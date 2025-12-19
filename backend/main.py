# BASIC CALCULATOR (+, -, x, /) for two numbers
#addition (+)
def addition(number1, number2):
    return number1 + number2

#subtraction (-)
def subtraction(number1,number2):
    return number1 - number2

#multiplication (x)
def multiplication(number1, number2):
    return number1 * number2

#division (/)
def division(number1, number2):
    return number1 / number2


number1 = int(input("Input number:"))
number2 = int(input("Input number:"))

# print("result:", operators(number1, number2, button))

print(addition(number1, number2)) #addition