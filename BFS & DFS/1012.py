import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i, j):

    global cnt

    if i < 0 or j >= n or i >= m or j < 0 or visited[i][j] == 1 or graph[i][j] == 0:
        return
    
    visited[i][j] = 1
    cnt += 1

    dfs(i, j+1) # 동
    dfs(i, j-1) # 서
    dfs(i-1, j) # 남
    dfs(i+1, j) # 북
    
T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)]
    locates = []
    for _ in range(k):
        i, j = map(int, input().split())
        locates.append((i,j))
        graph[i][j] = 1
    
    cnt = 0
    res = []
    for locate in locates:
        i, j = locate
        if visited[i][j] == 0:
            dfs(i,j)
            if cnt != 0:
                res.append(cnt)
                cnt = 0

    print(len(res))


