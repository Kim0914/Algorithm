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

    
    return True

N = int(input())
heap = []

for _ in range(N):
    n = int(input())
        
    if n == 0:
        if len(heap) > 0:
            print(heap[1])
            delete(heap)
        else:
            print(0)
    
    else:
        insert(heap, n)




    