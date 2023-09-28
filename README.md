# QMDash
## Description
QMDash is a dashboard to visualize concepts in quantum mechanics for educational purposes. For now, it can be used to visualize the time-dependent nature of wavefunctions in the infinite square well. The user chooses the size of the well, the mass of the particles in it, and the length of time we are simulating its time evolution. Finally, to simulate the wavefunction, the user fills in a table of constants and eigenstates (see Quantum Superposition below).

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

