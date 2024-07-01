import numpy as np
import matplotlib.pyplot as plt
from kit.functions import F

def optimized_read(d:dict, key):
    key_result = -1
    for i in d:
        if (abs((i-key)/key) < 0.01):
            key_result = d[i]
            break
    return key_result

dz = 0.0001

d = dict()

for i in range(1000):
    d[(i/1000)**2] = dz * i


print(d)
ans = optimized_read(d, 0.000144002)
print(ans)


