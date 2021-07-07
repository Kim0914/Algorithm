S = int(input())
sum = 0
i = 1
while(True):
    sum = sum + i
    if(sum > S):
        break
    i += 1
N = i - 1
print(N)