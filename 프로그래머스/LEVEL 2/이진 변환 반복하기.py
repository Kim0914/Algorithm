def solution(s):
    answer = []
    mod_cnt, zero_cnt = 0, 0

    if s == '1':
        answer.append(mod_cnt)
        answer.append(zero_cnt)
        return answer


    while True:
        if s == '1':
            break

        s = list(s)

        new_s = ''
        for i in range(len(s)):
            if s[i] == '1':
                new_s += s[i]
        zero_cnt += len(s) - len(new_s)

        len_s = len(new_s)

        bin_num = (bin(len_s)[2:])
        mod_cnt += 1

        s = bin_num

    answer.append(mod_cnt)
    answer.append(zero_cnt)
    return answer

print(solution("1"))