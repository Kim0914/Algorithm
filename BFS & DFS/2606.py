def dfs(v):
    global cnt
    visited[v] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and mat[v][i] == 1:
            cnt += 1
            dfs(i)


n = int(input())
m = int(input())

mat = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n + 1)
cnt = 0

for _ in range(m):
    i, j = map(int, input().split())
    mat[i][j] = 1
    mat[j][i] = 1

dfs(1)
print(cnt)