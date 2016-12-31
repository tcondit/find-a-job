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
    I_plus_plus = 0

    for m in A:
        if m >= max:
            max = m
        else:
            print 'breaking', m 
            I_plus_plus = A.index(m)
            break # found a local max
    print 'one step beyond:', I_plus_plus

    # this is  I
    print A[I_plus_plus-1]

