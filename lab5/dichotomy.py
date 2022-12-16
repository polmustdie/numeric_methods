import numpy as np
import matplotlib.pyplot as plt


def func(coefficient, x):
    y = 0
    for i in range(len(coefficient)):
        y += (x ** i) * coefficient[i]
    return y


def sign_check(a, b, coefficient):
    valueInA = func(coefficient, a)
    valueInB = func(coefficient, b)
    return valueInA * valueInB < 0 # проверка произведения значений функции по формуле


if __name__ == '__main__':
    precision = 0.001

    n = int(input('Power of equation: '))
    coefficient = []

    line = str(input('Enter coefficients in a descending order')).split()
    if line.__len__() != n + 1:
        print('Error input, more than {} elemets'.format(n + 1)) # it's a rule
        exit(-1)

    for num in line:
        try:
            coefficient.append(eval(num)) # list of coefficients
        except ValueError:
            print('Error input in \'{}\''.format(num))
            exit(-2)

    # print(coefficient)
    coefficient.reverse() # ascending order (reversed)
# построение графика
    listX = []
    listY = []

    for x in np.linspace(-15, 0, 1000): # обалсть значений функции, нужна для построения графика
        listX.append(x)
        listY.append(func(coefficient, x)) # значения

    fig = plt.subplots()
    plt.plot(listX, listY)
    plt.grid(True)
    plt.show()
# построение графика end
    a = float(input('Enter a of [a; b]: '))
    b = float(input('Enter b of [a; b]: '))

    if (not sign_check(a, b, coefficient)): # теорема не выполняется
        print('Root doesn\'t exist for the segment')
        exit(-1)

    while b-a > 2 * precision: # до тех пор пока длина отрезка не меньше 2 * погрешность
        # тогда корень - середина последнего отрезка
        c = (a + b) / 2 # division by half
        if (func(coefficient, c) == 0):
            break
        if (sign_check(a, c, coefficient)):
            b = c # меняем
        else: # иначе меняем границу
            a = c
    print('X = ', (a + b) / 2)

 # признак монотонности - сохранение знака производной функции
# Теорема: непрерывная строго монотонная ф-ция имеет единственный 0 на отрезке, т. и т.т.к.
# на концах принимает значение разных знаков.
