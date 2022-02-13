bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

# bridge_length: 다리에 올라가는 트럭 수
# weight: 다리가 견디는 무게
# truck_weights: 트럭별 무게

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    
    while bridge:
        answer += 1
        bridge.pop(0)  # 1. [0], 2. [7]
        
        if truck_weights:
            if truck_weights[0] <= weight - sum(bridge):
                bridge.append(truck_weights.pop(0)) # 1. [0,7]
            
            else:
                bridge.append(0) # 2. [7,0]

    return answer

print(solution(bridge_length, weight, truck_weights))