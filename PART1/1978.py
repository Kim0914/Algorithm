n = int(input())
count = 0

data = [int(x) for x in input().split()]

for num in data:
    if(num == 1):
            continue
    for i in range(2,num+1):
        if(i == num):
            count += 1
            break
        if(num % i == 0):
            break
print(count)
    