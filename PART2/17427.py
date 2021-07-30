N = int(input())
sum_ = 0

for i in range(1,N+1):
    sum_ += (N//i)*i
print(sum_)