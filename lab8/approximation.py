import matrix as mx

def bubbleMaxRow(matrix: mx.Matrix, index: int):
    maxElem = abs(matrix[index][index])
    rowWithMaxElem = index
    for i in range (index + 1, matrix.n):
        if abs(matrix[i][index]) > maxElem:
            maxElem = abs(matrix[i][index])
            rowWithMaxElem = i
    if rowWithMaxElem != index:
        matrix.swapRows(index, rowWithMaxElem)

def Gauss(matrix: mx.Matrix):
    # прямой ход метода Гаусса
    for k in range (matrix.n - 1):
        bubbleMaxRow(matrix, k)
        matrix.divideRow(k, matrix[k][k])
        for i in range (k + 1, matrix.n):
            div = matrix[i][k]
            # операция над столбцом с ответами
            matrix[i][-1] -= div * matrix[k][-1]

            for j in range (k, matrix.n):
                matrix[i][j] -= div * matrix[k][j]

    # обратный ход метода Гаусса
    x = [0 for i in range(matrix.n)]
    for k in range(matrix.n - 1, -1, -1):
        sum = 0
        for j in range (k + 1, matrix.n):
            sum += matrix[k][j] * x[j]
        x[k] = (matrix[k][-1] - sum) / matrix[k][k]
    x.reverse()
    print('Coefficients: ')
    print("\n".join("a{0} =\t{1:10.6f}".format(i, x) for i, x in enumerate(x)))
    return x

def calculateSumInAnyPower(listValue: list, degree: int):
    sum = 0
    for i in listValue:
        sum += i**degree
    return sum

def calculteSumOfMultiplyElements(listOne, degree, listTwo):
    sum = 0
    if (len(listOne) != len(listTwo)):
        print('Trying to multiply 2 lists of different lengths. Exit!')
        exit(0)
    for x, y in zip(listOne, listTwo):
        sum += x**degree * y
    return sum

def calculateSumOfSquaredErrors(setpoints, getpoints):
    sum = 0
    for i in range (len(setpoints)):
        sum += (getpoints[i] - setpoints[i]) ** 2
    return sum

def createPolynomial(coefficient):
    def polynomial(x):
        y = 0
        for i in range (len(coefficient)):
            y += (x ** i) * coefficient[i]
        return y
    return polynomial
