info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    answer = []
    

    for query_data in query:
        cnt = 0
        query_data = query_data.replace("and ", "")
        query_data = list(query_data.split())
        

        for info_data in info:
            info_data = info_data.split()
            
            if int(info_data[-1]) < int(query_data[-1]): # 점수가 조건에 충족하지 못하는 경우
                continue
            
            if info_data[0] != query_data[0]: # 언어가 다르거나, 무관이 아니면
                if query_data[0] == '-': pass
                else: continue

            if info_data[1] != query_data[1]: # 직종이 다르거나, 무관이 아니면
                if query_data[1] == '-': pass
                else: continue
                    
            if info_data[2] != query_data[2]: # 경력이 다르거나, 무관이 아니면
                if query_data[2] == '-': pass
                else: continue

            if info_data[3] != query_data[3]: # 음식이 다르거나, 무관이 아니면
                if query_data[3] == '-': pass
                else: continue

            cnt += 1

        answer.append(cnt)
    
    return answer


solution(info, query)