# 동,서,남,북
# 깊이 우선 탐색???? 아니었음. 구현은 가능 but recursion err BFS!!!!
# visited 필요
# 도달 못하는 경우 return -1

from collections import deque

def solution(maps):
    n = len(maps)        # 세로
    m = len(maps[0])     # 가로
    
    # 방문 여부 배열
    visited = [[False] * m for _ in range(n)]
    
    # (y, x, dist)
    q = deque()
    q.append((0, 0, 1))          # 시작점, 시작 거리 1칸
    visited[0][0] = True         # 시작점 방문 표시
    
    # 상, 하, 좌, 우
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while q:
        y, x, dist = q.popleft()
        
        # 도착점에 도달
        if y == n-1 and x == m-1:
            return dist
        
        # 4방향 탐색
        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            
            # 범위 체크
            if 0 <= ny < n and 0 <= nx < m:
                # 길이고, 아직 방문 안 했으면
                if maps[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx, dist + 1))
    
    # 큐 다 비워질 때까지 도착 못하면
    return -1
