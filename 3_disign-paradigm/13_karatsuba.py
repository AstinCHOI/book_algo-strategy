
def normalize(num):
    num.append(0)
    for i in range(len(num) - 1):
        if num[i] < 0:
            borrow = int((abs(num[i]) + 9) / 10)
            num[i+1] -= borrow
            num[i] += borrow * 10
        else:
            num[i+1] += int(num[i] / 10)
            num[i] %= 10
    while len(num) > 1 and num[-1] == 0:
        num.pop()

    return num

def multiply(a, b):
    c = [0 for _ in range(len(a) + len(b) + 1)]
    for i in range(len(a)):
        for j in range(len(b)):
            c[i+j] += a[i] * b[j]
    
    return normalize(c)

# a = a + (b*10^k)
import copy
def addTo(a, b, k):
    an = len(a)
    bn = len(b)
    # a2 = copy.deepcopy(a)
    b2 = copy.deepcopy(b)
    
    for i in range(k):
        b2.insert(0, 0)
    
    if an > bn:
        for j in range(bn, an):
            b2.append(0)
    else:
        for j in range(an, bn):
            a.append(0)

    a = [sum(x) for x in zip(a, b2)]
    
    return normalize(a)

# a -= b (suppose a >= b)
def subFrom(a, b):
    an = len(a)
    bn = len(b)

    # a2 = copy.deepcopy(a)
    b2 = copy.deepcopy(b)

    if an > bn:
        for j in range(bn, an):
            b2.append(0)
    else:
        for j in range(an, bn):
            a.append(0)
    
    b2 = [x * -1 for x in b2]
    a = [sum(x) for x in zip(a, b2)]

    return normalize(a)


def karatsuba(a, b):
    an = len(a)
    bn = len(b)
    if an < bn:
        return karatsuba(b, a)
    
    if an == 0 or bn == 0:
        return [0]
    
    if an <= 50: 
        return multiply(a, b)
    
    half = int(an / 2)
    
    a0 = a[:half]
    a1 = a[half:]
    b0 = b[:min(len(b), half)]
    b1 = b[min(len(b), half):]
    
    # z2 = a1 * b1
    z2 = karatsuba(a1, b1)

    # z0 = a0 * b0
    z0 = karatsuba(a0, b0)

    # a0 = a0 + a1; b0 = b0 + b1
    a0 = addTo(a0, a1, 0)
    b0 = addTo(b0, b1, 0)

    # z1 = (a0 * b0) - z0 - z2
    z1 = karatsuba(a0, b0)
    z1 = subFrom(z1, z0)
    z1 = subFrom(z1, z2)

    # ret = z0 + z1 * 10^half + z2 * 10^(half*2)
    ret = addTo([], z0, 0)
    ret = addTo(ret, z1, half)
    ret = addTo(ret, z2, half + half)
    
    return ret

a = [3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1,3,2,1]
b = [3]
print(karatsuba(a, b))