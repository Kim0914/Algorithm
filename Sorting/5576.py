w_score = []
k_score = []
for i in range(20):
    score = int(input())
    if i < 10:
        w_score.append(score)
    else:
        k_score.append(score)

w_score.sort(reverse=True)
k_score.sort(reverse=True)

print(w_score[0] + w_score[1] + w_score[2], end = ' ')
print(k_score[0] + k_score[1] + k_score[2])