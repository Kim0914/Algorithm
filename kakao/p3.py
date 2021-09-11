def solution(fees, records):
    import math
    # 기본 주차시간 : 180분
    # 기본 요금 : 5000원
    # 기준 시간 : 10분
    # 시간당 요금 : 600원
    orgin_time, origin_fee, time_std, time_price = map(int, fees)
    
    answer = []
    car_list = []
    cars = {}
    datas = []
    for record in records:
        record = record.split()
        datas.append(list((record[1], record[0], record[2])))
        car_list.append(record[1])
        cars[record[1]] = 0

    datas = sorted(datas)
    
    for i in range(len(datas)):
        finish_hour, finish_min = 23, 59
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

            else: finish_hour, finish_min = 23, 59

        minute = finish_min - start_min
        if minute < 0:
            finish_hour -= 1
            finish_min += 60
            minute = finish_min - start_min

        hour = finish_hour - start_hour

        time = hour * 60 + minute
        
        tmp = cars.get(datas[i][0])
        tmp = tmp + time
        cars[datas[i][0]] = tmp
       
    
    
    car_list = list(set(car_list))
    car_list.sort()
    # print(cars)
    # print(car_list)

    for car in car_list:
        time_sum = cars.get(car)
        # print(time_sum)
        if time_sum <= orgin_time:
            res = origin_fee
        else:
            res = origin_fee + math.ceil((time_sum - orgin_time) / time_std) * time_price
        answer.append(res)
        
    return answer


fees = [120, 0, 60, 591]
records= ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
print(solution(fees, records))