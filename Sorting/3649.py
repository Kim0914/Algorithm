width = int(input())  # cm
n = int(input())      # rego count

length = []
res = []
sum = 10000000 * width

for i in range(n):
    length.append(int(input()))

sort_length = sorted(length)



for data in sort_length:
    if data > 0:
        diff = sum - data
        
        if diff in sort_length:
            diff_index = sort_length.index(diff)
            data_index = sort_length.index(data)
            value = abs(data - sort_length[diff_index])
            
            if data <= sort_length[diff_index] and diff_index != data_index: 
                res.append((data, sort_length[diff_index], value)) # [(a,b,c), ......]

            elif data <= sort_length[diff_index] and sort_length.count(sort_length[diff_index]) > 1:
                res.append((data, sort_length[diff_index], value))

            else:
                continue

res.sort(key=lambda x:x[2], reverse=True)


if len(res) == 0:
    print('danger')
else:
    print('yes ' + str(res[0][0]) + ' ' + str(res[0][1]))