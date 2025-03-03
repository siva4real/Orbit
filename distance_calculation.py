import matplotlib.pyplot as plt
import numpy as np

# Marginal PMF of X
x_values = [-3, -2, -1, 0, 1, 2, 3]
x_probabilities = [1/15, 2/15, 1/5, 1/5, 1/5, 2/15, 1/15]

# Marginal PMF of Y
y_values = [-1, 0, 1]
y_probabilities = [1/3, 1/3, 1/3]

# Create figure with two subplots side by side
plt.figure(figsize=(12, 5))

# Plot for X
plt.subplot(1, 2, 1)
plt.bar(x_values, x_probabilities, color='skyblue', edgecolor='black')
plt.title('Marginal PMF of X')
plt.xlabel('X')
plt.ylabel('Probability P(X = x)')
plt.ylim(0, 0.25)  # Set y-limit to accommodate the highest probability (0.2)
plt.grid(True, alpha=0.3)

# Plot for Y
plt.subplot(1, 2, 2)
plt.bar(y_values, y_probabilities, color='lightgreen', edgecolor='black')
plt.title('Marginal PMF of Y')
plt.xlabel('Y')
plt.ylabel('Probability P(Y = y)')
plt.ylim(0, 0.5)  # Set y-limit to accommodate the probability (1/3 ≈ 0.3333)
plt.grid(True, alpha=0.3)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()