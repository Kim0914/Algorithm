h, m = map(int, input().split())

if m - 45 < 0:
    h -= 1
    m = (m+60) - 45

    if h < 0:
        h = h + 24
    
    print(h, m)

else:
    print(h, m-45)