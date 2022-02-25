import math


def solution(fees, records):
    orgin_time, origin_fee, time_std, time_price = map(int, fees)
    
    answer = []
    car_list = []
    car_dict = {}
    datas = []
    for record in records:
        record = record.split()
        datas.append(list((record[1], record[0], record[2]))) # 차 번호, 시간, IN/OUT
        car_list.append(record[1])
        car_dict[record[1]] = 0 # 차 마다 시간을 담는 dict

    car_list = list(set(car_list)) # 차 종류를 중복 제거
    datas = sorted(datas) # 차량 번호 기준으로 sort 
    # print(datas)

    for i in range(len(datas)):
        finish_hour, finish_min = 23, 59 # 배열이 1개만 있는 경우를 위해 초기화

        if datas[i][2] == 'IN':
            car_num = datas[i][0]
            start_hour = int(datas[i][1].split(':')[0])
            start_min = int(datas[i][1].split(':')[1])
        else:
            continue
        
        for j in range(i+1, len(datas)):
            if datas[j][0] == car_num and datas[j][2] == 'OUT':
                finish_hour = int(datas[j][1].split(':')[0])
                finish_min = int(datas[j][1].split(':')[1])
                break
            
            else:
                finish_hour, finish_min = 23, 59

        minute = finish_min - start_min
        if minute < 0:
            finish_hour -= 1
            finish_min += 60
            minute = finish_min - start_min
        
        hour = finish_hour - start_hour

        time = hour * 60 + minute
        car_dict[car_num] += time


    car_list.sort()
    for car in car_list:
        time_sum = car_dict[car]

        if time_sum <= orgin_time:
            res = origin_fee
        else:
            res = origin_fee + math.ceil((time_sum - orgin_time) / time_std) * time_price
        
        answer.append(res)
    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees,records))