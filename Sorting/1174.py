num_list = [0,1,2,3,4,5,6,7,8,9]

N = int(input())

# 최대 경우의 수 N 은 1023 (10C1 + ..... 10C10) = 2^10 -1
for num in num_list:
    for j in range(num%10):
        num_list.append(10 * num + j)
        data = 10 * num + j
        if data == 987654321:
            break

if N > len(num_list):
    print(-1)
else:
    print(num_list[N-1])


# def check(num):
    
#     if (num >= 0 and num <= 9):
#         return True
    
#     flag = False
#     num = list(str(num))
#     for i in range(len(num) - 1):
#         if num[i] > num[i+1]:
#             flag = True
#         else:
#             flag = False
#             break
    
#     return flag
    

# N = int(input())
# cnt = 0
# num_list = []
# for i in range(987654321 + 1):
#     print(i)
#     if check(i):
#         num_list.append(i)
#         cnt += 1
#         print('cnt : ' + str(cnt))
#         if(cnt == N):
#             break

# if N > len(num_list):
#     print(-1)
# else:
#     print(num_list[N-1])