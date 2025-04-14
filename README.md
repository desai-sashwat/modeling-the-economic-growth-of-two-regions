# Studying the Interconnections Between the Economic Growth of Two Regions Based on Capital and Labor Flow

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Table of Contents
- [Overview](#overview)
- [Authors](#authors)
- [Model Framework](#model-framework)
- [Key Research Questions](#key-research-questions)
- [Methodology](#methodology)
- [Key Findings](#key-findings)
  - [Equilibrium Analysis](#equilibrium-analysis)
  - [Parameter Sensitivity](#parameter-sensitivity)
  - [Threshold Phenomenon](#threshold-phenomenon)
  - [Economic Implications](#economic-implications)
- [Repository Structure](#repository-structure)
- [Usage](#usage)
- [Future Work](#future-work)
- [License](#license)

## Overview
This repository contains the code, analysis, and findings from our research study examining the interconnections between the economic growth of two regions based on capital and labor flow. By integrating the Solow Growth Model with the Malthusian Population Model, we construct a system of four differential equations to capture the complex dynamics between capital accumulation, labor force growth, and inter-regional mobility.

## Authors
- Sashwat Desai (desai.sas@northeastern.edu)
  - MS, Applied Mathematics
  - Northeastern University, Boston

## Model Framework
Our mathematical framework is built on the integration of two classical models:
- **Solow Growth Model** - Explains interactions between capital accumulation, labor force growth, and technological progress
- **Malthusian Population Model** - Describes population growth dynamics with limited resources

The combined model incorporates:
- Capital diffusion between regions
- Labor diffusion between regions
- Capital-induced labor movement
- Region-specific economic parameters

## Key Research Questions
- How do capital and labor flows affect regional economic convergence or divergence?
- What is the impact of capital-induced labor movement on regional economic equity?
- Under what conditions do regions develop symmetrically or asymmetrically?
- How do different parameters (diffusion coefficients, technology levels, etc.) affect system behavior?

## Methodology
The study employs mathematical modeling and numerical simulations:
- Construction of a four-equation system of ordinary differential equations
- Proof of existence and uniqueness of equilibrium points
- Stability analysis of equilibrium states
- Parameter sensitivity analysis
- Numerical simulations under various initial conditions and parameter values

## Key Findings

### Equilibrium Analysis
- The system has a unique positive equilibrium point when capital-induced labor movement is zero (c = 0)
- Equilibrium characteristics depend on the relationships between labor diffusion and growth rates

### Parameter Sensitivity
- Diffusion coefficients (dk and dl) significantly impact equilibrium states
- Technology levels (A1 and A2) affect capital distribution but have limited impact on labor distribution
- Labor growth rates (a1 and a2) directly influence regional development patterns

### Threshold Phenomenon
- A critical threshold exists for capital-induced labor movement (c)
- Below threshold: Regions converge to similar development levels regardless of initial conditions
- Above threshold: Asymmetric development occurs, creating persistent economic inequalities

### Economic Implications
- Unrestricted movement may amplify existing regional disparities rather than reduce them
- Excessive capital-induced labor movement decreases total capital and labor in the system
- Policy interventions may be necessary to balance economic efficiency and regional equity

## Repository Structure
- **LICENSE** - MIT License
- **README.md** - Project documentation
- **python-files/** - Python code for model implementation and analysis
  - **equilibrium-analysis/** - Analysis of equilibrium conditions
    - **Equilibrium Analysis.py** - Analysis of equilibrium states under different parameter conditions
    - **Equilibrium and Stability Analysis.py** - Stability analysis of equilibrium points
    - **Labor and Capital Equilibrium.py** - Analysis of labor-capital equilibrium relationships
    - **placeholder.md** - Placeholder file
  - **main.py** - Core implementation of the two-region economic model
  - **parameter-sensitivity-analysis/** - Analysis of parameter sensitivity
    - **Capital vs c.py** - Relationship between capital and capital-induced labor movement
    - **Labor and Capital Changes for DIfferent Parameters 2.py** - Additional parameter analysis
    - **Labor and Capital Changes for Different Parameters.py** - Parameter sensitivity analysis
    - **Labor vs c.py** - Relationship between labor and capital-induced labor movement
    - **placeholder.md** - Placeholder file
  - **placeholder.md** - Placeholder file
- **report/** - Project report directory
  - **Modeling_the_Economic_Growth_of_Two_Regions_draftv3.pdf** - Research paper/report
  - **placeholder.md** - Placeholder file
- **requirements.txt** - Python package dependencies

## Usage
The main implementation is in `main.py`, which defines the `TwoRegionEconomicModel` class:

```python
# Create model with default parameters
model = TwoRegionEconomicModel()

# Set initial conditions [K1_0, K2_0, L1_0, L2_0]
initial_state = [0.25, 0.6, 0.8, 0.2]

# Run simulation
t, solution = model.simulation(initial_state, 20)

# Plot and analyze results
model.results(t, solution)
model.equilibrium_analysis(t, solution)
plt.show()
```

## Future Work
- Extending the model to incorporate technological diffusion between regions
- Introducing trade barriers and their effects on economic development
- Exploring policy interventions that promote both efficiency and equity
- Expanding the framework to multiple interacting regions
- Incorporating additional factors such as human capital and innovation

## License
This project is licensed under the MIT License - see the LICENSE file for details.
