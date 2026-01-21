# 트리 형태로 연결되어 있다...
# 트리로 어떻게 만들지 어떻게 연결짓지 ?

def get_size(start, avoid, graph, n):
    # 어디서 시작할지, 어딜 절대 못가는지, 연결 정보, visited 배열 크기
    visited = [False] * (n+1)
    
    stack = [start]     #시작점 넣기
    visited[start] = True
    size = 1
    
    while stack:        # 스택 빌 때까지
        cur = stack.pop()
        
        for nei in graph[cur]:
            if nei != avoid and not visited[nei]:   # 절대 도달하지 못하는 노드는 아니면서 방문한적 없는 노드
                visited[nei] = True     # 방문 표시
                stack.append(nei)       # 연결된 애들 찾아야하니 stack 에 넣기
                size += 1       # 사이즈 늘리기
                
    return size

def solution(n, wires):
    graph = [[] for _ in range(n+1)]        # 빈 노드를 n개수만큼 만들었음
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    #print(graph)
    answer = n
    # 이제 끊은 뒤 각자의 크기를 구하는 로직이 필요 (DFS) - 함수로 처리
    # 모든 간선 끊어보고 제일 작은 값 리턴
    for a, b in wires:
        size_a = get_size(a,b, graph, n)
        size_b = n- size_a
        answer = min(answer, abs(size_a -size_b))
    return answer
                     