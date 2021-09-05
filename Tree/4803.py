import sys
input = sys.stdin.readline

case = 0
while True:
    case += 1
    n, m = map(int, input().split())
    if m == 0 and n == 0:
        break
    
    graph = [[0] for _ in range(n+1)]
    visited = [0] * (n+1)

    for _ in range(m):
        a, b = map(int, input().split())