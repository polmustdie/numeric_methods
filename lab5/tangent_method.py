#
# Условие сходимости:
# f(x0)*f''(x0) > 0

import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return x**3 / 10 + x / 13 + 130


def dif_1(x):
    return 3/10 * x**2 + 1/13


def dif_2(x):
    return 3/5 * x


def conv_check(x):
    return func(x) * dif_2(x) > 0


if __name__ == '__main__':
    listX = np.linspace(-11, -8, 100)
    listY = [func(x) for x in listX]
    fig = plt.subplots()
    plt.plot(listX, listY)
    plt.grid(True)
    plt.show()

    x_curr = -11 # начальное приближение
    if not conv_check(x_curr):
        print('The starting point of the approximation {} does not satisfy the conditions of the theorem'.format(x_curr))
        exit(1)

    x_next = x_curr - func(x_curr) / dif_1(x_curr)
    while abs(x_next - x_curr) > 0.0000001:
        if conv_check(x_curr):
            x_curr = x_next
            x_next = x_curr - func(x_curr) / dif_1(x_curr)
    print('X = ', x_next)

