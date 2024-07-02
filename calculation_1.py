import numpy as np
import matplotlib.pyplot as plt
from kit.Constants import *
from kit.functions import *

path = '/Users/gansz/Downloads/CUPT2024/PythonAnalysis/plots/cal_plot.png'

# Initializations
dt = 0.0001
t_max = 30
steps = int(t_max / dt)

z = [0.0] * steps
z1 = [0.0] * steps
z2 = [0.0] * steps

# Initial conditions
z[0] = 0.06

# Calculation
for i in range(steps - 1):
    if z[i] < H or z[i] > 1:
        steps = i
        print(f"final {i}, {z[i]}")
        break

    z2[i] = z1[i] * F(z[i]) + F_m(z[i]) - g
    z1[i + 1] = z1[i] + z2[i] * dt
    z[i + 1] = z[i] + z1[i] * dt

# t = [0.0] * steps
# for i in range(steps):
#     t[i] = dt * (i + 1)

t = np.linspace(0, 30, steps)

x = np.array(t)
y = np.array(z[0:steps:1])

plt.figure(figsize=(10, 6))
plt.plot(x, y, lw='0.3')
plt.xlabel('time/seconds')
plt.ylabel('z/meter')
plt.grid()
plt.savefig(path, dpi=600)

plt.show()
