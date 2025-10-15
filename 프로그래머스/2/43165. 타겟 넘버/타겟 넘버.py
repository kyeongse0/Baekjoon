def solution(numbers, target):
    answer = 0
    def dfs(depth, x):
        nonlocal answer
        if (depth == len(numbers)):
            if (x == target):
                answer +=1
            return
        dfs(depth+1, x + numbers[depth])
        dfs(depth+1, x - numbers[depth])
        
    dfs(0,0)
    return answer