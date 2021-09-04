import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
result = [0] * (n+1) # 해당 index마다의 부모 노드를 입력하기 위한 변수
graph = [[] for _ in range(n+1)] 
visited = [0] * (n+1) # 해당 정점을 방문하였는지 체크하기 위한 변수

for _ in range(n-1):
    i, j = map(int, input().split()) # 양방향 연결
    graph[i].append(j) # i 행과 연결된 정점들을 추가
    graph[j].append(i) # j 행과 연결된 정점들을 추가


queue = deque()
queue.append(1) # 가장 먼저 시작할 1번 노드 queue에 넣기

while queue:
    row = queue.popleft()
    visited[row] = 1    # 방문했다고 체크

    for data in graph[row]: # 현재 row 에서 방문할 수 있는 정점들 하나씩 체크
        if visited[data] == 0: # 해당 정점이 방문하지 않은 정점이면
            queue.append(data) # 탐색하기 위해 해당 정점을 queue에 추가
            result[data] = row # 해당 정점의 부모노드를 현재 row로 갱신

for i in range(2, n+1):
    print(result[i])

'''
첫번째 예시로 설명하면, 
7
1 6
6 3
3 5
4 1
2 4
4 7
이 입력으로 들어올 때
[1] = [6, 4]
[2] = [4]
[3] = [6, 5]
[4] = [1, 2, 7]
[5] = [3]
[6] = [1, 3]
[7] = [4]
1부터 queue에 넣고 탐색하기 시작하면, 1을 방문했다고 체크
먼저 6을 선택하게 되고 6을 방문하지 않았으므로 6의 부모는 1이라고 할당
6으로 들어와서 6은 1과 3을 갈 수 있는데, 1은 이미 방문했으므로 3으로 갈 수 있고 3의 부모를 1이라고 할당
'''