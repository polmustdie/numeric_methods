class Matrix:
    def __init__(self, n: int, m: int, values: list = None) -> None:
        self.n = n  # строк
        self.m = m  # столбцов
        if values is None:
            self.matrix = self.getMatrix(n, m)
        else:
            self.matrix = self.setValues(values)

    def getMatrix(self, n: int, m: int):
        matrix = [[None for j in range(m)] for i in range(n)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        return matrix

    def setValues(self, values: list):
        matrix = [[None for j in range(self.m)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                matrix[i][j] = values[i * self.m + j]
        return matrix

    def getReadableMatrixString(self, matrix):
        strings = []
        for row in matrix:
            strings.append(str(row))
        return '\n'.join(strings)

    def __str__(self):
        return self.getReadableMatrixString(self.matrix)

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item: int):
        return self.matrix[item]

    def getNumberOfColomns(self):
        return self.m

    def getNumberOfRows(self):
        return self.n

    def setElement(self, i: int, j: int, element):
        self.matrix[i][j] = element

    def getElement(self, i: int, j: int):
        return self.matrix[i][j]

    def transposeAnyMatrix(self, matrix: 'Matrix'):
        return [list(i) for i in zip(*matrix)]

    def transpose(self):
        self.matrix = self.transposeAnyMatrix(self.matrix)

    def getTranspose(self):
        return self.getReadableMatrixString(self.transpose())

    def multiply(self, matrix: 'Matrix'):
        try:
            print(len(self.matrix), self.n)
            if (self.m != matrix.getNumberOfRows()):
                raise Exception()
            resultMatrix = [[0 for j in range(matrix.getNumberOfColomns())] for i in range(self.n)]
            for i in range(self.n):
                for j in range(matrix.getNumberOfColomns()):
                    for k in range(matrix.getNumberOfRows()):
                        resultMatrix[i][j] += self.matrix[i][k] * matrix[k][j]
            return resultMatrix
        except Exception:
            print(
                'You can\'t multiply matrices! The number of columns in the first matrix is not equal to the number of rows in the second matrix.')

    def getMultiply(self, matrix):
        return self.getReadableMatrixString(self.multiply(matrix))

    def __mul__(self, other):
        # является ли other объектом класса Matrix
        if isinstance(other, Matrix):
            try:
                if (self.m != other.getNumberOfRows()):
                    raise Exception()
                resultMatrix = Matrix(self.n, other.getNumberOfColomns())
                for i in range(self.n):
                    for j in range(other.getNumberOfColomns()):
                        for k in range(other.getNumberOfRows()):
                            resultMatrix[i][j] += self.matrix[i][k] * other[k][j]
            except Exception:
                print(
                    'You can\'t multiply matrices! The number of columns in the first matrix is not equal to the number of rows in the second matrix.')
        else:
            resultMatrix = Matrix(self.n, self.m)
            for i in range(self.n):
                for j in range(self.m):
                    resultMatrix[i][j] = self.matrix[i][j] * other
        return resultMatrix

    def __sub__(self, other: 'Matrix'):
        if (self.n != other.n or self.m != other.m):
            return None
        arr = Matrix(self.n, self.m)
        for i in range(0, self.n):
            for j in range(0, self.m):
                arr.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return arr

    def __add__(self, other: 'Matrix'):
        if (self.n != other.n or self.m != other.m):
            return None
        arr = Matrix(self.n, self.m)
        for i in range(0, self.n):
            for j in range(0, self.m):
                arr.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return arr

    def swapRows(self, row_1: int, row_2: int):
        row = self.matrix[row_1]
        self.matrix[row_1] = self.matrix[row_2]
        self.matrix[row_2] = row

    def divideRow(self, row: int, divider):
        try:
            for i in range(0, self.m):
                self.matrix[row][i] /= divider
        except ZeroDivisionError:
            self.matrix[row][i] = 0

    def combineRows(self, row: int, source_row: int, weight):
        self.matrix[row] = [(a + k * weight) for a, k in zip(self.matrix[row], self.matrix[source_row])]

    def firstNorm(self):
        if (self.m == 1):
            maxElem = 0
            for i in range(self.n):
                if (abs(self.matrix[i][0]) > maxElem):
                    maxElem = abs(self.matrix[i][0])
            return maxElem
        else:
            maxSumInColumns = 0
            for i in range(self.n):
                sum = 0
                for j in range(self.m):
                    sum += abs(self.matrix[i][j])
                if (sum > maxSumInColumns):
                    maxSumInColumns = sum
            return maxSumInColumns

    def secondNorm(self):
        if (self.m == 1):
            sum = 0
            for i in range(self.n):
                sum += abs(self.matrix[i][0])
            return sum
        else:
            maxSumInColumns = 0
            for j in range(self.m):
                sum = 0
                for i in range(self.n):
                    sum += abs(self.matrix[i][j])
                if (sum > maxSumInColumns):
                    maxSumInColumns = sum
            return maxSumInColumns

    def thirdNorm(self):
        if (self.m == 1):
            norma = 0
            for i in range(self.n):
                norma += self.matrix[i][0] ** 2
            return norma ** 0.5
        else:
            norma = 0
            for i in range(self.n):
                for j in range(self.m):
                    norma += self.matrix[i][j] ** 2
            return norma ** 0.5

    def normCalculation(self, norm: int):
        if norm == 1:
            return self.firstNorm()
        if norm == 2:
            return self.secondNorm()
        if norm == 3:
            return self.thirdNorm()

