import sys
sys.setrecursionlimit(10**9)

N, M = map(int, sys.stdin.readline().split())

mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)] # 방문한 좌표를 체크하기 위해

def findPath(x, y):
    dir = [(1,0), (-1,0), (0,1), (0,-1)]

    if x == N-1 and y == M-1:
        return 1

    if dp[x][y] == -1: # 방문하지 않았으면
        dp[x][y] = 0  # 방문하였다고 표시
    
    for dx, dy in dir:
        if 0 <= x+dx < N and 0 <= y+dy < M and mat[x][y] > mat[x+dx][y+dy]:
            dp[x][y] += findPath(x+dx, y+dy)
    
    return dp[x][y]

print(findPath(0,0))




