# Small reusable functions

def greet(name):
    return f"Hello, {name}! Welcome to Python practice."


def is_even(number):
    return number % 2 == 0


def calculate_factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


print(greet("Nikku"))
print("Is 14 even?", is_even(14))
print("Factorial of 5:", calculate_factorial(5))
