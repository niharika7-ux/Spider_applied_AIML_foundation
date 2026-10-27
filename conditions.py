# Use conditions to display a result based on marks

try:
    marks = float(input("Enter marks out of 100: "))

    if not 0 <= marks <= 100:
        print("Please enter a value between 0 and 100.")
    elif marks >= 90:
        print("Result: Excellent")
    elif marks >= 75:
        print("Result: Very good")
    elif marks >= 40:
        print("Result: Pass")
    else:
        print("Result: Needs improvement")
except ValueError:
    print("Invalid input. Enter marks using numbers.")
