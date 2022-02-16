def solution(m, n, board):
    answer = 0
    block = []
    for data in board:
        block.append(data)

    print(block)
    return answer


print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))