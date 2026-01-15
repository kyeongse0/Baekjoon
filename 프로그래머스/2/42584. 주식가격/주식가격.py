# 스택 문제인가
def solution(prices):
    answer = [0] * len(prices)
    stack = []      # 가격이 떨어지지 않은 인덱스 / 
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:    # 새 가격 < 스택 맨 위 가격
            # 떨어졌다!
            idx = stack.pop()
            answer[idx] = i - idx   #떨어지는데 걸린시간
        stack.append(i)
    
    for idx in stack:   # 끝까지 안떨어진 애들
        answer[idx] = len(prices) - idx - 1
    return answer