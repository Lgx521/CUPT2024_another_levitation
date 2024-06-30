import numpy as np
import matplotlib.pyplot as plt

#save path
path = '/Users/gansz/Downloads/CUPT2024/PythonAnalysis/plots/forceByEddyCurrent.png'

def log(x):
    return np.log(x)

def atan(x):
    return np.arctan(x)

pi = 3.1415926535

g = 9.7887

V = pi * (1.5 ** 2) * 0.5 * 1e-6
V_2= pi * (0.5 ** 2) * 0.5 * 1e-6

rho = 7.55 * 1e3

m = rho * V

sigma = 57142857

m_left = 0.45

m_1 = m_left * V
m_2 = m_left * V_2


mu_0 = 4 * pi * 1e-7

D = 0.01
H = 0.0175
R = 0.05
h0 = 0.014

h = [0.0] * 1000

for i in range(1000):
    h[i] = i / 1000 + 0.01

F_l = [0.0] * 1000

for i in range(1000):
    F1 = (5 / (6 * (R ** 2))) * (1 / h[i] - 1 / (h[i] + D))
    F2 = (1 / (6 * (R ** 3))) * (atan((h[i] / R)) - atan((h[i] + D) / R))
    F3 = (log(1 + ((R ** 2) / (h[i] ** 2)))) / (6 * (h[i] ** 3)) - (log(1 + (R ** 2 / (h[i] + D) ** 2))) / (6 * ((h[i] + D) ** 3))
    F4 = -5 / (18 * (h[i] ** 3)) + 5 / (18 * ((h[i] + D) ** 3))
    F_l[i] = ((9 * sigma * (mu_0 ** 2) * (m_2 ** 2)) / (8 * pi)) * (F1 + F2 + F3 + F4)

xpoints = np.array(h)
ypoints = np.array(F_l)
plt.plot(xpoints, ypoints, lw='0.5')
plt.savefig(path, dpi=320)
