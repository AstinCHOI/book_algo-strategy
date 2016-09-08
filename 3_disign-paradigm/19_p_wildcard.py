
a, b, c = 0, 0, 0

def match(w, s):
    global a
    a += 1

    pos = 0
    while pos < len(s) and pos < len(w) \
      and (w[pos] == '?' or w[pos] == s[pos]):
        pos += 1
    
    if pos == len(w):
        return pos == len(s)

    if w[pos] == '*':
        skip = 0
        for skip in range(pos+skip, len(s)+1):
            if match(w[pos+1:], s[skip:]):
                return True
    return False


## O(n^3)
cache = [[-1 for i in range(101)] for j in range(101)]
def matchMemoized(w, s):
    global b
    b += 1

    global W, S
    if cache[w][s] != -1:
        return cache[w][s]
    
    while s < len(S) and w < len(W) \
      and (W[w] == '?' or W[w] == S[s]):
        w += 1
        s += 1

    if w == len(W):
        cache[w][s] = (s == len(S))
        return cache[w][s]
    
    if W[w] == '*':
        skip = 0
        for skip in range(s+skip, len(S)+1):
            if matchMemoized(w+1, skip):
                cache[w][s] = True
                return cache[w][s]

    cache[w][s] = False
    return cache[w][s]


## O(n^2)
cache = [[-1 for i in range(101)] for j in range(101)]
def matchMemoized2(w, s):
    global c
    c += 1

    global W, S    

    if cache[w][s] != -1:
        return cache[w][s]
    
    while s < len(S) and w < len(W) \
      and (W[w] == '?' or W[w] == S[s]):
        cache[w][s] = matchMemoized2(w+1, s+1)
        return cache[w][s]

    if w == len(W):
        cache[w][s] = (s == len(S))
        return cache[w][s]
    
    if W[w] == '*':
        skip = 0
        if matchMemoized2(w+1, s) or (s < len(S) and matchMemoized2(w, s+1)):
            cache[w][s] = True
            return cache[w][s]

    cache[w][s] = False
    return cache[w][s]
    

if __name__ == '__main__':
    # w1 = 'he?p'
    # s1 = 'help'
    # s11 = 'helpp'
    # print(match(w1, s1))
    # print(match(w1, s11))

    # w1 = '*p*'
    # s1 = 'help'
    # s11 = 'papa'
    # print(match(w1, s1))
    # print(match(w1, s11))
    

    # W = '*bb*'
    # S = 'b'
    # print(matchMemoized2(0, 0))


    W = '*bb*'
    S = 'babbbc'
    # print(matchMemoized(0, 0))    
    print(matchMemoized2(0, 0))

    # print(a, b, c)
