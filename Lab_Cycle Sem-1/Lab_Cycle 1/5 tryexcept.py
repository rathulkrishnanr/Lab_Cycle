try:
    num1=float(input("Enter numerator:"))
    num2=float(input("Enter denominator:"))
    result = num1/num2
    print(f"Result is {result}")
except ZeroDivisionError:
    print("Division by zero is no possible! Check the input values!")
