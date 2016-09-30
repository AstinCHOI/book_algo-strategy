
MAX_NUMBER = 30
triangle = [
    [6],
    [1, 2],
    [3, 7, 4],
    [9, 4, 1, 7],
    [2, 7, 5, 9, 4],
]
n = len(triangle)

cache = [[[-1 
    for i in range(100) ] 
    for j in range(100) ] 
    for k in range(MAX_NUMBER*100+1) ]

# too much memory
def path1(y, x, sum):
    if y == n-1: # the last line
        return sum + triangle[y][x]
    
    if cache[y][x][sum] != -1:
        return cache[y][x][sum]
    
    sum += triangle[y][x]
    cache[y][x][sum] = max(path1(y+1, x+1, sum), path1(y+1, x, sum))
    return cache[y][x][sum]


if __name__ == '__main__':
    print(path1(0, 0, 0))