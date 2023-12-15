# QMDash
## Description
QMDash is a dashboard to visualize basic concepts in quantum mechanics for educational purposes. For now, it can be used to visualize the time-dependent nature of wavefunctions in the infinite square well. The user chooses the size of the well, the mass of the particles in it, and the length of time we are simulating its time evolution. Finally, to simulate the wavefunction, the user fills in a table of constants and eigenstates (see Quantum Mechanics below).

## Dependencies
- Python == 3.11
- Dash == 2.13.0
- Numpy == 1.26.0

## To Run Locally
After installing the above dependencies using pip and cloning the repo, go into the repo. Then run the below command:

`python app.py`

This will run the server locally on `http://127.0.0.1:8050/`. Copy and paste the link into your web browser and you can use the app from there.

## Quantum Mechanics
The dashboard simulates the `time evolution for a quantum superposition of eigenstates in the infinite square well`. Let's pick apart the different parts of that statement.

### The Schrodinger Equation
Before we can dive into the above statement, we first need to start with the Schrodinger Equation shown below:

$$ [-\frac{ℏ}{2m}\frac{\partial^2 }{\partial x^2} + V(x,t)]\Psi (x,t) = iℏ\frac{\partial }{\partial t}\Psi (x,t) $$

This is called a partial differential equation and by solving for $\Psi (x,t)$, we can determine the probability that a particle will be at position `x` at time `t` (note: $\Psi^2 (x,t)$ is the probability density function, NOT $\Psi (x,t)$). 

For now (since this dashboard targets basic concepts in QM), let us assume that the potential $V(x,t)$ does not change with time and is therefore only a function of x (eg. $V(x,t) = V(x)$. We can then use [separation of variables](https://chem.libretexts.org/Courses/Pacific_Union_College/Quantum_Chemistry/02%3A_The_Classical_Wave_Equation/2.02%3A_The_Method_of_Separation_of_Variables) to solve for $\Psi(x,t)$

$$ \Psi(x,t) = \psi(x) \times \varphi(t) $$

where $\psi(x)$ is the solution to the ordinary differential equation:

$$ [-\frac{ℏ}{2m}\frac{\partial^2 }{\partial x^2} + V(x)]\psi (x) = E\psi (x) $$

and $\varphi(t)$ is the solution to the ordinary differential equation:

$$ iℏ\frac{\partial }{\partial t}\varphi (t) = E\varphi(t) $$

### Time Evolution
We can then solve for $\varphi(t)$ easily:

$$ \varphi(t) =  e^{\frac{-iE_{n}t}{ℏ}} $$

In the simulation shown on the dashboard, we see how the probability density changes over time based on the above function.

### Infinite Square Well
In this dashboard, we are concerned with particles in an `Infinite Square Well` potential. This potential is defined by: 

$$ V(x) = \begin{cases}
0 & \text{ if } \ x > 0\ or\ x < a\\
\infty & \text{ if } \ x<= 0\ or\ x>= a
\end{cases} $$

The solution for $\psi_n(x)$ then becomes:

$$ \psi_n(x) = \sqrt{\frac{2}{a}}sin(\frac{n\pi}{a}x) \ \ where \ \ n = 0, 1, 2... $$

and the solution for $\Psi_n(x,t)$ is:

$$ \Psi_n(x,t) = \sqrt{\frac{2}{a}}sin(\frac{n\pi}{a}x)e^{\frac{-iE_{n}t}{ℏ}} \ \ where \ \ n = 0, 1, 2... $$

See https://sciencing.com/particle-in-a-box-13722579.html for more details.

### Eigenstates
The above equation for $\Psi_n(x,t)$ represents the eigenstates of the particle in an `Infinite Square Well`. Eigenstates are an important concept in quantum mechanics as they are states of the wavefunction in which the probability density does not change with time (Try this for yourself! Remove all rows except 1 in the table and set its value of `C` to 1. Then see what happens).

### Quantum Superposition
However, these eigenstates are not the only solutions to the Schrodinger Equation. Any [linear combination](https://en.wikipedia.org/wiki/Linear_combination#:~:text=In%20mathematics%2C%20a%20linear%20combination,a%20and%20b%20are%20constants).) of the above eigenstates are also valid solutions to the Schrodinger Equation. Therefore, any linear combination of eigenstates are valid wavefunctions (so long as their probability density is equal to 1). 

$$\Psi(x,t) = \sum_{n=1}^{\infty}c_n\sqrt{\frac{2}{a}}sin(\frac{n\pi}{a}x)e^{\frac{-iE_{n}t}{ℏ}} \ \  where \ \ \sum_{n=1}^{\infty}|c_n|^{2} = 1 $$

This is called Quantum Superposition and it is a fundamental principle in quantum physics. It is why multiple measurements of the same quantum system can yield different results: the system is in a *superposition* of different eigenstates and the act of measurement collapses it to a single state. The coefficient in front of the eigenstate represents the probability that the system will collapse to that particular eigenstate.

### Table of Constants and Eigenstates
