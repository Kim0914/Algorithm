def find(ans, n, m):
    if len(ans) == m:
        print(*ans)
        return
    
    for num in nums:
        if num not in ans:
            if len(ans) == 0 or num > ans[-1]:
                ans.append(num)
                find(ans,n,m)
                ans.pop()
    

n, m = map(int, input().split())

nums = [int(i+1) for i in range(n)]
ans = []
find(ans, n, m)