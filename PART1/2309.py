small_boy = []
sum = 0
del_val1 = 0
del_val2 = 0

for i in range(9):
    boy_data = int(input())
    sum = sum + boy_data
    small_boy.append(boy_data)

diff = sum - 100
small_boy = sorted(small_boy)

for i in range(9):
    for j in range(i+1, 9):
        if(small_boy[i] + small_boy[j] == diff):
            del_val1 = small_boy[i]
            del_val2 = small_boy[j]
            break

small_boy.remove(del_val1)
small_boy.remove(del_val2)

for i in range(len(small_boy)):
    print(small_boy[i])