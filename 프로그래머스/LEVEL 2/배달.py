N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K = 3



def solution(N, road, K):
    answer = 0

    _map = [[0] * N for _ in range(N)]
    

    for data in road:
        x = data[0]
        y = data[1]
        dis = data[2]
        
        _map[x-1][y-1], _map[y-1][x-1] = dis, dis


            
    return answer


print(solution(N, road, K))