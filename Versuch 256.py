#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np


#Messwerte (Fe, Ti, Cu, Zr, Mo, Zn, Ni, Ag)
Z=np.array([26,22,29,40,42,30,28,47])
K_alpha=np.array([6.41,4.44,8.08,15.82,17.48,8.67,7.40,21.95])
Delta_K_alpha=np.array([0.20,0.20,0.20,0.25,0.25,0.20,0.20,0.25])
sqrt_K_alpha=np.sqrt(K_alpha)
Delta_sqrt_K_alpha=(0.5*Delta_K_alpha*sqrt_K_alpha)/K_alpha

#sqrt_K_alpha-Z Diagramm
plt.errorbar(Z, sqrt_K_alpha, Delta_sqrt_K_alpha, fmt=".")
plt.xlabel('Keenladumgszahl Z')
plt.ylabel(r'$\sqrt{E_\alpha}/\sqrt{keV}$', fontsize=14)
plt.title(r'$\sqrt{E_\alpha}$' + 'als Funktion von Z')

plt.show()


