trial = int(input())

for i in range(trial):
    num = format(int(input()), 'b')
    num_list = list(num)
    num_list.reverse()
    
    for j in range(len(num_list)):
        if(num_list[j] == '1'):
            print(j, end=' ')
    print('')