def solution(progresses, speeds):
    answer = []
    
    while len(progresses) > 0:
        N = len(progresses)
        for i in range(N):
            if progresses[i] != 100:
                progresses[i] += speeds[i]
            
            if progresses[i] >= 100:
                progresses[i] = 100

        cnt = 0
        while True:
            top = progresses[0]
            if top == 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
            else:
                if cnt > 0:
                    answer.append(cnt)
                break
            
            if len(progresses) == 0:
                answer.append(cnt)
                break

    return answer