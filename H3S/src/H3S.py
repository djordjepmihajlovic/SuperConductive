import numpy as np  
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from scipy.optimize import curve_fit
import seaborn as sns

f = open("../data/ecut_conv.txt", "r")
ecut = []
E = []
for lines in f:
    if lines[0] == "#":
        continue
    x = str.split(lines)
    ecut.append(float(x[0]))
    E.append(float(x[1]))
f.close()

sns.set_style("whitegrid")
plt.plot(ecut, E, '-', color='k', linewidth=0.75)
plt.plot(ecut, E, 'x', color='k')
plt.xlabel("Energy cutoff (eV)")
plt.ylabel("Total energy (eV)")
plt.legend()

plt.gca().tick_params(which="both", direction="in", right=True, top=True)
plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
plt.gca().xaxis.set_ticks_position('both')
plt.gca().yaxis.set_ticks_position('both')

plt.show()