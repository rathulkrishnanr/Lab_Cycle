import matplotlib.pyplot as plt
import numpy as np

# Define x values
x = np.linspace(-10, 10, 400)

# Define y = x^2
y = x**2

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='y = x²', color='blue')
plt.title('Graph of y = x²')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
