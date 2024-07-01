import numpy as np
import matplotlib.pyplot as plt
from kit.Constants import *
from kit.functions import *

path = '/Users/gansz/Downloads/CUPT2024/PythonAnalysis/plots/cal_plot.png'


# Initializations
dt = 0.00001
t_max = 2
steps = int(t_max / dt)

z = [0.0] * steps
z1 = [0.0] * steps
z2 = [0.0] * steps

# Initial conditions
z[0] = 0.05

# Calculation
for i in range(steps - 1):
    if z[i] < H or z[i] > 1:
        steps = i
        print(f"final {i}, {z[i]}")
        break
    z2[i] = z1[i] * F(z[i]) + F_m(z[i]) - g
    # z2[i] = -0.5 * z1[i] / m + F_m(z[i]) - g
    z1[i + 1] = z1[i] + z2[i] * dt
    z[i + 1] = z[i] + z1[i] * dt
    # print(f"{i}, {z[i]}")

t = [0.0] * steps
for i in range(steps):
    t[i] = dt * (i + 1)

x = np.array(t)
y = np.array(z[0:steps:1])
# y = np.array(z)


plt.xlabel('time/seconds')
plt.ylabel('z/meter')
plt.figure(figsize=(10,6))
plt.plot(x, y, lw='1')
plt.grid()
plt.savefig(path, dpi = 320)

plt.show()