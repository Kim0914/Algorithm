import sys

def BackTracking(start, cnt):
    if cnt == 6: # 길이가 6이 되면 res를 출력하고 return
        print(*res)
        return

    for i in range(start, len(nums)): # 인자로 넘어온 start index 부터 마지막 까지 반복하며
        res[cnt] = nums[i] # res의 최신값을 nums[i]로 할당한 후
        BackTracking(i+1, cnt+1) # 재귀적으로 호출

while True:
    global res, nums
    nums = list(map(int, sys.stdin.readline().split()))
    head = nums[0]
    if head == 0:
        break
    nums = nums[1:] # 첫번째 원소빼고 다시 nums 정의
    res = [0] * 6 # 결과를 출력하기 위한 변수 초기화
    BackTracking(0,0)
    print()