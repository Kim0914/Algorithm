N = int(input())
road_length = list(map(int, input().split()))
oil_price = list(map(int, input().split()))
total_price = 0

cost = oil_price[0]

for i in range(0,N-1):
    if oil_price[i] < cost:
        cost = oil_price[i]
        total_price += cost * road_length[i]

    else:
        total_price += cost * road_length[i]

print(total_price)
