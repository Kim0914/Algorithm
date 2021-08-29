from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    queue.append([x, y])
    visited = [[0] * n for _ in range(m)]
    visited[x][y] = 1
    cnt = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4): # 동서남북 4개의 방향을 검사하기 위해
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n: # 범위안에 있는지 확인
                if graph[nx][ny] == 'L' and visited[nx][ny] == 0: # 이동할 좌표가 육지이고, 방문하지 않은 좌표인 경우
                    visited[nx][ny] = visited[x][y] + 1 # 이전 좌표의 이동 값에서 1을 더해서 갱신
                    cnt = max(cnt, visited[nx][ny]) # 가장 마지막 좌표에 입력된 값이 최종 거리
                    queue.append([nx,ny]) # 인접한 좌표를 queue에 넣고 다시 탐색한다

    return cnt - 1 # 1부터 시작하기 때문에 1 에서 부터의 길이는 최종값 - 1


m, n = map(int, input().split())
graph = []
queue = deque()

for _ in range(m):
    graph.append(list(map(str, input())))

res = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 'L':
            res = max(res, bfs(i,j)) # 모든 경우를 시작점으로 하여 최단 거리 중 가장 max인 값.

print(res)

'''
DFS는 시작점에서 도착점으로 가는 무한히 많은 길을 탐색해야 해서 구하기 어려움
BFS는 최단거리를 찾자마자 종료할 수 있다
'''


