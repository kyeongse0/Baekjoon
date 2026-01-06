# +, - 두 가지 있음
# 깊이 우선 탐색인 것 같은데? +/값\-
# 쭉 내려가서 계산된 값을 리스트에 저장 -> 저장된 리스트 내에 target값이 몇 개인지 count
# 어떻게 구현? for문 안에서 dfs 함수 반복 호출? 
def solution(numbers, target):
    answer = 0
    def dfs(idx, val):
        nonlocal answer     # nonlocal을 써야하는 이유
        if idx == len(numbers):     # 깊이 끝까지 같을 때
            if val == target:       # target 값과 같은지 확인
                answer +=1          # 같으면 answer +1
            return
        dfs(idx+1, val - numbers[idx])  # 다음 깊이로 -
        dfs(idx+1, val + numbers[idx])  # 다음 깊이로 +
    dfs(0,0)    # 0부터 시작
    return answer