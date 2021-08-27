def search(i, j):
    global house

    if i < 0 or j >= n or i >= n or j < 0 or graph[i][j] == 0: # i, j가 범위를 벗어나는 경우, 방문한 좌표인 경우 종료
        return
    
    graph[i][j] = 0  # 그래프에 방문하였다고 0으로 표시
    visited[i][j] = 1 # 방문한 좌표 1로 표시
    house += 1 # 현재 단지에서 집의 갯수 추가

    # 동서남북 탐색
    search(i + 1, j)
    search(i, j + 1)
    search(i - 1, j)
    search(i, j - 1)
   
        
        
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
houses = []
house = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1: # 좌표를 방문하지 않은 경우
            search(i,j)
            houses.append(house)
            house = 0

print(len(houses))
for house_cnt in sorted(houses):
    print(house_cnt)