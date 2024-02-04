import numpy as np
import sympy as sym

# h_bar
H_BAR = 1.05457e-34

# unit conversion functions
def hartree_mass(m):
    return m * 9.109e-28


def hartree_length(x):
    return x * 5.29e-11


def hartree_time(t):
    return t * 2.4189e-17


# finding the area under two points on a curve
def find_area(x1, x2, y1, y2):
    return np.abs((x2 - x1) * (y2 + y1) / 2)


# creating eigenstate dictionary
def eigenstate_dictionary(potential, n, c, m, t):
    return {
        "c": c,
        "y": potential.wavefunction(n),
        "t": potential.time_dependence(t, potential.energy(n, m))
    }


# create function from expression
def expression_to_function(expr, axis):
    x = sym.symbols("x")
    ex = sym.sympify(expr)
    return np.array([float(ex.subs(x, index)) for index in axis])