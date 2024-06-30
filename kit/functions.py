import numpy as np
from kit.Constants import *

__all__ = ['F']


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


def F(z):
    # 相减相当于完成最后一步莱布尼茨公式的积分运算，获得积分值
    f = F1(z - H + D) - F1(z - H) + F2(z - H + D) - F2(z - H) + F3(z - H + D) - F3(z - H)
    result = ((9 * sigma * (mu_0 ** 2) * (m_2 ** 2)) / (8 * pi * m)) * f
    return result


def F_test(z):
    return F1(z) + F2(z) + F3(z)


# @test
if __name__ == '__main__':
    print(F_test(z=0.1))
