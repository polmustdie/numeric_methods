import numpy as np
import matplotlib.pyplot as plt
import approximation as aprx

if __name__ == '__main__':
    NumberGroup = 10
    NumberStudent = 13
    a = NumberGroup + NumberStudent
    listX = [(i + 0.5) * a for i in range(-3, 2, 1)]
    listY = [84 - NumberGroup, 73 - NumberGroup * 2, 63 - NumberGroup * 3, 55 - NumberGroup * 4, 47 - NumberGroup * 5]
    print('X = ', listX)
    print('Y = ', listY)
    sumXFirstDegree = aprx.calculateSumInAnyPower(listX, 1)
    normalSystemOfLeastSquares = aprx.mx.Matrix(2, 3, [aprx.calculateSumInAnyPower(listX, 2),
                                                       sumXFirstDegree,
                                                       aprx.calculteSumOfMultiplyElements(listX, 1, listY),
                                                       sumXFirstDegree,
                                                       len(listX),
                                                       aprx.calculateSumInAnyPower(listY, 1)])
    linearPolynomial = aprx.createPolynomial(aprx.Gauss(normalSystemOfLeastSquares))

    listXForPlot = np.linspace(listX[0], listX[len(listX) - 1], 1000)
    listYForPlot = []
    listgetYFromLinearPolynomial = []
    for x in listX:
        listgetYFromLinearPolynomial.append(linearPolynomial(x))

    for x in listXForPlot:
        listYForPlot.append(linearPolynomial(x))

    print('Сумма ошибок ', aprx.calculateSumOfSquaredErrors(listY, listgetYFromLinearPolynomial))

    fig = plt.subplots()
    plt.scatter(listX, listY, c='r')
    plt.plot(listXForPlot, listYForPlot, color="g")
    plt.grid(True)

    plt.show()
