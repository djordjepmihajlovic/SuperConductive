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

data_points = np.linspace(3, 33, 11)
print(data_points)
for k in data_points:
    f = open(f"../data/h3s_dos_tetra_{int(k)}.dat", "r")
    h3s_e = []
    h3s_dos_1 = []
    h3s_dos_2 = []

    for lines in f:
        if lines[0] == "#":
            continue
        x = str.split(lines)
        h3s_e.append(float(x[0]))
        h3s_dos_1.append(float(x[1]))

    f.close()

    sns.set_style("whitegrid")
    plt.plot(h3s_dos_1, h3s_e, "-", color="black")
    plt.xlabel(r'DOS d(E)')
    plt.ylabel(r"Energy (ev)")
    plt.title(f"Energy DOS for H3S at k point {k}")
    plt.gca().tick_params(which="both", direction="in", right=True, top=True)
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().xaxis.set_ticks_position('both')
    plt.gca().yaxis.set_ticks_position('both')
    plt.savefig(f"../plots/h3s.e-dos-{int(k)}.png")
    plt.clf()




