# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, B):
    # A integer in range [0..100,000,000]
    # B integer in range [0..100,000,000]
    # zip them
    # return -1 for results > 100,000,000

    # get A, convert to list, get length
    # get B, convert to list, get length

    _A = list(str(A))
    _B = list(str(B))

    zipped_tuple = sum(tuple(map(None, _A, _B)), ())

    # >>> sum(tuple(map(None, _a, _b)), ())
    # ('2', '5', '9', '0', '9', None)

    zipped_list = []

    for _next in zipped_tuple:
        if _next: # it's not None
            zipped_list.append(_next)

    return int(''.join(zipped_list))
