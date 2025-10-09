class Person:
    def __init__(self, Name, Age):
        self.name = Name
        self.age = Age
    
    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")

def main():
    People=[]
    n=int(input("Enter the number of inputs:"))

    for i in range(1,n+1):
       Name=input(f"Enter the name of {i} person:")
       Age=int(input(f"Enter the age of {i} person:"))
       People.append(Person(Name, Age))
    
    print("\nDisplaying Information:")
    for People in People:
        People.display()

main()

