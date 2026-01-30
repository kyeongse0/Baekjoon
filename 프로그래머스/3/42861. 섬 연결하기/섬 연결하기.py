def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])  # 1. 비용 기준 정렬
    parent = [i for i in range(n)]  # 각 섬
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    for a, b, c in costs:  # 2. 간선 하나씩 보면서
        if find(a) != find(b):  # 아직 연결 안된 두 섬이면
            union(a, b)        # 연결하고
            answer += c        # 비용 추가

    return answer