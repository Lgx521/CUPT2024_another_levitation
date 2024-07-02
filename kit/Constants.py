pi = 3.1415926535

# Gravity
g = 9.7887

# Volume
V = pi * (1.5 ** 2) * 0.5 * 1e-6
V_2= pi * (0.5 ** 2) * 0.5 * 1e-6

# Density of the magnet
rho = 7.55 * 1e3

# Mass of bigger magnet
m = rho * V

# Electric conductivity of copper
sigma = 57142857

# Residual Magnetic Flux Density
m_left = 1.45

# Magnetic conductivity in vacuum
mu_0 = 4 * pi * 1e-7

# Magnetic moment
m_1 = m_left * V / mu_0
m_2 = m_left * V_2 / mu_0

# Initial configuration
D = 0.02
# H = 0.0275
H = 0.025
R = 0.05
h0 = 0.014


if __name__ == '__main__':
    print(m)
