import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Provided data
years = np.array([2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016])
population = np.array([4253641, 4383184, 4516571, 4654245, 4795967, 4942026, 5092533, 5247624, 5407489, 5572285, 5742093])

# Logistic function
def logistic_growth(t, K, P0, r):
    return K * P0 / (P0 + (K - P0) * np.exp(-r * (t - years[0])))

# Fit model
popt, _ = curve_fit(logistic_growth, years, population, p0=[10_000_000, population[0], 0.03])

# Extract parameters
K, P0, r = popt
print(f"Estimated Carrying Capacity (K): {K:.2f}")

# Plot
plt.scatter(years, population, label="Data")
plt.plot(years, logistic_growth(years, *popt), label="Logistic Growth", color='red')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.show()