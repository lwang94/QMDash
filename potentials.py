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

    def constants_to_approx_custom_func(self, expression):
        function = u.expression_to_function(expression, self.x)
        func = np.where(self.x<self.a, function, 0)

        func_pdf = func ** 2
        func_probabilities = [
            u.find_area(
                self.x[i], 
                self.x[i+1], 
                func_pdf[i], 
                func_pdf[i+1]
            ) for i in range(len(self.x) - 1)
        ]
        norm_func = func/np.sqrt(np.sum(func_probabilities))

        c = {}
        for i in range(1, 21):
            wf = self.wavefunction(i)
            norm = np.dot(wf, wf)
            c[i] = np.dot(norm_func, wf) / norm
        
        return c


class FreeParticle:

    def __init__(self, x):
        self.x = x

    
    def wavefunction(self, p):
        wf = np.zeros(len(self.x), dtype='complex128')
        for momentum in p:
            wf += np.exp(1j*momentum*x/H_BAR)
        return wf


    def approximate_localization(self, a):
        wf_x = np.where((self.x > -a) & (self.x < a), 1/np.sqrt(2 * a), 0)
        
        w = 1 / (1 / len(self.x))
        p = np.fft.fftfreq(self.x.shape[0]) * w

        wf_p = np.fft.fft(wf_x)

        return self.x, wf_x, p, wf_p
