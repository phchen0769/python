import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Given data
x_data = np.array(
    [
        1.2,
        2.3,
        3.5,
        4.1,
        5.0,
        6.2,
        7.1,
        8.4,
        9.0,
        10.1,
        11.2,
        12.3,
        13.4,
        14.5,
        15.6,
        16.7,
        17.8,
        18.9,
        20.0,
        21.1,
    ]
)
y_data = np.array(
    [
        41.2,
        33.2,
        28.7,
        24.6,
        20.9,
        18.3,
        15.9,
        13.6,
        11.4,
        9.4,
        7.5,
        6.0,
        4.7,
        3.5,
        2.6,
        1.8,
        1.2,
        0.8,
        0.5,
        0.3,
    ]
)


# Define the model function (exponential decay)
def model_function(x, a, b):
    return a * np.exp(-b * x)


# Fit the model to the data using curve_fit
params, covariance = curve_fit(model_function, x_data, y_data)

# Extract the fitted parameters
a_fit, b_fit = params

# Generate y values using the fitted parameters
y_fit = model_function(x_data, a_fit, b_fit)

# Plot the original data and the fitted curve
plt.scatter(x_data, y_data, label="Original Data")
plt.plot(x_data, y_fit, label="Fitted Curve", color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# Print the fitted parameters
print("Fitted parameters:")
print("a =", a_fit)
print("b =", b_fit)
