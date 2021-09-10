def solution(v):
    answer = []

    
    x_cor = []
    y_cor = []

    for i in range(3):
        x_cor.append(v[i][0])
        y_cor.append(v[i][1])
    
    x_set = list(set(x_cor))
    y_set = list(set(y_cor))
    x_flag1, x_flag2 = x_set[0], x_set[1]
    y_flag1, y_flag2 = y_set[0], y_set[1]

    a, b = 0, 0
    if x_cor.count(x_flag1) == 1:
        a = x_flag1
    else:
        a = x_flag2
    
    if y_cor.count(y_flag1) == 1:
        b = y_flag1
    else:
        b = y_flag2

    answer = [a,b]

    return answer

v = [[1, 4], [3, 4], [3, 10]]

res = solution(v)
print(res)