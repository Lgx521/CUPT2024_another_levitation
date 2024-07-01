from kit.functions import *
from kit.Constants import *
import numpy as np
from matplotlib import pyplot as plt

path = '/Users/gansz/Downloads/CUPT2024/PythonAnalysis/plots/force_comparation.png'

# Initializations
dt = 0.00001

t_max = 0.6

steps = int(t_max / dt)

z = [0.0] * steps
z1 = [0.0] * steps
z2 = [0.0] * steps

z1_z = dict()

# Initial conditions
z[0] = 0.0403

# Calculation
for i in range(steps - 1):
    if z[i] < H or z[i] > 1:
        print(f"final {i}, {z[i]}, {z[i-1]}, {z1[i]}, {z1[i-1]}")
        break
    z1_z[z[i]] = z1[i]
    z2[i] = z1[i] * F(z[i]) - g
    z1[i + 1] = z1[i] + z2[i] * dt
    z[i + 1] = z[i] + z1[i] * dt


interval: int = 120

z0 = [0.0] * interval
F_1 = [0.0] * interval
F_1_raw = [0.0] * interval
F_2 = [0.0] * interval
ratio = [0.0] * interval
speed = [0.0] * interval
dz = 0.0001
for i in range(interval):
    z0[i] = 0.028 + dz * i
    temp = optimized_read(z1_z, z0[i])
    F_1[i] = F(z0[i]) * temp
    speed[i] = -1 * temp
    F_1_raw[i] = -F(z0[i])
    F_2[i] = F_m(z0[i])
    ratio[i] = - F_1[i] / F_2[i]

f1 = np.array(F_1)
f1_raw = np.array(F_1_raw)
f2 = np.array(F_2)
spd = np.array(speed)
r = np.array(ratio)
zh = np.array(z0)

plt.figure(figsize=(20, 6))

plt.subplot(1, 3, 1)
plt.plot(zh, f1, lw='1', label='Eddy Current Force(F1) (N)\nMagnet initial position z=0.04')
# plt.plot(zh, f1_raw, lw='1', label='Eddy Current Force(F1_raw)/(N)')
plt.plot(zh, f2, lw='1', label='Magnetic Force(F2) (N)')
plt.title('Separate Plot')
plt.grid()
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(zh, r, lw='1', label='Ratio of F1 to F2')
plt.title('Ratio Plot')
plt.grid()
plt.legend()

plt.subplot(1, 3, 3)
plt.plot(zh, spd, lw='1', label='Speed (m/s)')
plt.title('Speed (Only the plate and falling magnet)')
plt.grid()
plt.legend()

plt.savefig(path, dpi=320)

plt.show()
