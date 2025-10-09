# n=int(input("Enter a number: "))

# for i in range(n):
#     Age=int(input("Enter Your Age: "))
    
#     if Age>=18:
#         print("You are eligible for voting")
#     else:
#         print("You are not eligible for voting")

# for i in range(1,11):
#     print(i)

# i=1
# while(i<=10):
#     print(i)
#     i+=1

# import numpy as np

# # First Matrix
# rows = int(input("Enter Number of rows for Matrix A: "))
# cols = int(input("Enter Number of columns for Matrix A: "))

# matrix1 = []
# for i in range(rows):
#     row = list(map(int, input(f"Enter row {i+1} elements (separated by space): ").split()))
#     matrix1.append(row)

# print("\nMatrix 1:")
# for row in matrix1:
#     print(row)

# # Second Matrix
# row1 = int(input("\nEnter Number of rows for Matrix B: "))
# col1 = int(input("Enter Number of columns for Matrix B: "))

# matrix2 = []
# for i in range(row1):
#     row2 = list(map(int, input(f"Enter row {i+1} elements (separated by space): ").split()))
#     matrix2.append(row2)

# print("\nMatrix 2:")
# for row in matrix2:
#     print(row)

# # Convert to numpy arrays
# A = np.array(matrix1)
# B = np.array(matrix2)

# print("\nMatrix A:\n", A)
# print("Matrix B:\n", B)

# # Matrix Multiplication
# if A.shape[1] == B.shape[0]:
#     C = np.dot(A, B)
#     print("\nMatrix Multiplication (A * B):\n", C)
# else:
#     print("\nMatrix multiplication not possible (columns of A != rows of B).")

# # Transpose of A
# print("\nTranspose of A:\n", A.T)

# # Determinant and Inverse
# if A.shape[0] == A.shape[1]:
#     det_A = np.linalg.det(A)
#     print("\nDeterminant of A:", det_A)

#     if det_A != 0:
#         A_inv = np.linalg.inv(A)
#         print("\nInverse of A:\n", A_inv)
#     else:
#         print("\nMatrix A is singular and does not have an inverse.")
# else:
#     print("\nMatrix A is not square, determinant and inverse cannot be computed.")


# Write a file
file=open("Demo.txt","w")
file.write("File has be created successfully")
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

