a,b = map(int, input().split())
data = []
sum = 0
for i in range(1,46):
    for j in range(1,i+1):
        data.append(i)

for ind in range(a-1,b):
    sum += data[ind]
print(sum)