import numpy as np
from matplotlib import pyplot as plt
from kit.Constants import *

__all__ = ['F', 'F_m', 'optimized_read']


# The eddy current excited force
def F1(z):
    f1 = -1 / (72 * (z ** 3))
    return f1


def F2(z):
    f2 = z * (5 * (R ** 4) - 8 * (R ** 2) * (z ** 2) - 5 * (z ** 4)) / (384 * ((R ** 2 + z ** 2) ** 3) * (R ** 2))
    return f2


def F3(z):
    f3 = -1 * (5 / 384) * (np.arctan(z / R)) / (R ** 3)
    return f3


#涡旋电场力
def F(z):
    # 相减相当于完成最后一步莱布尼茨公式的积分运算，获得积分值
    f = F1(z - H + D) - F1(z - H) + F2(z - H + D) - F2(z - H) + F3(z - H + D) - F3(z - H)
    result = ((9 * sigma * (mu_0 ** 2) * (m_2 ** 2)) / (8 * pi * m)) * f
    return -result


#磁力
def F_m(z):
    fm = (3*mu_0*m_1*m_2)/(2*pi*(z**4)*m)
    return fm


def F_test(z):
    return F1(z) + F2(z) + F3(z)



def __plot():
    dz = 0.00001
    z = [0.0] * 100
    for i in range(100):
        z[i] = dz * i + 0.018

    y1arr = [0.0] * 100
    y2arr = [0.0] * 100
    ratio = [0.0] * 100

    for i in range(100):
        f1 = F(z[i])
        f2 = F_m(z[i])
        y1arr[i] = f1
        y2arr[i] = f2
        ratio[i] = f1 / f2

        print("%-.12f  && %-.12f" % (f1, f2))

    # plt.plot(z,y1arr,lw='1')
    # plt.plot(z,y2arr,lw='1')
    plt.plot(z, ratio, lw='1')
    plt.xlabel('z/meter')
    plt.ylabel('ratio of ECRF to M-force')
    plt.savefig('/Users/gansz/Downloads/CUPT2024/PythonAnalysis/plots/ratio_of_two_force.png', dpi=320)
    plt.show()


def optimized_read(d:dict, key):
    key_value = -1
    count = 0
    for i in d:
        count += 1
        if (abs((i-key)/i) < 0.01):
            key_value = d[i]
            break
    if key_value == -1:
        print(count,key_value)
    return key_value

# @test
if __name__ == '__main__':
    print(F1(0.1)+F2(0.1)+F3(0.1))



