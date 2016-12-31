def solution(A):
#    unsorted_A = A
#    sorted_A = sorted(A)

#    return A == sorted(A)

    # find first number that drops after increasing or stay same (e.g., [1, 5, 3, 3, 7] -> 3)
    # "back up" and pick one just before (e.g., 5)
    #
    # find first number greater than the pick (e.g., 7)
    # "back up" and insert number there
    #
    # True if == sorted, else False

    max = 0
    _I = 0
    _J = 0

    for m in A:
        if m >= max:
            max = m
        else:
#            print 'breaking', m 
            _I = A.index(m)
            break # found first local max
#    print '1/one step beyond:', _I

    # this is I
    I = A[_I-1]

    for m in range(_I, len(A)):
        print 'A[m]:', A[m]
        if A[m] < I:
#            print 'continuing'
            continue
        # found second local max
        _J = A.index(A[m])
        print '2/one step beyond:', _J

    # this is J
    J = A[_J-1]

    print 'A[m]:', A[m]
    print 'J:', J
