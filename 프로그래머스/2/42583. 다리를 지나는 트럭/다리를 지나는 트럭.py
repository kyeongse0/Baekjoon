# 초를 어떻게 세는 거지? - 넘어가는데 다리 길이 만큼 걸림
from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    before = deque(truck_weights)   # 다리에 오르기 전 (대기줄)
    after = deque([0] * bridge_length) # 다리에 오른 후 가 아니라 다리 길이 만큼의 상태
    current_weight = 0  # 현재 무게
    
    while before or current_weight > 0:
        time += 1       # 루프 맨 위에서 초는 계속 간다.
        truck = after.popleft()
        current_weight -= truck
        
        if before and before[0] + current_weight <= weight:  # 트럭이 또 올라간다면
            new = before.popleft()
            after.append(new)
            current_weight += new
        else:
            after.append(0) #못올라간다면 앞에서 빠진 거 다시 넣기
    return time