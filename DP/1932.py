n = int(input())

num_list = []
res = 0

for _ in range(n):
    num_list.append(list(map(int, input().split())))


for i in range(1,n):
    for j in range(len(num_list[i])):
        if j == 0: # 가장 왼쪽(첫번째) 원소
            num_list[i][j] = num_list[i][j] + num_list[i-1][j]
        
        elif j == i: # 가장 오른쪽(마지막) 원소
            num_list[i][j] = num_list[i][j] + num_list[i-1][j-1]

        else: # 위 두 경우를 제외한 나머지 원소
            num_list[i][j] = num_list[i][j] + max(num_list[i-1][j-1], num_list[i-1][j]) # 내려올 수 있는 두 경우 중 값이 큰 것

res = max(num_list[n-1]) # 마지막 depth에서 값이 가장 큰 경우를 선택

print(res)
