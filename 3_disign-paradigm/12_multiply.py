
def normalize(num):
    num.append(0)
    print(num)
    for i in range(len(num) - 1):
        if num[i] < 0:
            borrow = (abs(num[i]) + 9) / 10
            num[i+1] -= borrow
            num[i] += borrow * 10
        else:
            num[i+1] += num[i] / 10
            num[i] %= 10
    while len(num) > 1 and num[-1] == 0:
        num.pop()

def multiply(a, b):
    c = [0 for _ in range(len(a) + len(b) + 1)]
    for i in range(len(a)):
        for j in range(len(b)):
            c[i+j] += a[i] * b[j]
    normalize(c)
    return c

print(multiply([3, 2, 1], [6, 5, 4])) # 123 x 456 = 56088
# >>>
# [8, 8, 0, 6, 5]