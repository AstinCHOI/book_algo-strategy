
def match(w, s):
    pos = 0
    while (pos < len(s)) and (pos < len(w)) \
      and (w[pos] == '?' or w[pos] == s[pos]):
        pos += 1
    
    if pos == len(w):
        return pos == len(s)

    if w[pos] == '*':
        skip = 0
        for skip in range(pos+skip, len(s)+1):
            if match(w[pos+1:], s[pos+skip:]):
                return True
    return False


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

    w1 = '*bb*'
    s1 = 'babbbc'

    print(match(w1, s1))

    