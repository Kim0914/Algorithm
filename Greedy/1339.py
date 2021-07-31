import sys

N = int(input())

word_list = []
word_list = [sys.stdin.readline().strip() for i in range(N)]

alpha_list = []
for word in word_list:
    alpha_list.append(list(word)) # => 단어를 알파벳당 하나씩 쪼개서 리스트에 추가
    
# print('alpha_list : ' , end='') 
# print(alpha_list)

alpha_dict = {}
for alpha in alpha_list: # 알파벳들의 자리수에 해당하는 10000, 1000, 100 ... 값을 {key, value} 형태로 저장
    k = len(alpha) - 1 # 단어 하나의 길이. ABCDE => A = 10^4 ... 
    for v in alpha:
        if v in alpha_dict: # 이미 dictionay에 있는 경우
            alpha_dict[v] += pow(10,k) 
        else:
            alpha_dict[v] = pow(10,k)
        k -= 1
            
data_list = []

for data in alpha_dict.values():
    data_list.append(data)

data_list.sort(reverse=True)

num_list = [0,1,2,3,4,5,6,7,8,9]
res = 0
for data in data_list:
    res += data * num_list.pop() # data_list의 data들을 9 ~ 0 사이의 해당되는 값과 곱해준다.

print(res)

