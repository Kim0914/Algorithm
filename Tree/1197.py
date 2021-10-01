import sys
input = sys.stdin.readline

def find(x):
    if x != Vroot[x]: # 자기 자신의 vertex가 root가 아니면
        Vroot[x] = find(Vroot[x]) # parent의 root값 return
    return Vroot[x]

v, e = map(int, input().split())
graph = []
Vroot = [i for i in range(v+1)] # 루트노드를 자기 자신의 vertex로 초기화

for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append([a,b,c])

graph.sort(key = lambda x:x[2], reverse=False) # 간선 가중치에 따라 오름차순 정렬

ans = 0
for s, e, w in graph:
    sRoot = find(s)
    eRoot = find(e)
    print(Vroot)
    print(sRoot, eRoot)
    # 두 정점의 루트가 같으면 사이클 형성
    if sRoot != eRoot: # 두 정점의 루트가 서로 다른 경우
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot # 큰 루트값을 작은 루트값으로 변경
        else:
            Vroot[eRoot] = sRoot

        ans += w # 총 비용 계산

print(ans)

'''
7 11
2 3 12
3 1 13
1 5 14
3 6 17
1 2 19
4 7 28
1 4 30
2 6 39
6 7 49
1 7 54
5 7 76
'''