
def bino(n, r):
    if r == 0 or n == r:
        return 1
    return bino(n-1, r-1) + bino(n-1, r)


cache = [[-1 for i in range(30)] for j in range(30)]
def bino2(n, r):
    if r == 0 or n == r:
        return 1
    
    if cache[n][r] != -1:
        return cache[n][r]

    # memoization
    cache[n][r] = bino2(n-1, r-1) + bino2(n-1, r)
    return cache[n][r]

if __name__ == '__main__':
    print(bino(4, 2))
    print(bino2(4, 2))