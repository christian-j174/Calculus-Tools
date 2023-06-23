import numpy as np

def calculate_partial_sum(numbers):
    partial_sum = 0
    
    for num in numbers:
        partial_sum += num
    
    return partial_sum


def f(x):
    # Define the function for which you want to calculate the integral
    return x**2

def trapezoidal_rule(a, b, n):
    # Calculate the width of each subinterval
    h = (b - a) / n
    
    # Generate the x-values for the subintervals
    x = np.linspace(a, b, n+1)
    
    # Evaluate the function at the x-values
    y = f(x)
    
    # Apply the trapezoidal rule formula
    integral = h * (np.sum(y) - 0.5 * (y[0] + y[-1]))
    
    return integral

# Define the bounds of integration and the number of subintervals
a = 0  # Lower bound
b = 1  # Upper bound
n = 100  # Number of subintervals

# Calculate the integral using the trapezoidal rule
integral_value = trapezoidal_rule(a, b, n)

print("The integral of f(x) from", a, "to", b, "is:", integral_value)


