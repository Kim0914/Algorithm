n, m = map(int, input().split())

board = []
visited = [[0] * m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
num = 0
mx = 0

def bfs(i, j):
    global num, mx
    if visited[i][j] == 1:
        return

    visited[i][j] = 1
    num += 1

    area = 1
    queue = []
    queue.append([i, j])
    while queue:
        pos = queue.pop()
        x, y = pos[0], pos[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            
            if visited[nx][ny] == 1 or board[nx][ny] == 0:
                continue
            
            area += 1
            visited[nx][ny] = 1
            queue.append([nx, ny])
        
    mx = max(mx, area)

for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            bfs(i,j)

print(num)
print(mx)