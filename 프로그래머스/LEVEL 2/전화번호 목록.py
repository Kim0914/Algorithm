def solution(phone_Book): 
    # 1. 전화번호 sorting 
    phone_Book.sort()
    
    # 2. sorting 한 전화번호부를 2개씩 확인해서 접두어인지 확인한다 
    for i in range(len(phone_Book) - 1): 
        if phone_Book[i+1].startswith(phone_Book[i]):     
            return False 
    return True

