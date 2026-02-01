# 1, 11, 111 , ... 은 무조건 만들 수 있음
# 자릿수에 따라 ?
# 곱하기의 활용은?
def solution(N, number):
    answer = 0
    dp = [set() for _ in range(9)]  # N을 k번써서 만들 수 있는 수들을 저장할 집합 리스트 (1~8)
    
    for i in range(1,9):
        dp[i].add(int(str(N)*i))    # 기본으로 붙일 수 있는 수
    #print(dp)
        for j in range (1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0: dp[i].add(a // b)
                    
        if number in dp[i]:
            return i
        
    return -1