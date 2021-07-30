i = 1
while(1):
    L, P, V = map(int, input().split())

    if L == 0 or P == 0 or V == 0: # L = 사용가능 P = 연속하는 일 V = 휴가 기간
        break

    cnt = int(V / P)
    div = V % P
    if div > L:
        div = L
    res = (L * cnt) + div
    print('Case ' + str(i) + ': ' +str(res))
    i += 1