import numpy as np
import matplotlib.pyplot as plt
from kit.Constants import *
from kit.functions import *

path = '/Users/gansz/Downloads/CUPT2024/PythonAnalysis/plots/only_copper.png'

# 开始迭代计算，不包含下方磁铁的作用力

# Initializations
dt = 0.00001
t_max = 0.2
steps = int(t_max / dt)

z = [0.0] * steps
z1 = [0.0] * steps
z2 = [0.0] * steps

#第一次循环，计算初始高度为0.035
# Initial conditions
z[0] = 0.04
# Calculation
for i in range(steps - 1):
    if z[i] < H or z[i] > 1:
        steps = i
        print(f"final {i}, {z[i]}")
        break
    z2[i] = (z1[i] * F(z[i])) - g
    z1[i + 1] = z1[i] + z2[i] * dt
    z[i + 1] = z[i] + z1[i] * dt

y1 = np.array(z[0:steps:1])



t = [0.0] * (steps)
for i in range(steps):
    t[i] = dt * (i + 1)

x = np.array(t)

plt.figure(figsize=(8,6))
plt.grid()
plt.title('Only Copper board and the falling magnet')
plt.xlabel('time/seconds')
plt.ylabel('z/meter')
plt.plot(x, y1, lw='1',label=f'Initial altitude above the board is %-.4fm' % (0.04-H))
plt.legend()
plt.savefig(path, dpi=320)
plt.show()