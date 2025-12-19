# BASIC CALCULATOR (+, -, x, /) for two numbers
#operators (+, -, x, /)
def operators(number1, number2, button):
    if button == "+":
        return number1 + number2
    elif button == "-":
        return number1 - number2
    elif button == "*":
        return number1 * number2
    elif button == "/":
        return number1 / number2
    else:
        return "Error! input operator +, -, *, /"



number1 = int(input("Input number:"))
button = input("Input button:")
number2 = int(input("Input number:"))

print("result:", operators(number1, number2, button))