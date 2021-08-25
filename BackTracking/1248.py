def ck(idx):
    hap = 0
    for i in range(idx, -1, -1):
        hap += result[i]
        if hap == 0 and S[i][idx] != 0: # 해당 값이 0인데 부호가 0이 아닐경우 False
            return False
        elif hap < 0 and S[i][idx] >= 0: # 해당 값이 0 미만인데 부호가 -1이 아닐경우 False
            return False
        elif hap > 0 and S[i][idx] <= 0: # 해당 값이  0보다 큰데 부호가 0보다 작거나 같은경우 False
            return False
    return True # 위의 조건문 다 걸리지 않는다면 True

def solve(idx):
    if idx == N:
        return True
    if S[idx][idx] == 0:
        result[idx] = 0
        return solve(idx+1)
    for i in range(1, 11):
        result[idx] = S[idx][idx] * i
        if ck(idx) and solve(idx+1):
            return True
    return False

N = int(input())
arr = list(input())
S = [[0]*N for i in range(N)]

for i in range(N):
    for j in range(i, N):
        temp = arr.pop(0)
        if temp == '+':
            S[i][j] = 1
        elif temp == '-':
            S[i][j] = -1

result = [0] * N
solve(0)
print(' '.join(map(str, result)))