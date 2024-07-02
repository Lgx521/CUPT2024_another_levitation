import numpy as np
from matplotlib import pyplot as plt
from kit.Constants import *

__all__ = ['F', 'F_m', 'optimized_read', 'air_drag']


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


# 涡旋电场力
def F(z):
    """

    The unity of F1 to F3 which is partial result
    This is a drag force caused by lenz's law
    Notice that the return value's positive direction is positive-z-axis

    :param z: Distance between the two magnet
    :return: the E-M damping force cause by the copper plate
    """
    f = F1(z - H + D) - F1(z - H) + F2(z - H + D) - F2(z - H) + F3(z - H + D) - F3(z - H)
    result = ((9 * sigma * (mu_0 ** 2) * (m_2 ** 2)) / (8 * pi * m)) * f
    return -result


# 磁力
def F_m(z):
    """

    Model: Interaction of two magnetic dipole
    Direction: Reversed (Opposite interaction)

    :param z: Distance between the two magnet
    :return: Magnetic force applied by the upper magnet caused by the lower magnet
    """
    fm = (3 * mu_0 * m_1 * m_2) / (2 * pi * (z ** 4) * m)
    return fm


def air_drag(v):
    """

    a < 0 for v > 0
    a > 0 for v < 0

    :param v: speed
    :return: acceleration of air drag force
    """
    ans = 0.0
    if v <= 0:
        ans = pi * (0.015 ** 2) * 6e-4 * (v ** 2) / m
    else:
        ans = -1 * pi * (0.015 ** 2) * 6e-4 * (v ** 2) / m
    return ans


def optimized_read(d: dict, key):
    """

    Choose the most near data from a dict
    Controlled accuracy: 1%.

    :param d: A dict to refer
    :param key: The key you want to read, there may not have an exact value in the dict
    :return: The value to another key which same to the origin one within in the margin of error
             If no keys within the margin of error, return -1 and print the position in the dict
    """
    key_value = -1
    count = 0
    for i in d:
        count += 1
        if (abs((i - key) / i) < 0.001):
            key_value = d[i]
            break
    if key_value == -1:
        print(count, key_value)
    return key_value


# @test
if __name__ == '__main__':
    print(F1(0.1) + F2(0.1) + F3(0.1))
