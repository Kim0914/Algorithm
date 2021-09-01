from collections import deque

def bfs(x,y):
    global cnt

    if x == n-1 and y == m-1: # 의미 없는 코드
        return

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1] # 동서남북을 이동하기 위해 설정
    
    visited[x][y] = 1 # 처음 들린 0,0 좌표를 들렀다고 표시
    queue.append([x,y]) # 큐에 0,0 좌표를 먼저 넣는다
    
    while queue:
        # for data in graph:
        #     print(data)
        # print('----------------------------')
        x,y = queue.popleft()
        for i in range(4): # 동서남북을 이동하기 위해 4번 반복
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: # 이동할 좌표가 범위 내에 있는지 먼저 확인
                if graph[nx][ny] == 1 and visited[nx][ny] == 0: # 이동할 좌표가 범위 내에 있고, 이동할 수 있는 칸이며, 방문하지 않은 경우
                    graph[nx][ny] = graph[x][y] + 1 # 이전 좌표에서 1을 더해주고
                    visited[nx][ny] = 1 # 이동할 좌표를 방문하였다고 표시
                    queue.append([nx,ny]) # 이동할 좌표를 큐에 넣고 반복

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
queue = deque()

bfs(0,0) # 0,0 은 항상 1이기 때문에 (시작점) 0,0 부터 시작

print(graph[n-1][m-1]) # N, M 위치의 값을 출력