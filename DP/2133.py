N = int(input())

tile = [0] * 31 # N 은 1 ~ 30

tile[0] = 1 # N == 0 인 경우, 아무것도 놓지 않는 경우를 1
for i in range(2, N+1, 2): # N이 홀수인 경우에는 만들 수 없다
    tile[i] = tile[i-2] * 3 # 바로 직전 짝수[i-2]번째 N 의 값에는 * 3

    for j in range(0, i-2, 2): # 바로 직전[i-2]번째를 제외한 N 값 * 2를 더해주는 점화식
        tile[i] += tile[j] * 2

print(tile[N])









