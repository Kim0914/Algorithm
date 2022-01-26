clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]


def solution(clothes):
    answer = 0
    wear = dict()

    for data in clothes:
        j = data[1] # 옷 종류
        if j not in wear: # 새로운 종류이면
            wear[j] = 1     # 종류 추가
        else:             # 있는 종류이면
            wear[j] += 1    # 개수 추가

    wear_value = list((wear.values()))

    comb = 1
    for value in wear_value:
        comb = comb * (value+1) # 입는경우, 입지않는 경우 2가지
    
    answer = comb - 1 # 아무것도 안 입는 경우 X
    return answer