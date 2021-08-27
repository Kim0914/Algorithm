import sys
m, n = map(int, sys.stdin.readline().split())

treasure_map = [list(sys.stdin.readline().strip()) for _ in range(m)]

land_map = [(i,j) for i in range(m) for j in range(n) if treasure_map[i][j] == 'L']

for data in land_map:
    print(data)