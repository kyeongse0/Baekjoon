# 참가자 명단에서 완주자 명단을 빼고 나면 누가 남는가?
# dictionary에 participant 이름이 새로 나올 때마다 key추가 후 value 에 1
# 동명이인일 경우 value +1
def solution(participant, completion):
    answer = ''
    count = {}
    for part in participant:
        if part not in count.keys():
            count[part] = 1
        else:
            count[part] += 1
    for com in completion:
        count[com] -= 1
    for name, c in count.items():
        if c != 0:
            answer += name
    return answer