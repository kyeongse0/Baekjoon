# 딕셔너리 이용해도 되지 않을까...?
# 안됨 뒤에 같은 숫자가 나왔을 때 유지가 불가능
# 스택이냐 큐냐? 직전 숫자와 비교하는 데에는 스택이 Good
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in arr:
        if answer[-1] == i:
            pass
        else:
            answer.append(i)
    return answer