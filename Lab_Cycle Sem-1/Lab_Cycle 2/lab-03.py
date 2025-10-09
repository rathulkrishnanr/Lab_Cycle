import numpy as np

A=np.array([[1,1],[1.50,4]])

B=np.array([2200,5050])

c=np.linalg.solve(A,B)

child,adult=c

print(f"child:{child}")
print(f"child:{adult}")