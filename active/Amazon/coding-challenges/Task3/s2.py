
def solution(A):

    # find first number that drops after increasing or stay same (e.g., [1, 5, 3, 3, 7] -> 3)
    # "back up" and pick one just before (e.g., 5)
    #
    # find first number greater than the pick (e.g., 7)
    # "back up" and insert number there
    #
    # True if == sorted, else False

    if A == sorted(A):
        return True


    max = 0
    _I = 0
    _J = 0

    for m in A:
        if m >= max:
            max = m
        else:
            _I = A.index(m)
            break

    I = A[_I-1]

    max2 = A[_I]

    for m in range(_I, len(A)-1):
        if m >= max2:
            max2 = m
        else:
            _J = A.index(m)
            break

    J = A[_J-1]

    B = []
    x, y = A.index(I), A.index(J)
    A[x], A[y] = A[y], A[x]

    return (A == sorted(A))
