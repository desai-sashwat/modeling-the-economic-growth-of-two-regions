import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def H(K1, K2, L1, L2, h=5.0):
    """Capital-induced labor movement function"""
    return ((L1 - L2) / (1 + np.exp(-h * (K2 - K1))) + L2) * (K2 - K1)


def system(state, t, c, params):
    """System of differential equations"""
    K1, K2, L1, L2 = state

    # Unpack parameters
    dk = params['dk']
    dl = params['dl']
    A = params['A']
    phi = params['phi']
    delta = params['delta']
    a = params['a']
    b = params['b']

    # Capital flow equations
    dK1 = dk * (K2 - K1) + A * (K1 ** phi) * (L1 ** (1 - phi)) - delta * K1
    dK2 = dk * (K1 - K2) + A * (K2 ** phi) * (L2 ** (1 - phi)) - delta * K2

    # Calculate H
    h_value = H(K1, K2, L1, L2)

    # Labor flow equations
    dL1 = dl * (L2 - L1) + a * L1 - b * L1 ** 2 - c * h_value
    dL2 = dl * (L1 - L2) + a * L2 - b * L2 ** 2 + c * h_value

    return [dK1, dK2, dL1, dL2]


# Parameters from the paper
params = {
    'dk': 0.1,  # capital diffusion coefficient
    'dl': 0.2,  # labor diffusion coefficient
    'A': 2.0,  # technology level
    'phi': 0.5,  # capital share
    'delta': 3.0,  # depreciation rate
    'a': 0.7,  # labor growth rate
    'b': 1.0,  # crowding coefficient
}

# Initial conditions
initial_state = [0.25, 0.6, 0.9, 0.1]  # [K1_0, K2_0, L1_0, L2_0]

# Create range of c values
c_values = np.linspace(0, 5, 100)
L1_equilibrium = []
L2_equilibrium = []

# Simulate for each c value
for c in c_values:
    # Solve system
    t = np.linspace(0, 20, 1000)
    solution = odeint(system, initial_state, t, args=(c, params))

    # Store equilibrium values (final values)
    L1_equilibrium.append(solution[-1, 2])
    L2_equilibrium.append(solution[-1, 3])

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(c_values, L1_equilibrium, 'b-', label='Labor 1')
plt.plot(c_values, L2_equilibrium, 'r--', label='Labor 2')
plt.xlabel('c')
plt.ylabel('Labor')
plt.legend()
plt.grid(True)
plt.show()