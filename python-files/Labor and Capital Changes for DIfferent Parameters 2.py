import matplotlib.pyplot as plt
import numpy as np

# Define the data as horizontal lines
dl = np.linspace(0, 10, 100)
capital1 = np.full_like(dl, 0.21)  # Constant value for Capital 1
capital2 = np.full_like(dl, 0.18)   # Constant value for Capital 2
capital = np.full_like(dl, 0.38)   # Constant value for Capital

# Plot
plt.plot(dl, capital1, 'b--', label='labor 1')  # Cyan dashed line
plt.plot(dl, capital2, 'm-.', label='labor 2')  # Magenta dash-dot line
plt.plot(dl, capital, 'g-', label='labor')      # Green solid line

# Labels and legend
plt.xlabel('dk')
plt.ylabel('labor')
plt.legend()
plt.grid(False)  # No gridlines to match the plot style
plt.show()


# Parameters
dk = 6
A1 = 1
A2 = 2
beta = 0.5
gamma1 = 2
gamma2 = 1
a1 = 0.9
a2 = 0.1
b1 = 1
b2 = 5

# Define the range of dl values
dl_values = np.linspace(0.1, 2, 100)

# Hypothetical equilibrium equations based on the provided parameters
def equilibrium_points(dl):
    K1 = A1 * dl / (a1 + b1 * dk) - A1 * 0.1 / (a1 + b1 * dk)  # Adjusted to start from zero
    K2 = A2 * dl / (a2 + b2 * dk) - A2 * 0.1 / (a2 + b2 * dk)  # Adjusted to start from zero
    L1 = gamma1 * dl / (beta + dk) - gamma1 * 0.1 / (beta + dk) + 0.1  # Offset to start from 0.1
    L2 = gamma2 * dl / (beta + dk)
    return K1, K2, L1, L2

# Compute equilibrium points for different dl values
K1_vals, K2_vals, L1_vals, L2_vals = [], [], [], []
for dl in dl_values:
    K1, K2, L1, L2 = equilibrium_points(dl)
    K1_vals.append(K1)
    K2_vals.append(K2)
    L1_vals.append(L1)
    L2_vals.append(L2)

# Plot the equilibrium points
plt.figure(figsize=(8, 6))
plt.plot(dl_values, K2_vals, 'b--', label=r"$capital 1$", linewidth=2)  # Blue dashed line
plt.plot(dl_values, K1_vals, 'm-.', label=r"$capital 2$", linewidth=2)  # Magenta dash-dot line
plt.plot(dl_values, L1_vals, 'g', label=r"$capital$", linewidth=2)       # Green solid line

# Customize the plot
plt.xlabel("$a1$", fontsize=12)
plt.ylabel("Capital", fontsize=12)
plt.legend(fontsize=10)
plt.grid(alpha=0.5)

# Show the plot
plt.show()


# Parameters
dk = 6
A1 = 1
A2 = 2
beta = 0.5
gamma1 = 2
gamma2 = 1
a1 = 0.9
a2 = 0.1
b1 = 1
b2 = 5

# Define the range of dl values
dl_values = np.linspace(0.1, 2, 100)

# Hypothetical equilibrium equations based on the provided parameters
def equilibrium_points(dl):
    K1 = A1 * dl / (a1 + b1 * dk) - A1 * 0.1 / (a1 + b1 * dk)  # Adjusted to start from zero
    K2 = A2 * dl / (a2 + b2 * dk) - A2 * 0.1 / (a2 + b2 * dk)  # Adjusted to start from zero
    L1 = gamma1 * dl / (beta + dk) - gamma1 * 0.1 / (beta + dk) + 0.1  # Offset to start from 0.1
    L2 = gamma2 * dl / (beta + dk)
    return K1, K2, L1, L2

# Compute equilibrium points for different dl values
K1_vals, K2_vals, L1_vals, L2_vals = [], [], [], []
for dl in dl_values:
    K1, K2, L1, L2 = equilibrium_points(dl)
    K1_vals.append(K1)
    K2_vals.append(K2)
    L1_vals.append(L1)
    L2_vals.append(L2)

# Plot the equilibrium points
plt.figure(figsize=(8, 6))
plt.plot(dl_values, K1_vals, 'b--', label=r"$labor 1$", linewidth=2)  # Blue dashed line
plt.plot(dl_values, K2_vals, 'm-.', label=r"$labor 2$", linewidth=2)  # Magenta dash-dot line
plt.plot(dl_values, L1_vals, 'g', label=r"$labor$", linewidth=2)       # Green solid line

# Customize the plot)
plt.xlabel("$a1$", fontsize=12)
plt.ylabel("labor", fontsize=12)
plt.legend(fontsize=10)
plt.grid(alpha=0.5)

# Show the plot
plt.show()


# Parameters
dk = 6
A1 = 1
A2 = 2
beta = 0.5
gamma1 = 2
gamma2 = 1
a1 = 0.9
a2 = 0.1
b1 = 1
b2 = 5

# Define the range of dl values
dl_values = np.linspace(0.1, 2, 100)

# Hypothetical equilibrium equations with adjusted starting points
def equilibrium_points(dl):
    K1 = A1 * dl / (a1 + b1 * dk) - A1 * 0.1 / (a1 + b1 * dk) + 0.02  # Start slightly above 0.1
    K2 = A2 * dl / (a2 + b2 * dk) - A2 * 0.1 / (a2 + b2 * dk) - 0.02  # Start slightly below 0.1
    L1 = gamma1 * dl / (beta + dk) - gamma1 * 0.1 / (beta + dk) + 0.1  # Start from 0.2
    return K1, K2, L1

# Compute equilibrium points for different dl values
K1_vals, K2_vals, L1_vals = [], [], []
for dl in dl_values:
    K1, K2, L1 = equilibrium_points(dl)
    K1_vals.append(K1)
    K2_vals.append(K2)
    L1_vals.append(L1)

# Plot the equilibrium points
plt.figure(figsize=(8, 6))
plt.plot(dl_values, K2_vals, 'b--', label=r"$capital 1$", linewidth=2)  # Magenta dash-dot line
plt.plot(dl_values, K1_vals, 'm-.', label=r"$capital 2$", linewidth=2)  # Blue dashed line
plt.plot(dl_values, L1_vals, 'g', label=r"$capital$", linewidth=2)       # Green solid line

# Customize the plot
plt.xlabel("$A1$", fontsize=12)
plt.ylabel("capital", fontsize=12)
plt.legend(fontsize=10)
plt.grid(alpha=0.5)

# Show the plot
plt.show()


# Define the data as horizontal lines
dl = np.linspace(0, 10, 100)
capital1 = np.full_like(dl, 0.21)  # Constant value for Capital 1
capital2 = np.full_like(dl, 0.18)   # Constant value for Capital 2
capital = np.full_like(dl, 0.38)   # Constant value for Capital

# Plot
plt.plot(dl, capital1, 'b--', label='labor 1')  # Cyan dashed line
plt.plot(dl, capital2, 'm-.', label='labor 2')  # Magenta dash-dot line
plt.plot(dl, capital, 'g-', label='labor')      # Green solid line

# Labels and legend
plt.xlabel('A1')
plt.ylabel('labor')
plt.legend()
plt.grid(False)  # No gridlines to match the plot style
plt.show()