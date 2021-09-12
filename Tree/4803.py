import sys
from collections import deque

input = sys.stdin.readline

def check(i):
    queue = deque()
    queue.append(i) # 방문할 차례의 vertex를 큐에 먼저 넣음

    is_cycle = False
    while queue:
        node = queue.popleft()
        if visited[node] == 1: # 그래프를 탐색하다가 방문한 좌표로 돌아오면
            is_cycle = True # 사이클을 형성
        
        visited[node] = 1 # 방문했다고 체크
        for data in graph[node]: # 해당 vertex에서 방문할 vertex를 탐색하며
            if visited[data] == 0: # 방문할 vertex가 방문하지 않은 vertex이면
                queue.append(data) # queue에 넣는다
    return is_cycle


case = 0
while True:
    case += 1
    
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    tree_cnt = 0
    for i in range(1, n+1): # 1 ~ n 까지의 vertex를 다 체크
        if visited[i] == 1: # 이전에 방문한 vertex 이면 체크하지 않고 다음으로 넘김
            continue

        cycle_flag = check(i) # cycle을 가졌는지 아닌지 판단

        if cycle_flag == True:
            #print('i = ' , i)
            continue
        else: # cycle이 없으면 tree 개수 카운트
            tree_cnt += 1
            #print('tree counted by i = ', i)
    
    if tree_cnt > 1:
        print('Case {}: A forest of {} trees.'.format(case, tree_cnt))
    elif tree_cnt == 1:
        print('Case {}: There is one tree.'.format(case))
    else:
        print('Case {}: No trees.'.format(case))
