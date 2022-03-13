def solution(gems):
    answer = []
    
    min_len = len(gems) + 1
    gems_len = len(set(gems))
    
    d = {}
    start, end = 0, 0
    while end < len(gems):
        if gems[end] not in d:
            d[gems[end]] = 1
        else:
            d[gems[end]] += 1
            
        end += 1
        
        if len(d) == gems_len:
            while start < end:
                if d[gems[start]] > 1: # 1개보다 많은 경우 줄여야 함
                    d[gems[start]] -= 1
                    start += 1
                
                elif min_len > (end - start):
                    min_len = (end - start)
                    answer = [start+1, end]
                    break
                    
                else:
                    break
                
    
    return answer