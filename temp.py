import numpy as np
import matplotlib.pyplot as plt
from kit.functions import F

#save path
path = '/Users/gansz/Downloads/CUPT2024/PythonAnalysis/plots/forceByEddyCurrent_F1-4.png'

h = [0.0] * 1000

for i in range(1000):
    h[i] = i / 50000 + 0.1


F_arr = [0.0] * 1000

for i in range(1000):
    F_arr[i] = F(h[i])

x = np.array(h)
y = np.array(F_arr)


plt.plot(x,y, lw='1', label='Total')
plt.legend()

plt.grid()
plt.xlabel('z')
plt.ylabel('force')

plt.savefig(path, dpi=320)
plt.show()

plt.close()

