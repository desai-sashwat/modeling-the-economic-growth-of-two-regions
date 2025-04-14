# %% Case 1:
import numpy as np
import matplotlib.pyplot as plt

# Parameters
a1 = 1
a2 = 2
dl = 3
b1 = 1
b2 = 2


# Functions for f(L1) and g⁻¹(L1)
def f(L1):
    return L1 * (1 - a1 / dl) + b1 / dl


def g_inv(L1):
    numerator = (1 - a2 / dl) + np.sqrt((1 - a2 / dl) ** 2 + 4 * b2 / dl * L1)
    denominator = 2 * b2 / dl
    return numerator / denominator


# Range of L1 values
L1 = np.linspace(0, 10, 500)  # Adjust the range as needed

# Calculate f(L1) and g⁻¹(L1)
f_values = f(L1)
g_inv_values = g_inv(L1)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(L1, f_values, label=r'$f(L_1)$', color='blue')
plt.plot(L1, g_inv_values, label=r'$g^{-1}(L_1)$', color='orange')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

# Add labels and legend
plt.xlabel('$L_1$')
plt.ylabel('$L_2$')

# Set axis limits to start from 0 and remove any gap
plt.xlim(0, 10)  # Ensure x-axis starts from 0
plt.ylim(min(min(f_values), min(g_inv_values)), max(max(f_values), max(g_inv_values)))  # Set y-axis limits

plt.legend()
plt.show()

# %% Case 2:
import numpy as np
import matplotlib.pyplot as plt

# Parameters for Case 2
a1 = 1
a2 = 2
dl = 1.5
b1 = 1
b2 = 2
y = np.linspace(0, 2, 500)


# Functions for f(L1) and g⁻¹(L1) with adjustments for specific intersections
def f(L1):
    return (-1) * y / 3 + 2 * y ** 2 / 3 + L1  # Adjusted to make the line start at 0


def g_inv(L1):
    numerator = (1 - a2 / dl) + np.sqrt((1 - a2 / dl) ** 2 + 4 * b2 / dl * L1)
    denominator = 2 * b2 / dl
    return numerator / denominator + 0.2  # Offset by 0.2


# Range of L1 values (smaller range to focus on intersection)
L1 = np.linspace(0, 2, 500)  # Small L1 range

# Calculate f(L1) and g⁻¹(L1)
f_values = f(L1)
g_inv_values = g_inv(L1)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(L1, f_values, label=r'$f(L_1)$', color='blue')
plt.plot(L1, g_inv_values, label=r'$g^{-1}(L_1)$', color='orange')

# Add labels and legend
plt.xlabel(r'x')
plt.ylabel(r'y')

# Set axis limits to remove gaps and align zero points
plt.xlim(0, 2)  # Set x-axis range starting from 0
plt.ylim(0, max(max(f_values), max(g_inv_values)))  # Set y-axis range starting from 0

# Show legend and plot
plt.legend()
plt.show()

# %% Case 3:
import numpy as np
import matplotlib.pyplot as plt

# Parameters for Case 3
a1 = 1
a2 = 2
dl = 1.5
b1 = 1
b2 = 2
y = np.linspace(0, 2, 500)


# Functions for f(L1) and g⁻¹(L1)
def f(L1):
    return (-1) * y / 3 + 2 * y ** 2 / 3


def g_inv(L1):
    numerator = (1 - a2 / dl) + np.sqrt((1 - a2 / dl) ** 2 + 4 * b2 / dl * L1)
    denominator = 2 * b2 / dl
    return numerator / denominator


# Range of L1 values (smaller range to focus on intersection)
L1 = np.linspace(0, 2, 500)  # Small L1 range

# Calculate f(L1) and g⁻¹(L1)
f_values = f(L1)
g_inv_values = g_inv(L1)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(L1, f_values, label=r'$f(L_1)$', color='blue')
plt.plot(L1, g_inv_values, label=r'$g^{-1}(L_1)$', color='orange')

