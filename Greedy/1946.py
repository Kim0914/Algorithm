import sys
T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    cnt = 1
    res = []
    for i in range(N):
        score = [int(x) for x in sys.stdin.readline().split()]
        res.append(score)
    res.sort()
    
    Max = res[0][1]

    for i in range(0,N):
        if Max > res[i][1]:
            cnt += 1
            Max = res[i][1]
    print(cnt)

