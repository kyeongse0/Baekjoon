# 모르겠다. 진짜 다 탐색해봐야할 듯 한데
   
def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n   # 방문여부
    answer = 0
    
    def dfs(cur_k, count):
        nonlocal answer
        answer = max(answer, count)
        
        for i in range(n):
            if visited[i] == False and dungeons[i][0] <= cur_k:     # if not visited[i]
                visited[i] = True
                dfs(cur_k- dungeons[i][1], count+1)
                visited[i] = False      #막히면 돌아와서 문 다시 열어놓고 다른 길로 backtrack
    dfs(k, 0)
    return answer