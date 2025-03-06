# Infectious Disease Simulation Using Cellular Automata

This repository implements a simulation of infectious disease spread using cellular automata. The model is based on the Susceptible-Infected-Recovered (SIR) framework, where individuals in a population are represented as cells on a grid. The grid evolves over time, with susceptible individuals becoming infected based on their interactions with neighboring infected cells, and infected individuals transitioning to a recovered state after a specified recovery time.

## **Features**
- **Grid-based Simulation**: A 50x50 grid representing a population of individuals.
- **Infection Dynamics**: Susceptible individuals become infected with a probability \( p_{\text{infection}} \) when neighboring infected individuals are present.
- **Recovery Time**: Infected individuals recover after \( t_{\text{recovery}} \) time steps and become immune.
- **Visualization**: The simulation is visualized using `Matplotlib`, with an animated display showing the spread of the infection over time.

## **How to Run**
### **Requirements**
To run the simulation, you need to have the following Python packages installed:
- **NumPy**
- **Matplotlib**

You can install them using `pip`:

```bash
pip install numpy matplotlib
```
## **Running the Simulation**

To run the simulation, execute the Python script:

```bash
python infectious_disease_simulation.py
```

The simulation will run for a set number of steps (`steps = 100` by default) and display an animated plot showing how the infection spreads over time. The infection probability (`p_infection`) and recovery time (`t_recovery`) are configurable in the script.

## **Parameters**
- **grid_size**: The size of the grid (50x50 by default).
- **p_infection**: The probability of an individual becoming infected if one of its neighbors is infected (default: 0.3).
- **t_recovery**: The number of time steps it takes for an infected individual to recover (default: 2).
- **steps**: The number of simulation steps to run (default: 100).

## **Code Explanation**
- **Initialization**: A grid of size `50x50` is initialized where each cell represents an individual in the population. Initially, a small fraction of individuals are infected (5 random individuals).
- **Update Function**: In each frame of the animation, the simulation updates based on the following rules:
  - Susceptible individuals (0) become infected if a neighboring cell is infected and a random value is less than `p_infection`.
  - Infected individuals (1) recover after `t_recovery` time steps and transition to the recovered state (2).
- **Visualization**: The grid is displayed using a color map, where:
  - **0** represents susceptible individuals (green).
  - **1** represents infected individuals (yellow).
  - **2** represents recovered individuals (purple).