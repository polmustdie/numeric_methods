
# Сходимость:
# fi(x) принадлежит [a, b] для любого x
# |fi'(x)| < q < 1

import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return x ** 3 / 2197 - x/10 + 1/13


def new_func(x):
    return np.cbrt((2197 / 10) * x - 169)


def diff_func(x):
    return (2197./30) / (np.cbrt(((2197. / 10) * x - 169)**2))


def should_stop(q, x_1, x_2, precision = 0.0001):
    return q / (1 - q) * abs(x_1 - x_2) > precision


if __name__ == '__main__':
    precision = 0.001
    listX = np.linspace(-15, 15, 1000)
    listY = [func(x) for x in listX]
    fig = plt.subplots()
    plt.plot(listX, listY)
    plt.grid(True)
    plt.show()
    start_point = -16 #задаем начальное приближение принадлежащее [a; b]
    #pr = diff_func(start_point)
    q = abs(diff_func(start_point))
    print(q)
    print("производная в точке x = {} : g\'({}) = {}".format(start_point, start_point, diff_func(start_point)))
    x_2 = start_point
    x_1 = new_func(x_2)

    if abs(diff_func(x_1)) >= 1.:
        print("Значение производной в этой точке больше единицы...", start_point)
        exit(-1)

    while True:
        x_0 = new_func(x_1)
        if abs(diff_func(x_0)) >= 1. or should_stop(q, x_1, x_2, precision):
            break
        x_2 = x_1
        x_1 = x_0

print("Найденный корень x =", x_0)

