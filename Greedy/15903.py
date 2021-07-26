n, m = map(int, input().split())
num_data = [int(x) for x in input().split()]

num_data.sort()


for i in range(m):
    val = num_data[0] + num_data[1]
    num_data[0], num_data[1] = val, val
    num_data.sort()

print(sum(num_data))