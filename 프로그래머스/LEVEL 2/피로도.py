from itertools import permutations

def solution(k, dungeons):
    answer = 0
    dungeons = list(permutations(dungeons, len(dungeons))) # 모든 경우의 수
    counts = []
    
    cnt = 0
    for dungeon in dungeons:
        hp = k
        for data in dungeon:
            heart = data[0]     # 필요한 체력
            fatigue = data[1]   # 소모 체력

            if hp >= heart:
                cnt += 1
                hp -= fatigue

            else:
                break

        counts.append(cnt)
        cnt = 0

    answer = max(counts)
    return answer

