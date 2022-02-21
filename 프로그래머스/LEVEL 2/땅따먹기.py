def solution(land):
    answer = 0

    dp = [[0] * 4 for _ in range(len(land))]

    for i in range(4):
        dp[0][i] = land[0][i]

    N = len(land)
    for i in range(1, N): # 전체 행
        for j in range(4): # 열
            data = []
            for k in range(4): # 본인 인덱스 제외한 값
                if k != j:
                    data.append(dp[i-1][k])

            dp[i][j] = max(data) + land[i][j]
            
    answer = max(dp[-1])
    return answer

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))

'''
1 2 3 5
5 6 7 50
4 3 2 1
'''