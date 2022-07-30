##################################
### CREATED BY: BRENO CABRAL ####
########## JULY/2022 ############
import numpy as np
from scipy.optimize import root


# set your variables below:
T = 8 # period
d = 5 # depth

omega =  2*np.pi/T # angular frequency


def dispersion_eq(k, w2 = omega**2, d = d, g = 9.8):
  return((g*k*np.tanh(d*k)/w2)-1) # -> written in a way that it should return 0, if well adjusted

o = 1 # order of magnitude of k

k = root(dispersion_eq, o).x[0]
L = 2 * np.pi/k # wavelength

# dispersion_eq(k)  -> if you wish to see the proof
