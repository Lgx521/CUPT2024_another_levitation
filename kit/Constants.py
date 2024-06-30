pi = 3.1415926535

g = 9.7887

V = pi * (1.5 ** 2) * 0.5 * 1e-6
V_2= pi * (0.5 ** 2) * 0.5 * 1e-6

rho = 7.55 * 1e3

m = rho * V

sigma = 57142857

m_left = 0.45

m_1 = m_left * V
m_2 = m_left * V_2


mu_0 = 4 * pi * 1e-7

D = 0.02
H = 0.0175
R = 0.05
h0 = 0.014


if __name__ == '__main__':
    print(m)