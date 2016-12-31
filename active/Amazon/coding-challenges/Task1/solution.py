# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    digits = []
    
    for N in S:
        if N.isdigit():
            digits.append(N)
    N2 = ''.join(digits)

    # N2 is now a string of digits
    print (type(N2))

    count = 1
    leftstr = ''
    rightstr = ''
    N3 = ''
    for digit in N2:
        print 'digit:', digit
        print 'count:', count
        if (count % 3) == 0:
            print count
            print digit
            leftstr = N2[:count]
            rightstr = N2[count:]
            return leftstr + "-" + rightstr
        count += 1
