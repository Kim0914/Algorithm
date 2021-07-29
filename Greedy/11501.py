import sys
T = int(input())

for loop in range(T):
    profit = 0
    max_val= 0
    
    N = int(sys.stdin.readline())
    stock_data = [int(x) for x in sys.stdin.readline().split()]
    

    while(len(stock_data) > 0):
        max_val = max(stock_data)
        max_ind = stock_data.index(max_val)

        for i in range(max_ind):
            profit = profit + (max_val - stock_data[i])
            
        stock_data = stock_data[max_ind + 1:]
        
    print(profit)

