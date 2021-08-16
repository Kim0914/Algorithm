import sys

def divide(size, start_row, start_col):
    global cnt
    if start_row == r and start_col == c: # 원하는 좌표를 찾은 경우
        print(cnt)
        exit(0)

    # 탐색 중인 사각형 영역에 찾고 있는 좌표가 없다면,
    # 사각형의 크기만큼 cnt에 더해주고 return
    if not (start_row <= r <start_row + size and start_col <= c < start_col + size):
        cnt += size * size
        return

    # 탐색 중인 사각형 영역에 찾고 있는 좌표가 있는 경우, 분할 
    else:
        divide(size // 2, start_row, start_col)
        divide(size // 2, start_row, start_col + size // 2)
        divide(size // 2, start_row + size // 2, start_col)
        divide(size // 2, start_row + size // 2, start_col + size // 2)


n, r, c = map(int, sys.stdin.readline().split())
cnt = 0
divide(2 ** n, 0 , 0)