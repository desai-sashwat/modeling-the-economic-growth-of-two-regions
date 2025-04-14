import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


class TwoRegionEconomicModel:
    def __init__(self, params=None):
        """
        Initialize the two-region economic growth model based on Solow-Malthusian framework

        Parameters:
        params (dict)
        """
        self.params = params if params else {
            'dk': 0.1,      #capital diffusion coefficient
            'dl': 0.2,      #labor diffusion coefficient
            'c': 3.5,       #capital-induced labor movement strength
            'A1': 2.0,      #technology level for region 1
            'A2': 2.0,      #technology level for region 2
            'phi': 0.5,     #capital share (0 < phi < 1)
            'delta1': 3.0,  #capital depreciation rate for region 1
            'delta2': 3.0,  #capital depreciation rate for region 2
            'a1': 0.7,      #labor growth rate for region 1
            'a2': 0.7,      #labor growth rate for region 2
            'b1': 1.0,      #labor crowding coefficient for region 1
            'b2': 5.0,      #labor crowding coefficient for region 2
            'h': 5.0        # Smoothing parameter for sigmoid
        }

    def capital_induced_labor_movement(self, K1, K2, L1, L2):
        """
        Calculate the capital-induced labor movement using smooth sigmoid function
        as defined in equation (3.3) of the paper
        """
        h = self.params['h']
        return ((L1 - L2) / (1 + np.exp(-h * (K2 - K1))) + L2) * (K2 - K1)

    def system(self, state, t):
        """
        Define the system of ODEs as given in equations (3.1) of the paper

        Parameters:
        state: Current state [K1, K2, L1, L2]
        t: Time point

        Returns:
        List of derivatives [dK1/dt, dK2/dt, dL1/dt, dL2/dt]
        """
        K1, K2, L1, L2 = state
        p = self.params

        # Capital flow equations
        dK1 = p['dk'] * (K2 - K1) + p['A1'] * K1 ** p['phi'] * L1 ** (1 - p['phi']) - p['delta1'] * K1
        dK2 = p['dk'] * (K1 - K2) + p['A2'] * K2 ** p['phi'] * L2 ** (1 - p['phi']) - p['delta2'] * K2

        # Calculate capital-induced labor movement
        H = self.capital_induced_labor_movement(K1, K2, L1, L2)

        # Labor flow equations
        dL1 = p['dl'] * (L2 - L1) + p['a1'] * L1 - p['b1'] * L1 ** 2 - p['c'] * H
        dL2 = p['dl'] * (L1 - L2) + p['a2'] * L2 - p['b2'] * L2 ** 2 + p['c'] * H

        return [dK1, dK2, dL1, dL2]

    def simulation(self, initial_state, t_span, t_points=1000):
        """
        Simulate the system over specified time period

        Parameters:
        initial_state: Initial values [K1_0, K2_0, L1_0, L2_0]
        t_span: Time duration
        t_points: Number of time points

        Returns:
        t: Time points
        solution: Solution array with shape (t_points, 4)
        """
        t = np.linspace(0, t_span, t_points)
        solution = odeint(self.system, initial_state, t)
        return t, solution

    def results(self, t, solution, show_total=True):
        """
        Plot the simulation results with capital and labor evolution in the same graph

        Parameters:
        t: Time points
        solution: Solution array
        show_total: Whether to plot total capital and labor
        """
        fig, ((ax1, ax2), (ax3, ax3)) = plt.subplots(2, 2, figsize=(15, 12))

        # Plot capital and labor evolution in the same graph
        ax1.plot(t, solution[:, 0], 'b-', label='Capital Region 1')
        ax1.plot(t, solution[:, 1], 'r--', label='Capital Region 2')
        ax1.plot(t, solution[:, 2], 'g-', label='Labor Region 1')
        ax1.plot(t, solution[:, 3], 'm--', label='Labor Region 2')
        ax1.set_title('Capital and Labor Evolution')
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Value')
        ax1.legend()

        # Plot capital differences
        ax2.plot(t, solution[:, 1] - solution[:, 0], 'k-')
        ax2.set_title('Capital Difference (K2 - K1)')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Difference')
        ax2.axhline(y=0, color='gray', linestyle=':')

        # Plot labor differences
        ax3.plot(t, solution[:, 3] - solution[:, 2], 'k-')
        ax3.set_title('Labor Difference (L2 - L1)')
        ax3.set_xlabel('Time')
        ax3.set_ylabel('Difference')
        ax3.axhline(y=0, color='gray', linestyle=':')

        plt.tight_layout()
        return fig

    def calculate_equilibrium_time(self, t, solution, threshold=1e-4):
        """
        Calculate the time at which the system reaches equilibrium

        Parameters:
        t: Time points array
        solution: Solution array
        threshold: Threshold for considering system at equilibrium

        Returns:
        float: Time at which equilibrium is reached
        """
        # Calculate changes in state variables
        changes = np.abs(np.diff(solution, axis=0))

        # Sum changes across all variables at each time point
        total_changes = np.sum(changes, axis=1)

        # Find first point where changes are below threshold
        equilibrium_index = np.where(total_changes < threshold)[0]

        if len(equilibrium_index) > 0:
            equilibrium_time = t[equilibrium_index[0] + 1]
            return equilibrium_time
        else:
            return None

    # Modify the equilibrium_analysis method to include this calculation
    def equilibrium_analysis(self, t, solution):
        """
        Analyze the equilibrium state of the system
        """
        final_state = solution[-1]
        K1, K2, L1, L2 = final_state

        eq_time = self.calculate_equilibrium_time(t, solution)

        print("Equilibrium Analysis:")
        print(f"Region 1: K = {K1:.4f}, L = {L1:.4f}")
        print(f"Region 2: K = {K2:.4f}, L = {L2:.4f}")
        print(f"Capital difference (K2-K1): {K2 - K1:.4f}")
        print(f"Labor difference (L2-L1): {L2 - L1:.4f}")
        print(f"Total capital: {K1 + K2:.4f}")
        print(f"Total labor: {L1 + L2:.4f}")
        if eq_time is not None:
            print(f"Time to reach equilibrium: {eq_time:.4f}")
        else:
            print("System did not reach equilibrium in the simulation time")


# Example usage:
if __name__ == "__main__":
    # Create model with default parameters
    model = TwoRegionEconomicModel()

    # Set initial conditions
    initial_state = [0.25, 0.6, 0.8, 0.2]  # [K1_0, K2_0, L1_0, L2_0]

    # Run simulation
    t, solution = model.simulation(initial_state, 20)

    # Plot and analyze results
    model.results(t, solution)
    model.equilibrium_analysis(t, solution)
    plt.show()