def func(_a, _b, _c, _d):
    n = len(_a)
    p = [0]*n
    q = [0]*n
    x = [0]*n

    p[0] = -_c[0]/_b[0]
    q[0] = _d[0]/_b[0]

    for i in range(1, n):
        p[i] = -_c[i]/(_b[i]+_a[i]*p[i-1])
        q[i] = (_d[i] - _a[i]*q[i-1])/(_b[i] + _a[i]*p[i-1])

    x[-1] = q[-1]

    for i in range(n-2, -1, -1):
        x[i] = q[i] + p[i]*x[i+1]

    return x


a = [0, 64, 94, 124, 154]
b = [-34, -124, -274, -484, -754]
c = [-26, -56, -86, -116, 0]
d = [34, 38, 42, 46, 50]
print(func(a, b, c, d))
