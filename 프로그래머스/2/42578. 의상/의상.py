def solution(clothes):
    answer = 1
    count ={}
    # 종류별로 개수를 딕셔너리화
    for cloth in clothes:
        if cloth[-1] not in count:
            count[cloth[-1]] = 1
        else:
            count[cloth[-1]] += 1
    
    answer = 1
    for c in count.values():
        answer *= (c + 1)   # 안 입는 경우까지 포함
    
    return answer - 1  