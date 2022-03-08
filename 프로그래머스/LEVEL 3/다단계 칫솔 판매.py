def solution(enroll, referral, seller, amount):
    answer = []
    prices = []
    d = {}

    for i in range(len(enroll)):
        prices.append(0)
        d[enroll[i]] = i
    
    for i in range(len(seller)):
        name = seller[i] 
        price = amount[i] * 100
        
        while True:
            ind = d[name] # 본인 번호 찾기
            recom_name = referral[ind] # 추천인 찾기
            
            if recom_name == '-':
                add = price - (price // 10)
                prices[ind] += add
                break
                
            else:
                add = price - (price // 10)
                prices[ind] += add
                price = price // 10
                
                name = recom_name
                if price < 1:
                    break
                    
    answer = prices
    return answer