num = input()

if int(num) < 10:
    num = '0' + num

num_list = list(num)

for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

cnt = 0
while(1):
    rem_val = num_list[0]
    tmp = sum(num_list)
    val = list(str(tmp)).pop()
    num_list.remove(rem_val)
    num_list.append(int(val))
    cnt += 1

    check = ''
    for data in num_list:
        check += str(data)
    
    if num == check:
        break

print(cnt)
