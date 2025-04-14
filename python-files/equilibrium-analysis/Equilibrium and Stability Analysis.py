# %%
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
    numerator = (1 - a2 / dl) + np.sqrt((1 - a2 / dl)**2 + 4 * b2 / dl * L1)
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
plt.title('Graph of $f(L_1)$ and $g^{-1}(L_1)$')
plt.xlabel('$L_1$')
plt.ylabel('$L_2$')

# Set axis limits to start from 0 and remove any gap
plt.xlim(0, 10)  # Ensure x-axis starts from 0
plt.ylim(min(min(f_values), min(g_inv_values)), max(max(f_values), max(g_inv_values)))  # Set y-axis limits

plt.show()

# %%
