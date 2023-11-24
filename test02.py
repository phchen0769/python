import numpy as np

# Given data
x = np.array(
    [
        [1.3, 2.1, 3.7, 4.2, 5.5, 6.9, 7.3],
        [1.7, 2.2, 3.5, 4.1, 5.0, 6.9, 7.4],
        [1.0, 2.4, 3.9, 4.4, 5.2, 6.7, 7.4],
        [0.5, 1.2, 2.7, 3.5, 4.0, 5.2, 6.7],
        [1.2, 2.5, 3.7, 4.8, 6.0, 7.2, 8.5],
        [1.0, 2.2, 3.5, 4.7, 6.0, 7.2, 8.5],
        [0.5, 1.2, 2.0, 2.7, 3.5, 4.2, 5.0],
        [1.1, 1.3, 2.5, 2.7, 3.8, 3.9, 4.5],
        [0.2, 1.4, 1.6, 2.8, 2.9, 3.4, 3.6],
        [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2],
    ]
)

y = np.array(
    [
        [10.2, 5.4, 2.7, -5.6, -9.1, -14.2, -19.8],
        [-4.2, -3.8, -2.5, -1.7, 0.5, 1.8, 4.3],
        [1.8, 3.3, 2.2, 4.0, 4.5, 5.1, 6.7],
        [-2.2, -1.1, 0.7, 1.5, 2.3, 2.8, 3.0],
        [-1.5, -0.8, 0.3, 1.6, 2.8, 4.1, 5.3],
        [-1.2, -0.5, 0.8, 1.5, 2.2, 3.1, 4.0],
        [-1.8, -1.0, 0.3, 0.9, 1.6, 2.1, 2.8],
        [0.8, 1.2, 1.9, 2.5, 3.1, 3.7, 4.2],
        [-0.5, 0.6, 1.5, 2.0, 2.7, 3.4, 4.0],
        [1.2, 1.3, 1.4, 1.6, 1.9, 2.3, 2.6],
    ]
)


# Linear regression function
def linear_regression(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    b = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
    a = y_mean - b * x_mean

    return a, b


# Calculate linear regression coefficients
a, b = linear_regression(x[0], y[0])

# Calculate the fit function values at x3
x3 = 3.0
fit_function_value = a + b * x3

print("Fit function value at x3:", fit_function_value)
