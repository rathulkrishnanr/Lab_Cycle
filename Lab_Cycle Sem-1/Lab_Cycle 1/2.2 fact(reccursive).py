#Factorial (recursive fn)
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter a number:"))
print("The factorial of the number",n,"is",fact(n))