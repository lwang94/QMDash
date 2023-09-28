# QMDash
## Description
QMDash is a dashboard to visualize basic concepts in quantum mechanics for educational purposes. For now, it can be used to visualize the time-dependent nature of wavefunctions in the infinite square well. The user chooses the size of the well, the mass of the particles in it, and the length of time we are simulating its time evolution. Finally, to simulate the wavefunction, the user fills in a table of constants and eigenstates (see Quantum Superposition below).

## Dependencies
- Python == 3.11
- Dash == 2.13.0
- Numpy == 1.26.0

## To Run Locally
After installing the above dependencies using pip and cloning the repo, go into the repo. Then run the below command:

`python app.py`

This will run the server locally on `http://127.0.0.1:8050/`. Copy and paste the link into your web browser and you can use the app from there.

## Quantum Superposition
The dashboard simulates the `time evolution for a quantum superposition of eigenstates in the infinite square well`. Let's pick apart the different parts of that statement.

### The Schrodinger Equation
Before we can dive into the above statement, we first need to start with the Schrodinger Equation shown below:

$$ [-\frac{ℏ}{2m}\frac{\partial^2 }{\partial x^2} + V(x,t)]\Psi (x,t) = iℏ\frac{\partial }{\partial t}\Psi (x,t) $$

This is called a partial differential equation and by solving for $\Psi (x,t)$, we can determine the probability that a particle will be at position `x` at time `t` (note: $\Psi^2 (x,t)$ is the probability density function, NOT $ \Psi (x,t) $). 

For now (since this dashboard targets basic concepts in QM), let us assume that the potential $V(x,t)$ does not change with time and is therefore only a function of x (eg. $V(x,t) = V(x)$. We can then use [separation of variables](https://chem.libretexts.org/Courses/Pacific_Union_College/Quantum_Chemistry/02%3A_The_Classical_Wave_Equation/2.02%3A_The_Method_of_Separation_of_Variables) to solve for $\Psi(x,t)$

$$ \Psi(x,t) = \psi(x) \times \varphi(t) $$

where $\psi(x)$ is the solution to the ordinary differential equation:

$$ [-\frac{ℏ}{2m}\frac{\partial^2 }{\partial x^2} + V(x)]\psi (x) = E\psi (x) $$

and $\varphi(t)$ is the solution to the ordinary differential equation:

$$ iℏ\frac{\partial }{\partial t}\varphi (t) = E\varphi(t) $$

### Time Evolution

### Quantum Superposition

### Eigenstates

### Infinite Square Well

### Table of Constants and Eigenstates
