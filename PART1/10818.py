n = int(input())
num = [int(x) for x in input().split()]
sorted_num = sorted(num)

print(sorted_num[0], end=' ')
print(sorted_num[n-1])