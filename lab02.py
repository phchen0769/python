# Lab02 Development and Simulation of a Fuzzy Control
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Import required libraries

# Step 2: Define constants
s = 0.01  # Integration step
T = 50.0  # Simulation duration
num_rules = 36  # Number of rules in the database

# Step 3: Read initial conditions from Table 3.1
initial_conditions = {
    "phi": [
        10,
        15,
        25,
        30,
        -40,
        -30,
        -20,
        -10,
        0,
        60,
        50,
        40,
        30,
        -30,
        -40,
        -50,
        -60,
        25,
        35,
        45,
        65,
        -65,
        -50,
        -20,
        0,
    ],
    "omega": [
        0,
        1,
        2,
        3,
        -4,
        -5,
        -6,
        -7,
        6,
        5,
        4,
        3,
        2,
        1,
        0,
        -1,
        -2,
        -3,
        -4,
        -5,
        -6,
        -7,
        -6,
        -5,
        -4,
    ],
}


# Step 4: Implement the fuzzy logic control algorithm
def fuzzy_logic_control(phi, omega):
    # TODO: Implement the fuzzy logic control algorithm based on the provided rules
    pass


# Step 5: Integrate the system of differential equations using the Euler method
def euler_integration(t, phi, omega, alpha):
    phi_dot = omega
    omega_dot = alpha

    t_next = t + s
    phi_next = phi + s * phi_dot
    omega_next = omega + s * omega_dot

    return t_next, phi_next, omega_next, phi_dot, omega_dot


def simulate_rotation(initial_conditions):
    phi = initial_conditions["phi"]
    omega = initial_conditions["omega"]

    # Initialize arrays to store simulation results
    t_array = np.zeros(int(T / s))
    phi_array = np.zeros(int(T / s))
    omega_array = np.zeros(int(T / s))
    alpha_array = np.zeros(int(T / s))

    t = 0
    i = 0

    while t < T:
        # Calculate the controlled angular acceleration using the fuzzy logic control algorithm
        alpha = fuzzy_logic_control(phi, omega)

        # Integrate the system of differential equations using the Euler method
        t, phi, omega, phi_dot, omega_dot = euler_integration(t, phi, omega, alpha)

        # Store the simulation results
        t_array[i] = t
        phi_array[i] = phi
        omega_array[i] = omega
        alpha_array[i] = alpha

        i += 1

    return t_array, phi_array, omega_array, alpha_array


# Step 6: Output the simulation results to a file and plot them
t_array, phi_array, omega_array, alpha_array = simulate_rotation(initial_conditions)

# Save simulation results to a file
np.savetxt(
    "simulation_results.txt",
    np.column_stack((t_array, phi_array, omega_array, alpha_array)),
)

# Plot the simulation results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(t_array, phi_array, label="Angle")
plt.xlabel("Time (s)")
plt.ylabel("Angle (deg)")
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(t_array, omega_array, label="Angular velocity")
plt.xlabel("Time (s)")
plt.ylabel("Angular velocity (deg/s)")
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(t_array, alpha_array, label="Angular acceleration")
plt.xlabel("Time (s)")
plt.ylabel("Angular acceleration (deg/s^2)")
plt.legend()

plt.tight_layout()
plt.show()
