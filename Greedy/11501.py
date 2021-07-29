import sys
T = int(input())

for loop in range(T):
    profit = 0
    max_val= 0
    
    N = int(sys.stdin.readline())
    stock_data = [int(x) for x in sys.stdin.readline().split()]
    

    max_val = stock_data[-1]

    for i in range(N-1,-1,-1):
        if stock_data[i] > max_val:
            max_val = stock_data[i]
        else:
            profit += (max_val - stock_data[i])

    print(profit)