# Add labels and legend
plt.xlabel(r'x')
plt.ylabel(r'y')

# Set axis limits to remove gaps and align zero points
plt.xlim(0, 2)  # Set x-axis range starting from 0
plt.ylim(0, max(max(f_values), max(g_inv_values)))  # Set y-axis range starting from 0
plt.legend()
plt.show()

# %% Case 4:
import numpy as np
import matplotlib.pyplot as plt

# Parameters for Case 4
a1 = 2
a2 = 1
dl = 0.5
b1 = 1
b2 = 2
y = np.linspace(0, 2, 500)


# Updated functions for f(L1) and g⁻¹(L1)
def f(L1):
    return -y + 4 * y ** 2  # Updated function for x = -y + 4y^2


def g_inv(L1):
    numerator = (1 - a2 / dl) + np.sqrt((1 - a2 / dl) ** 2 + 4 * b2 / dl * L1)
    denominator = 2 * b2 / dl
    return numerator / denominator + 0.2  # Offset by 0.2


# Range of L1 values (smaller range to focus on intersection)
L1 = np.linspace(0, 2, 500)  # Small L1 range

# Calculate f(L1) and g⁻¹(L1)
f_values = f(L1)
g_inv_values = g_inv(L1)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(L1, f_values, label=r'$f(L_1)$', color='blue')
plt.plot(L1, g_inv_values, label=r'$g^{-1}(L_1)$', color='orange')

# Add labels and legend
plt.xlabel(r'x')
plt.ylabel(r'y')

# Set axis limits to remove gaps and align zero points
plt.xlim(0, 1)  # Set x-axis range starting from 0
plt.ylim(0, 1)  # Set y-axis range starting from 0

# Show legend and plot
plt.legend()
plt.show()

# %% Case 5:
import numpy as np
import matplotlib.pyplot as plt

# Define parameters
dk = 6
dl = 5
A1 = 1
A2 = 2
gamma = 0.5
theta1 = 2
theta2 = 1
a1 = 0.9
a2 = 0.1
b1 = 1
b2 = 5

# Define initial values
K1_0 = 0.5
K2_0 = 0.1
L1_0 = 0.4
L2_0 = 0.3

# Time span
t = np.linspace(0, 10, 1000)  # Increase the number of points for higher resolution


# Define the system of differential equations
def system(y, t, dk, dl, A1, A2, gamma, theta1, theta2, a1, a2, b1, b2):
    K1, K2, L1, L2 = y
    dK1_dt = dk * (K2 - K1) + A1 * K1 * L1
    dK2_dt = dk * (K1 - K2) + A2 * K2 * L2
    dL1_dt = dl * (L2 - L1) + a1 * L1 - b1 * L2
    dL2_dt = dl * (L1 - L2) + a2 * L2 - b2 * L2
    return [dK1_dt, dK2_dt, dL1_dt, dL2_dt]


# Solve the system using numerical integration
from scipy.integrate import odeint

y0 = [K1_0, K2_0, L1_0, L2_0]
solution = odeint(system, y0, t, args=(dk, dl, A1, A2, gamma, theta1, theta2, a1, a2, b1, b2))

K1 = solution[:, 0]
K2 = solution[:, 1]
L1 = solution[:, 2]
L2 = solution[:, 3]

# Plot the results
plt.figure(figsize=(8, 4))
plt.plot(t, K1, 'b-', label='capital 1')
plt.plot(t, K2, 'g-', label='capital 2')
plt.plot(t, L1, 'k-', label='labor 1')
plt.plot(t, L2, 'r--', label='labor 2')
plt.xlabel('time', fontsize=12)
plt.ylabel('capital amount / population', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust x-axis and y-axis for better visualization
plt.xlim([0, 10])  # Extend x-axis to 10
plt.ylim([0, 1])  # Adjust y-axis range
plt.xticks(np.arange(0, 10, 1))  # Make x-axis ticks more granular
plt.yticks(np.arange(0, 1.5, 0.5))  # Make y-axis ticks more granular

plt.show()
