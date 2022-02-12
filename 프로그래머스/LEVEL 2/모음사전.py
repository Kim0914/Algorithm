words = []
alpha_list = ['A', 'E', 'I', 'O', 'U']

def dfs(cnt, char):

    if cnt == 5:
        return

    for alpha in alpha_list:
        tmp_c = char + alpha
        words.append(tmp_c)
        dfs(cnt + 1, tmp_c)

def solution(word):
    answer = 0

    dfs(0, '')
    answer = words.index(word) + 1
    return answer



print(solution("AAAAE"))

'''
A = 1
AA = 2
AAA = 3
AAAA = 4
AAAAA = 5
AAAAE = 6
AAAAO = 7
AAAAI = 8
AAAAU = 9
AAAE = 10

'''