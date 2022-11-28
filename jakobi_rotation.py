from math import sqrt, atan, cos, sin, pi


def diag(mat):
    d = []
    n = len(mat)
    for i in range(n):
        d.append(mat[i][i])
    return d


def matmult(a,b):
    zip_b = zip(*b)
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]


def invert_matrix(a):
    # Section 2: Make copies
    n = len(a)
    a_ = [row[:] for row in a]
    e = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    e_ = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    # Section 3: Perform row operations
    indices = list(range(n))  # to allow flexible row referencing ***
    for fd in range(n):  # fd stands for focus diagonal
        fd_scaler = 1.0 / a_[fd][fd]
        # FIRST: scale fd row with fd inverse.
        for j in range(n):  # Use j to indicate column looping.
            a_[fd][j] *= fd_scaler
            e_[fd][j] *= fd_scaler
        # SECOND: operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd + 1:]:
            # *** skip row with fd in it.
            cr_scaler = a_[i][fd]  # cr stands for "current row".
            for j in range(n):
                # cr - crScaler * fdRow, but one element at a time.
                a_[i][j] = a_[i][j] - cr_scaler * a_[fd][j]
                e_[i][j] = e_[i][j] - cr_scaler * e_[fd][j]
    return e_


v = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
a = [[17, 1, 1], [1, 17, 2], [1, 2, 4]] # Find largest off-diag. element a[k,l]
n = len(a)
maxRot = 5*(n**2)
tol = 0.001

for i in range(maxRot):
    phi = 0
    aMax = 0.0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(a[i][j]) >= aMax:
                aMax = abs(a[i][j])
                k = i;
                m = j
    #print(aMax, k, m)
    if aMax < tol:
        print('eigen values:')
        print(diag(a))
        print('v',v)
        break

    if a[k][k] == a[m][m]:
        if a[k][m] > 0:
            phi = pi/4
        else:
            phi = -(pi/4)
    else:
        phi = 0.5*atan((2*aMax)/(a[k][k] - a[m][m]))
    e = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    h = [row[:] for row in e]
    #print(phi)
    #print(e)
    #print('---------------')

    for i in range(len(e)):
        for j in range(len(e)):
            if i == k and j == k:
                h[i][j] = cos(phi)
            if i == k and j == m:
                h[i][j] = -sin(phi)
            if i == m and j == k:
                h[i][j] = sin(phi)
            if i == m and j == m:
                h[i][j] = cos(phi)
    #print(h)
    new_a = matmult(invert_matrix(h), a)
    #print(new_a)
    a = matmult(new_a, h)
    for i in range(n):
        for j in range(n):
            if a[i][j] < tol:
                a[i][j] = 0.0

    # print(v)
    # print(h)
    v = matmult(v, h)
    print(v)
    print('-----')

    v_1 = [v[0][0], v[1][0], v[2][0]]
    v_2 = [v[0][1], v[1][1], v[2][1]]
    v_3 = [v[0][2], v[1][2], v[2][2]]
    print(v_1)
    print(v_2)
    print(v_3)






