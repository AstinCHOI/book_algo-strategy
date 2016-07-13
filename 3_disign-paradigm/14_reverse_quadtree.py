
MAX_SIZE = 8
decompressed = [[0 for col in range(MAX_SIZE)] for row in range(MAX_SIZE)]

it = '' # xxbwwbbbw
def decompress(y, x, size):
    global it
    head = it[0]
    it = it[1:]
    if head == 'b' or head == 'w':
        for dy in range(size):
            for dx in range(size):
                decompressed[y+dy][x+dx] = head
    else:
        half = int(size / 2)
        decompress(y, x, half)
        decompress(y, x+half, half)
        decompress(y+half, x, half)
        decompress(y+half, x+half, half)


def reverse():
    global it
    head = it[0]
    it = it[1:]
    if head == 'b' or head == 'w':
        return head
    
    upperLeft = reverse() # b W-
    upperRight = reverse() # w b-
    lowerLeft = reverse() # x b- ->xxbwwb
    lowerRight = reverse() # w- b
    
    return "x" + lowerLeft + lowerRight + upperLeft + upperRight


if __name__ == '__main__':
    # it = 'xbwwb'
    it = 'xbwxwbbwb' # xxbwwbbbw
    # decompress(len(it)-1, 0, len(it))
    # print(decompressed)
    print(reverse())