import sys, time

def search(i,j):
    global length
    
    if i < 0 or j >=n or i >=m or j < 0 or visited[i][j] == 1 or treasure_map[i][j] == 'W':
        return

    print(i, j)
    visited[i][j] =1
    length += 1

    for data in visited:
        print(data)

    # 동서남북 탐색
    search(i + 1, j)
    search(i, j + 1)
    search(i - 1, j)
    search(i, j - 1)
    print('-----------------------------')


m, n = map(int, sys.stdin.readline().split())
treasure_map = [list(sys.stdin.readline().strip()) for _ in range(m)]
length = 0
lengthes = []
visited = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if treasure_map[i][j] == 'L':
            search(i,j)
            lengthes.append(length)
            length = 0

print(lengthes)

'''
DFS방식으로 재귀를 돌리니 무한이 많은 길을 찾아야함.
recursion을 반복하여 깊이를 계산하는데 파이썬에서 오류를 내보냄
'''