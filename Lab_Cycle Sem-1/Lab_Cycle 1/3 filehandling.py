# Write a file
file=open("Demo.txt","w")
file.write("File has be created successfully\n")
file.close()

# Read a file
file=open("Demo.txt","r")
print(file.read())
file.close()

# Append a file
file=open("Demo.txt","a")
n=10
print("First 10 natural numbers created successfully")
for i in range (1,n+1):
    file.write(str(i)+"\n")
file.close()