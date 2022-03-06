def solution(phoneBook): 
    # 1. 전화번호 sorting 
    phoneBook.sort()
    
    # 2. sorting 한 전화번호부를 2개씩 확인해서 접두어인지 확인한다 
    for i in range(len(phoneBook) - 1): 
        if phoneBook[i+1].startswith(phoneBook[i]):     
            return False 
    return True

