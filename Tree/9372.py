import sys
input = sys.stdin.readline

def dfs(v):
    global cnt
    cnt += 1
    #print(v, end = ' ') 
    visited[v] = 1 
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1: 
            dfs(i)

T = int(input())

for _ in range(T):
    n, m = map(int, input().split()) # n : 국가의 수, m : 비행기의 종류
    cnt = 0
    graph = [[0] * (n+1) for _ in range(n+1)]
    visited = [0] * (n+1)

    cnt = 0
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    dfs(1)

    print(cnt-1)

'''
edge의 개수만 출력하면 되는 것 같음...

'''