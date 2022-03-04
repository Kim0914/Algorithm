import sys
input = sys.stdin.readline

def insert(heap, num):
    heap.append(num)
    child_index = len(heap) - 1

    while child_index > 1:
        parent_index = child_index // 2

        if heap[child_index] > heap[parent_index]:
            tmp = heap[parent_index]
            heap[parent_index] = heap[child_index]
            heap[child_index] = tmp

            child_index = parent_index
        
        else:
            break



def delete(heap):
    root = heap[1]
    tail = heap.pop()

    parent = 1
    child = 2

    N = len(heap)

    while child <= N - 1:
        if child < N - 1 and heap[child] < heap[child + 1]:
            child += 1
        
        if heap[child] <= tail:
            break
        
        heap[parent] = heap[child]

        parent = child
        child = child * 2

    if len(heap) != 1:
        heap[parent] = tail
    
    return root
    

N = int(input())
heap = [0]

for _ in range(N):
    n = int(input())
        
    if n == 0:
        if len(heap) > 1:
            print(delete(heap))
        else:
            print(0)
    
    else:
        insert(heap, n)
    

'''
sys 라이브러리로 input을 처리하지 않으면 시간초과 발생함 !
'''