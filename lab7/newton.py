import numpy as np
import matplotlib.pyplot as plt


def create_divided_diff(listX, listY, k):
    divided_diff = 0
    for j in range(k + 1):
        multiply = 1
        for i in range(k + 1):
            if i != j:
                multiply *= (listX[j] - listX[i])
        divided_diff += listY[j] / multiply
    return divided_diff


def create_newton_polynom(listX, listY):
    last_divided_diff = []

    for i in range(1, len(listX)):
        last_divided_diff.append(create_divided_diff(listX, listY, i))

    def polynomialNewton(x):
        polynomial = listY[0]
        for k in range(1, len(listY)):
            multiply = 1
            for i in range(k):
                multiply *= (x - listX[i])
            polynomial += last_divided_diff[k - 1] * multiply
        return polynomial

    return polynomialNewton


if __name__ == '__main__':
    _x = [-2, -1, 0, 1, 2]
    _y = [13, 10, -1, 10, 13]

    newton_polynom = create_newton_polynom(_x, _y)

    plot_x = np.linspace(-2, 2, 100)
    plot_y = []

    # for x in _x:
    #     print('x = {:.4f}\t y = {:.4f}'.format(x, newton_polynom(x)))

    for x in plot_x:
        plot_y.append(newton_polynom(x))

    fig = plt.subplots()
    plt.scatter(_x, _y, c='g')
    plt.plot(plot_x, plot_y, color="g")
    plt.grid(True)
    # показываем график
    plt.show()

