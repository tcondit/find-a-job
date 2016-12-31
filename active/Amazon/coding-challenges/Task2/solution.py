def solution(A, B):
    _A = list(str(A))
    _B = list(str(B))

    zipped_tuple = sum(tuple(map(None, _A, _B)), ())
    zipped_list = []

    for _next in zipped_tuple:
        if _next: # it's not None
            zipped_list.append(_next)

    zipped_result = int(''.join(zipped_list))
    if zipped_result >= 100000000:
        return -1
    return zipped_result
