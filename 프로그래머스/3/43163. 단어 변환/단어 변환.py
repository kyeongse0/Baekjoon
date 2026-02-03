# 왜 BFS/DFS일까

from collections import deque

def is_adjacent(a,b):   # 하나만 다른 단어인지 확인 함수
    diff = 0
    for x, y in zip(a,b):
        if x != y:
            diff += 1
            if diff > 1:
                return False
    return diff == 1

def solution(begin, target, words):
    
    if target not in words:
        return 0
    q = deque()     # 큐 비어있음
    q.append((begin,0))     # 큐: [("hit", 0)]  ← (현재단어, 변환횟수)
    visited = set([begin])  # 방문: {"hit"}
    
    while q:
        word, cnt = q.popleft()
        if word == target:      # 타겟값이랑 같음(종료)
            return cnt
        for w in words:         # 타겟과 다름
            if w not in visited and is_adjacent(word, w):
                visited.add(w)
                q.append((w,cnt + 1))
    
    return 0