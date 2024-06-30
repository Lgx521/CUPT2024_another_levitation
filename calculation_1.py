import matplotlib.pyplot as plt
from numpy import *
from kit.Constants import *


dt = 0.001
t_max = 1

steps = int(t_max / dt)

z = [0.0] * steps
z1 = [0.0] * steps
z2 = [0.0] * steps

z[0] = H + h0

for i in range(steps - 1):
    h = z[i] - H
    F1 = (5 / (6 * (R ** 2))) * (1 / h - 1 / (h + D))
    F2 = (1 / (6 * (R ** 3))) * (arctan((h / R)) - arctan((h + D) / R))
    F3 = (log(1 + ((R ** 2) / (h ** 2)))) / (6 * (h ** 3)) - (log(1 + (R ** 2 / (h + D) ** 2))) / (6 * ((h + D) ** 3))
    F4 = -5 / (18 * (h ** 3)) + 5 / (18 * ((h + D) ** 3))
    F_l = ((9 * sigma * z1[i] * (mu_0 ** 2) * (m_2 ** 2)) / (8 * pi)) * (F1 + F2 + F3 + F4)
    F_m = (3 * mu_0 * m_1 * m_2) / (2 * pi * (z[i] ** 4))
    z2[i] = -g + F_m / m + F_l / m
    z1[i + 1] = z1[i] + dt * z2[i]
    z[i + 1] = z[i] + dt * z1[i]

t = [0.0] * steps
for i in range(steps):
    t[i] = (i + 1) * dt

ypoints = np.array(z)
xpoints = np.array(t)

name = '/Users/gansz/Downloads/CUPT2024/PythonAnalysis/plots/plot_1.png'

plt.plot(xpoints, ypoints, lw='0.5')
plt.savefig(name, dpi=320)
plt.show()
