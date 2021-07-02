n = int(input())

for i in range(n):
    data = [int(x) for x in input().split()]
    data = sorted(data,reverse=True)
    print(data[2])