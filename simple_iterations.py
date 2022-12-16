import matrix as mx


def jacobi(matrixA: mx.Matrix, vectorB: mx.Matrix):
    if not diagonal_check(matrixA, vectorB):
        print("We can't apply Jacobi method:(")
        return False
    for i in range(matrixA.n):
        vectorB[i][0] = vectorB[i][0] / matrixA[i][i]
        for j in range(matrixA.m):
            if i != j:
                matrixA[i][j] = -matrixA[i][j] / matrixA[i][i] # формула
    for i in range(matrixA.n):
        matrixA[i][i] = 0
    return True


def find_not_null(matrix: mx.Matrix, column: int):
    for i in range(matrix.n):
        if matrix[i][column] != 0:
            return i
    return -1


def diagonal_check(matrixA: mx.Matrix, vectorB: mx.Matrix):
    i = 0
    countSwap = 0
    while i != matrixA.n and i != matrixA.m and countSwap != matrixA.n:
        if matrixA[i][i] == 0:
            rowForChange = find_not_null(matrixA, i)
            if rowForChange < 0:
                return False
            else:
                matrixA.swapRows(i, rowForChange)
                vectorB.swapRows(i, rowForChange)
                i = rowForChange
                countSwap += 1
        else:
            i += 1
    if countSwap != matrixA.n:
        return True
    else:
        return False


def error_calc(matrixNorm, normForVector: int, vectorCurrent: mx.Matrix, vectorPrev: mx.Matrix):
    if matrixNorm >= 1:
        return (vectorCurrent - vectorPrev).normCalculation(normForVector) # different formulas for different cases
    else:
        return matrixNorm / (1 - matrixNorm) * (vectorCurrent - vectorPrev).normCalculation(normForVector)


def inputMatrix():
    try:
        lines = int(input('Enter n of rows: '))
        columns = int(input('Enter m of columns: '))
    except ValueError:
        print('Error, input numerics')
        exit(-3)
    matrix = []
    print('Enter matrix')
    for i in range(0, lines):
        line = str(input()).split()
        if line.__len__() != columns:
            print('Error input, more than {} elements'.format(columns)) # using formula
            exit(-1)

        for num in line:
            try:
                matrix.append(float(num))
            except ValueError:
                print('Error input in \'{}\''.format(num))
                exit(-2)
    return [lines, columns, matrix]


if __name__ == '__main__':
    print('Enter matrix coefficients')
    matrixFromUser = inputMatrix()
    matrixForCheck = mx.Matrix(matrixFromUser[0], matrixFromUser[1], matrixFromUser[2])
    matrixAlpha = mx.Matrix(matrixFromUser[0], matrixFromUser[1], matrixFromUser[2])
    print('Enter answer vector')
    vectorFromUser = inputMatrix()
    matrixBeta = mx.Matrix(vectorFromUser[0], vectorFromUser[1], vectorFromUser[2])

    precision = 0.001

    jacobi(matrixAlpha, matrixBeta)

    matrixNorm = matrixAlpha.firstNorm() # choosing the best norm (the least)
    vector_Norm = 1
    tempMatrixNorm = matrixAlpha.secondNorm()
    if tempMatrixNorm < matrixNorm:
        matrixNorm = tempMatrixNorm
        vector_Norm = 2

    tempMatrixNorm = matrixAlpha.thirdNorm()
    if tempMatrixNorm < matrixNorm:
        matrixNorm = tempMatrixNorm
        vector_Norm = 3

    if matrixNorm < 1:
        print(
            " Better norm = {} value = {}".format(
                vector_Norm, matrixNorm))

    vectorNorm = matrixBeta.normCalculation(vector_Norm)
    countIteration = 0 # iteration start
    x_prev = matrixBeta

    while True:
        x_curr = matrixAlpha * x_prev + matrixBeta
        countIteration += 1
        if error_calc(matrixNorm, vector_Norm, x_curr, x_prev) < precision:
            break
        x_prev = x_curr

    print('Number of iterations made: ', countIteration)
    print('Vector x: ')
    print(x_curr)
    print('Check: B * x = ')
    print(matrixForCheck * x_curr)
