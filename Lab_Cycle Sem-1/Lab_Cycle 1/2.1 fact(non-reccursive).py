# Factorial (non-recursive fn)
def fact(n):
    result = 1
    if n<=1:
        return 1
    else:
        for i in range(2, n+1):
            result=result*i
    return result

num=int(input("Enter a number:"))
print("The factorial of the number",num,"is",fact(num))