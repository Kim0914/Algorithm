def solution(cacheSize, cities):
    answer = 0
    time = 0
    cities = [city.lower() for city in cities]
    cache = []

    N = len(cities)
    
    if cacheSize == 0: # no cache
        answer = 5 * len(cities)
        return answer
        
    
    else:
        for city in cities:
            if city in cache: # hit
                cache.remove(city)
                cache.append(city)
                time += 1
            
            else: # miss
                if len(cache) < cacheSize:
                    cache.append(city)
                    time += 5
                else:
                    cache.pop(0)
                    cache.append(city)
                    time += 5
    answer = time
    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))


# def solution(cacheSize, cities):
#     answer = 0
#     time = 0
    
#     if cacheSize == 0:
#         answer = 5 * len(cities)
#         return answer

    
#     cache = []
    
#     N = len(cities)

#     for i in range(N):
#         cities[i] = cities[i].lower()
    
#     for i in range(N):
#         if len(cache) == cacheSize: # 캐시가 꽉 참
#             if cities[i] in cache: # hit
#                 time += 1

#                 ind = cache.index(cities[i])
#                 cache.pop(ind)
#                 cache.append(cities[i])

#             else: # miss
#                 time += 5
#                 cache.pop(0)
#                 cache.append(cities[i])

#         else: # 캐시가 비어있음
#             time += 5
#             cache.append(cities[i])
        
#     answer = time
#     return answer