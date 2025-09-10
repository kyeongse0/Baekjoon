def solution(n):
    answer = []
    if (n%2 ==0):
        key = int(n/2)   # 10이면 5
    else:
        key= int((n+1)/2) #9면 5
        
    for i in range(0, key):
        answer.append(2*i+1)
    return answer