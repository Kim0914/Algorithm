def call(res, num):
    if num == 0:
        print(res)
        return
    res = res * num
    call(res, num-1)
    
N = int(input())
res = 1
if N == 0:
    print(1)
else:
    call(res, N)
    