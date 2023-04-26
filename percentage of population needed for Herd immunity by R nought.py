import matplotlib.pyplot as plt
import numpy as np

def herd_immunity(r_0):
    return 1 - 1/r_0

r_0_vals = np.linspace(0.5, 10, 100)
herd_immunity_vals = herd_immunity(r_0_vals)

plt.plot(r_0_vals, herd_immunity_vals)
plt.xlabel("$R_0$")
plt.ylabel("Fraction Immune for Herd Immunity")
plt.title("Percentage of Population Needed for Herd Immunity by $R_0$")
plt.ylim(0, 1)
plt.show()

