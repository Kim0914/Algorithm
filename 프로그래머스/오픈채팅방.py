record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
answer = []
client_dict = {} # (id, name)으로 딕셔너리 형태로 저장

for data in record:
    data = data.split(' ')
    status = data[0]

    if status == 'Enter' or status == 'Change':
        uid = data[1]
        name = data[2]
        client_dict[uid] = name


for data in record:
    data = data.split(' ')
    status = data[0]
    uid = data[1]
    if status == 'Enter':
        message = "{}님이 들어왔습니다.".format(client_dict[uid])
        answer.append(message)

    elif status == 'Leave':
        message = "{}님이 나갔습니다.".format(client_dict[uid])
        answer.append(message)

print(answer)
 
