# 1번은 12345 (8자리) 1250
# 2번은 21232425 (11자리) 910
# 3번은 3311224455 (13자리) 60

# answers와 비교?
# answers 길이만큼 n1,n2,n3 변수에 값 지정 후 비교하기?
# n1, n2, n3 변수에 원하는 만큼 int로 어떻게 리스트 생성할까?

# 나머지 연산을 사용해 패턴에서 몇 번의 정답이 있는지 더하는 방식을 고려했어야 함.

def solution(answers):
    length = len(answers)   # 문제 개수
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0,0,0]
    answer = []
    # 함수화하는게 낫지 않나? 하면 매개변수가 너무 많이 필요함...
    # 이 아니라 각각의 변수 저장이 아닌 리스트에 저장
    for i , a in enumerate(answers):
        if n1[i%len(n1)] == a:
            scores[0] +=1
        if n2[i%len(n2)] == a:
            scores[1] +=1
        if n3[i%len(n3)] == a:
            scores[2] +=1
            
    max_score = max(scores)
    
    for idx, s in enumerate(scores):
        if s == max_score:
            answer.append(idx+1)
    return answer