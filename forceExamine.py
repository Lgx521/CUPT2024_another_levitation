from kit.functions import *
import numpy as np
from matplotlib import pyplot as plt

path = '/Users/gansz/Downloads/CUPT2024/PythonAnalysis/plots/force_examine.png'

interval = 250

z = [0.0] * interval
F_1 = [0.0] * interval
F_2 = [0.0] * interval
ratio = [0.0] * interval
dz = 0.0001
for i in range(interval):
    z[i] = 0.03 + dz * i
    F_1[i] = F(z[i])
    F_2[i] = F_m(z[i])
    ratio[i] = -F_1[i] / F_2[i]

f1 = np.array(F_1)
f2 = np.array(F_2)
r = np.array(ratio)
zh = np.array(z)



plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
plt.plot(zh, f1, lw='1', label='Eddy Current Force/(N*ss/m)')
plt.plot(zh, f2, lw='1', label='Magnetic Force/(N)')
plt.title('Separate Plot')
plt.grid()
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(zh, r , lw='1', label='ratio')
plt.title('Ratio Plot')
plt.grid()
plt.legend()

plt.savefig(path, dpi=320)

plt.show()
