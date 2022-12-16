import numpy as np
import matplotlib.pyplot as plt


def create_basic_polynom(listX, i):

    def basic_polynom(x):
        numerator = 1
        denominator = 1
        for j in range (len(listX)):
            if j != i:
                numerator *= (x - listX[j])
                denominator *= (listX[i] - listX[j])
        return numerator / denominator
    return basic_polynom


def create_lagrange_polynom(listX, listY):
    basics = []

    for i in range (len(listX)):
        basics.append(create_basic_polynom(listX, i))

    def polynomialLagrange(x):
        polynomial = 0
        for i in range (len(listY)):
            polynomial += listY[i] * (basics[i](x))
        return polynomial

    return polynomialLagrange

if __name__== '__main__':
    _x = [-2, -1, 0, 1, 2]
    _y = [13, 10, -1, 10, 13]

    lagrange_p = create_lagrange_polynom(_x, _y)
    print(lagrange_p)
    x_plot= np.linspace(-2, 2, 100)
    y_plot = []

    # for x in _x:
    #     print('x = {}\t y = {}'.format(x, lagrange_p(x)))

    for x in x_plot:
        y_plot.append(lagrange_p(x))

    fig = plt.subplots()
    plt.scatter(_x, _y, c='g')
    plt.plot(x_plot, y_plot, color="g")
    plt.grid(True)

    plt.show()
