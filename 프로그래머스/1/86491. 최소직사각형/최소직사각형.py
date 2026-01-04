# 가로로 눕혀 수납하는 경우를 고려해야 함 (회전)
# 큰 수를 앞에, 작은 수를 뒤에 ?
def solution(sizes):
    answer = 0
    ssize = []
    for i in sizes:
        ssize.append(sorted(i))
    
    w = []
    h = []
    for j in ssize:
        w.append(j[0])
        h.append(j[1])
    answer = max(w)*max(h)
    
    return answer