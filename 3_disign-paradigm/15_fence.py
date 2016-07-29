
# my wrong answer
def fence(arr):
    length = len(arr)
    m = 0
    for left in range(length):
        for right in range(left+1, length):
            if arr[left] > arr[right]:
                s = arr[left] * (right - left)
                m = max(s, m)
                break
    return m

# from the book: O(n^2)
def bruteForce(h):
    N = len(h)
    ret = 0

    for left in range(N):
        minHeight = h[left]
        for right in range(left, N):
            minHeight = min(minHeight, h[right])
            ret = max(ret, (right - left + 1) * minHeight)
    return ret

# from the book: O(nlogn)
height = []
def solve(left, right):
    if left == right: return height[left]

    mid = int((left + right) / 2)    
    ret = max(solve(left, mid), solve(mid+1, right))

    lo, hi = mid, mid+1
    h = min(height[lo], height[hi])

    ret = max(ret, h*2)

    # To extend until entire square in the range
    while left < lo or hi < right:
        # Extend to higher height
        if hi < right and (lo == left or height[lo-1] < height[hi+1]):
            hi += 1
            h = min(h, height[hi])
        else:
            lo -= 1
            h = min(h, height[lo])
        
        ret = max(ret, h * (hi - lo + 1))
    
    return ret


if __name__ == '__main__':
    height = [7, 1, 5, 9, 6, 7, 3]
    # height = [1, 4, 4, 4, 4, 3, 3, 3, 1, 1]
    # height = [1, 8, 2, 2]
    print(fence(height))
    print(bruteForce(height))
    print(solve(0, len(height)-1))