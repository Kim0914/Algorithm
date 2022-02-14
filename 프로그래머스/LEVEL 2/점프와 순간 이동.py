def solution(n):
    ans = 0

    while True:
        if n == 1:
            ans += 1
            break
        else:
            if n%2 == 0:
                n = n / 2
            
            else:
                ans += 1
                n = (n-1) / 2

    return ans

# 5000 -> 2500 -> 1250 -> 625(1) -> 312 -> 156 -> 78 -> 39(1) -> 19(1) -> 9(1) -> 4 -> 2 -> 1(1)