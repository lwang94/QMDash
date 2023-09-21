import numpy as np
import util as u

class Inf_Square_Well:
    
    def __init__(self, a, x):
        self.a = a
        self.x = x
    
    def wavefunction(self, n):
        return np.where(self.x<self.a, np.sqrt(2/self.a) * np.sin(n*self.x*np.pi/self.a), 0)
    
    def energy(self, n, m):
        return (n**2)*(np.pi**2)*(u.H_BAR**2)/(2*m*(self.a**2))
    
    def time_dependence(self, t, E):
        return np.exp(-1j*E*t/u.H_BAR)