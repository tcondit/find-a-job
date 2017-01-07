# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    digits = []
    
    for N in S:
        if N.isdigit():
            digits.append(N)
    N2 = ''.join(digits)

    count = 1
    leftstr = ''
    rightstr = ''
    N3 = ''
    for digit in N2:
        if (count % 3) == 0:
            leftstr = N2[:count]
            rightstr = N2[count:]
            return leftstr + "-" + rightstr
        count += 1
