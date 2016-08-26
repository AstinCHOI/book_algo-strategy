
# board = [
#     [2,5,1,6,1,4,1],
#     [6,1,1,2,2,9,3],
#     [7,2,3,2,1,3,1],
#     [1,1,3,1,7,1,2],
#     [4,1,2,3,4,1,2],
#     [3,3,1,2,3,4,1],
#     [1,5,2,9,4,7,0]
# ]

board = [
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,2],
    [1,1,1,1,1,2,0]
]

n = len(board)
j1 = 0
j2 = 0

def jump(y, x):
    global j1
    j1 = j1 + 1
    if y >= n or x >= n: # out of index
        return False
    if y == n-1 and x == n-1: # arrival
        return True
    
    jumpSize = board[y][x]
    return jump(y + jumpSize, x) or jump(y, x + jumpSize)


cache = [[-1 for i in range(100)] for j in range(100)]
def jump2(y, x):
    global j2
    j2 = j2 + 1
    if y >= n or x >= n:
        return False
    if y == n-1 and x == n-1:
        return True
    
    if cache[y][x] != -1:
        return cache[y][x]

    jumpSize = board[y][x]
    cache[y][x] = (jump2(y + jumpSize, x) or jump2(y, x + jumpSize))
    return cache[y][x]


if __name__ == "__main__":
    print(jump(0, 0))
    print(jump2(0, 0))
    print(j1, j2)