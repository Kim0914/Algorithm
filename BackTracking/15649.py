def dfs(ans, N, M):
    if len(ans) == M:
        print(*ans)
        return
    
    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            dfs(ans, N, M)
            ans.pop()
    

N, M = map(int, input().split()) # 1 ~ N 까지의 자연수 중에서 중복 없이 M 개 고른 수열
ans = []

dfs(ans, N, M)
