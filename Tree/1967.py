from collections import deque

import sys
input = sys.stdin.readline

n = int(input())
graph= [[] for _ in range(n)]

for _ in range(n):
    x, y, w = map(int, input().split())
