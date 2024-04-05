import numpy as np  
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from scipy.optimize import curve_fit
import seaborn as sns

f = open("../data/ecut_conv.txt", "r")
ecut = []
E = []
conv = 13.6057
for lines in f:
    if lines[0] == "#":
        continue
    x = str.split(lines)
    ecut.append(float(x[0]))
    E.append(0.5*float(x[1])*conv)
f.close()

f = open("../data/k_conv.txt", "r")
k = []
E_k = []
for lines in f:
    if lines[0] == "#":
        continue
    x = str.split(lines)
    k.append(float(x[0]))
    E_k.append(0.5*float(x[1])*conv)

f.close()

w = [2, 3, 4, 6, 8]
print(len(w))
lamb = [[] for _ in range(0, len(w))]
Tc = [[] for _ in range(0, len(w))]

for idw, wl in enumerate(w):
    f = open(f"../data/lambda_{wl}.out", "r")

    for enum, lines in enumerate(f):
        if lines[0] == "#":
            continue
        x = str.split(lines)
        print(idw)
        lamb[idw].append(float(x[0]))
        Tc[idw].append(float(x[2]))
    f.close()


for i in range(len(E)):
    if abs(E[-1] - E[i]) < 0.001:
        
        print(ecut[i])

sns.set_style("whitegrid")
plt.plot(ecut, E, '-', color='k', linewidth=0.75)
plt.plot(ecut, E, 'x', color='k')

plt.xlabel("Energy cutoff (eV)")
plt.ylabel("Total energy (eV)")
plt.title("Energy cutoff convergence for H$_3$S")
plt.legend()

plt.gca().tick_params(which="both", direction="in", right=True, top=True)
plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
plt.gca().xaxis.set_ticks_position('both')
plt.gca().yaxis.set_ticks_position('both')

plt.show()

for i in range(len(E_k)):
    if abs(E_k[-1] - E_k[i]) < 0.001:
        
        print(k[i])

sns.set_style("whitegrid")
plt.plot(k, E_k, '-', color='k', linewidth=0.75)
plt.plot(k, E_k, 'x', color='k')

plt.xlabel("(N$_k$, N$_k$, N$_k$) k-point grid value")
plt.ylabel("Total energy (eV)")
plt.title("$N_k$ energy convergence for H$_3$S")
plt.legend()

plt.gca().tick_params(which="both", direction="in", right=True, top=True)
plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
plt.gca().xaxis.set_ticks_position('both')
plt.gca().yaxis.set_ticks_position('both')

plt.show()

sns.set_style("whitegrid")
print(w)

plt.plot(lamb[0], Tc[0], '-', color='k', linewidth=0.75, label="$N_q$=2")
plt.plot(lamb[0], Tc[0], 'x', color='k')
plt.plot(lamb[1], Tc[1], '-', color='b', linewidth=0.75, label="$N_q$=3")
plt.plot(lamb[1], Tc[1], 'x', color='b')
plt.plot(lamb[2], Tc[2], '-', color='r', linewidth=0.75, label="$N_q$=4")
plt.plot(lamb[2], Tc[2], 'x', color='r')
plt.plot(lamb[3], Tc[3], '-', color='g', linewidth=0.75, label="$N_q$=6")
plt.plot(lamb[3], Tc[3], 'x', color='g')
plt.plot(lamb[4], Tc[4], '-', color='y', linewidth=0.75, label="$N_q$=8")
plt.plot(lamb[4], Tc[4], 'x', color='y')

plt.xlabel("Lambda")
plt.ylabel("Critical temperature, $T_c$ (K)")
plt.title("Critical temperature convergence wrt $N_q$ for H$_3$S")
plt.legend()

plt.gca().tick_params(which="both", direction="in", right=True, top=True)
plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
plt.gca().xaxis.set_ticks_position('both')
plt.gca().yaxis.set_ticks_position('both')

plt.show()

data_points = np.linspace(3, 33, 11)
print(data_points)
for c, k in enumerate(data_points):
    f = open(f"../data/h3s_dos_tetra_{int(k)}.dat", "r")
    z = open(f"../data/EFermi.dat", "r")
    h3s_e = []
    h3s_dos_1 = []
    h3s_dos_2 = []

    for lines in f:
        if lines[0] == "#":
            continue
        x = str.split(lines)
        h3s_e.append(float(x[0]))
        h3s_dos_1.append(float(x[1]))

    for num, lines in enumerate(z):
        if lines[0] == "#":
            continue
        if num == c:
            x = str.split(lines)
            EFermi = float(x[1])
            break
    z.close()

    f.close()
    h3s_e = np.array(h3s_e)
    bounds = np.where(h3s_e<EFermi)[0]
    print(bounds)
    h3s_dos_fill = []
    h3s_e_fill = []

    for i in bounds:
        h3s_dos_fill.append(h3s_dos_1[i])
        h3s_e_fill.append(h3s_e[i]) 


    sns.set_style("whitegrid")
    plt.plot(h3s_e, h3s_dos_1, "-", color="black")
    plt.axvline(EFermi, color="red", linestyle="--", label="Fermi energy")
    plt.fill_between(h3s_e_fill, h3s_dos_fill, color='blue', alpha=0.3)  # Fill area under the curve
    # Annotation for Fermi energy line
    plt.text(EFermi, max(h3s_dos_1), f'EFermi (eV) = {EFermi}', verticalalignment='bottom', horizontalalignment='right')
    plt.ylabel(r'DOS d(E)')
    plt.xlabel(r"Energy (ev)")
    plt.legend()
    plt.title(f"Energy DOS for H$_3$S at k-point grid $N_k=${k}")
    plt.gca().tick_params(which="both", direction="in", right=True, top=True)
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().xaxis.set_ticks_position('both')
    plt.gca().yaxis.set_ticks_position('both')
    plt.savefig(f"../plots/h3s.e-dos-{int(k)}.png")
    plt.clf()




