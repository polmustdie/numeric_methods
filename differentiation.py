x = [0.2, 0.5, 0.8, 1.1, 1.4]
y = [12.906, 5.5273, 3.8777, 3.2692, 3.0319]

requiredX = 0.8
indexRequiredY = 2
h = 0.3
print('First right derivative at a point x = {} is {}'.format(requiredX, (y[indexRequiredY + 1] - y[indexRequiredY]) / h))
print('First left derivative at a point x = {} is {}'.format(requiredX, (y[indexRequiredY] - y[indexRequiredY - 1]) / h))
print('First derivative at a point x = {} is {}'.format(requiredX, (y[indexRequiredY + 1] - y[indexRequiredY - 1]) / (2*h)))
print('Second derivative at a point x = {} is {}'.format(requiredX, (y[indexRequiredY + 1] - 2 * y[indexRequiredY] + y[indexRequiredY - 1]) / (h**2)))
