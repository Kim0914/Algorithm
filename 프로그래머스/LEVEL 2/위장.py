def solution(clothes):
    answer = 0
    wear = dict()

    for data in clothes:
        j = data[1]
        if j not in wear:
            wear[j] = 1
        else:
            wear[j] += 1

    wear_value = list((wear.values()))

    comb = 1
    for value in wear_value:
        comb = comb * (value+1)
    
    answer = comb - 1
    return answer