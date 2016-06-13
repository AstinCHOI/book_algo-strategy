
INF = 9999
SWITCHES = 10
CLOCKS = 16
linked = [ 
    "xxx.............",
    "...x...x.x.x....",
    "....x.....x...xx",
    "x...xxxx........",
    ".....xxx..x.x...",
    "x.x...........xx",
    "...x..........xx",
    "....xx.x......xx",
    ".xxxxx..........",
    "...xxx...x...x..",
]

def areAligned(clocks):
    pass

def push(clocks, swtch):
    for clock in range(CLOCKS):
        if linked[swtch][clock] == 'x':
            clocks[clock] += 3
            if clocks[clock] == 15:
                clocks[clock] = 3

def slove(clocks, swtch):
    if swtch == SWITCHES:
        if areAligned(clocks):
            return 0
        else:
            return INF
    ret = INF
    for cnt in range(4):
        ret = min(ret, cnt + solve(clocks, swtch + 1))
        push(clocks, swtch)
    
    return ret

if __name__ == '__main__':
    cases = raw_input('num of cases(<=30): ')
    for i in range(cases):
        hw = raw_input('Clocks :')