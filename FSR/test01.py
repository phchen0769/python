import numpy as np
from sympy import symbols, simplify, expand

# Given data
x_values = [
    [0.00, 1.20, 2.80, 4.75, 6.35, 8.20, 10.44],
    [3.08, 6.05, 7.35, 8.55, 10.35, 12.45, 9.55],
    [-0.25, 1.25, 2.00, 4.75, 6.55, 8.30, 9.48],
    [3.25, 2.34, 1.30, 4.15, 5.16, 6.18, 8.15],
    [4.15, 3.22, 4.80, 5.16, 2.18, 7.19, 5.24],
    [0.00, -1.20, -2.80, -4.75, -6.35, -8.20, -10.44],
    [3.48, 6.55, 7.05, 8.25, 10.05, 12.25, 9.50],
    [-0.25, 1.45, 2.50, 4.35, 6.45, 8.70, 9.18],
    [-3.25, 2.54, 1.35, 4.45, 5.55, 6.36, 8.45],
    [4.25, 3.27, 4.83, 5.10, 2.15, 7.99, 5.21],
]

y_values = [
    [2.00, 3.30, -1.40, 0.20, 3.30, 5.75, 3.40],
    [0.15, 2.15, 4.55, 5.43, 3.65, 5.45, 7.34],
    [3.82, 2.94, 1.25, 5.85, 6.35, 4.25, 7.30],
    [2.18, 2.25, 3.35, 6.40, 7.50, 8.60, 3.75],
    [2.85, 3.96, 4.00, 5.10, 3.25, 2.35, 1.40],
    [2.50, -3.60, -1.70, 0.80, -3.95, 5.05, 3.15],
    [-0.25, 2.30, 4.45, 5.53, 3.65, 5.57, 7.28],
    [-3.99, 2.90, 1.91, 5.82, 6.43, 4.14, 7.43],
    [-2.58, 2.65, 3.75, 6.83, 7.29, 8.10, 3.11],
    [-2.25, 3.23, 4.45, 5.85, 3.65, 2.75, 1.28],
]


# Lagrange interpolation
def lagrange_interpolation(x_values, y_values, x):
    result = 0
    n = len(x_values)

    for i in range(0, n):
        term = y_values[i][0]
        for j in range(0, len(y_values[i])):
            if j != i:
                term *= (x - x_values[i][j]) / (x_values[i][i] - x_values[i][j])
        result += term

    return simplify(result)


# Newton interpolation
def newton_interpolation(x_values, y_values, x):
    n = len(x_values)
    coefficients = np.zeros(n)

    for i in range(n):
        coefficients[i] = y_values[i][0]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coefficients[i] = (coefficients[i] - coefficients[i - 1]) / (
                x_values[i][i] - x_values[i - j][i - j]
            )

    result = coefficients[n - 1]
    for i in range(n - 2, -1, -1):
        result = result * (x - x_values[i][i]) + coefficients[i]

    return expand(result)


# Calculate and compare values at x3
x3 = 3.0

lagrange_result = lagrange_interpolation(x_values, y_values, x3)
newton_result = newton_interpolation(x_values, y_values, x3)

print("Lagrange interpolation at x3:", lagrange_result.evalf())
print("Newton interpolation at x3:", newton_result.evalf())
