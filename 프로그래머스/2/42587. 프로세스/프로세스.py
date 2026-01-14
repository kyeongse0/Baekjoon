# priorities 숫자 클수록 먼저 실행됨
# location은 인덱스
# idx 유지한채로 정렬?을? 어케하지?

from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque()
    for idx, val in enumerate(priorities):
        q.append((val,idx)) # (우선순위, 인덱스) 튜플을 큐에 집어넣음
    while len(q) != 0:
        curr = q.popleft()
        if any(curr[0] < x[0] for x in q):  # 내 뒤에 더 큰 우선순위가 있냐
            q.append(curr)
        else:
            answer += 1
            if curr[1] == location:
                return answer