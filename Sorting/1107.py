channel = 100
cnt = 0

N = int(input())
btn_cnt = int(input())
num_list = [0,1,2,3,4,5,6,7,8,9]
a = []

if btn_cnt > 0:
    btn_list = [int(x) for x in input().split()]


for num in btn_list:
    if num in num_list:
        num_list.remove(num)
    

N_list = list(map(int, str(N)))


for N_list_data in N_list:
    if N_list_data in num_list:
        a.append(str(N_list_data))
    else:
        tmp = 9
        min_val = 0
        for num_list_data in num_list:
            diff = abs(num_list_data - N_list_data)
            if diff < tmp:
                tmp = diff
                min_val = num_list_data
        a.append(str(min_val))

val = int("".join(a))

cnt1 = len(a) + abs(N - val)
cnt2 = abs(N - channel)

if cnt1 <= cnt2:
    cnt = cnt1
else:
    cnt = cnt2

if N == channel:
    print(0)
else:
    print(cnt)