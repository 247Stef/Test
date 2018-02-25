#sqrt_Er, sig12 sind Fitparameter
n1=1
n2=2
def fit_func(x, sqrt_Er, sig12):
	return sqrt_Er*(x-sig12)*np.sqrt(1/n1**2-1/n2**2)
	
from scipy.optimize import curve_fit
popt, pcov=curve_fit(fit_func, Z, sqrt_K_alpha, sigma=Delta_sqrt_K_alpha)

#popt[0]
#np.sqrt(pcov[0,0])

plt.errorbar(Z, sqrt_K_alpha, Delta_sqrt_K_alpha, fmt=".")
plt.xlabel('Keenladumgszahl Z')
plt.ylabel(r'$\sqrt{E_\alpha}/\sqrt{keV}$', fontsize=14)
plt.title(r'$\sqrt{E_\alpha}$' + 'als Funktion von Z')
plt.plot(Z, fit_func(Z, *popt))

plt.show()

print("sqrt_Er=",popt[0], "Standardfehler=" np.sqrt(pcov[0][0]))
print("sig12=", popt[1], "Standardfehler=" np.sqrt(pcov[1][1]))
