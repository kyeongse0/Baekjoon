def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0] * m for _ in range(n)]
    
    # 1. 웅덩이 표시 (집/학교는 웅덩이 아님)
    puddle_set = set((x-1, y-1) for x, y in puddles)
    
    dp[0][0] = 1  # 시작점 1가지 방법
    
    # 2. 첫 행 (왼쪽에서만 올 수 있음)
    for j in range(1, m):
        if (j, 0) not in puddle_set:  # 웅덩이 아니면
            dp[0][j] = dp[0][j-1]
    
    # 3. 첫 열 (위에서만 올 수 있음)
    for i in range(1, n):
        if (0, i) not in puddle_set:  # 웅덩이 아니면
            dp[i][0] = dp[i-1][0]
    
    # 4. 나머지 칸들
    for i in range(1, n):
        for j in range(1, m):
            if (j, i) in puddle_set:  # 웅덩이면 0
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
    
    return dp[n-1][m-1]
