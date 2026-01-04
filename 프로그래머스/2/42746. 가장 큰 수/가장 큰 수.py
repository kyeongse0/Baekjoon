# 왜 정렬 카테고리 문제일까?

# 1. 숫자를 문자열로 변환 2. 정렬 기준 설정 3. 실제로 정렬 4. 엣지케이스 고려(0000)
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))   # 숫자를 문자열로 변환
    numbers.sort(key = lambda x :x*3, reverse=True)
    
    answer="".join(numbers)
    
    return '0' if answer[0] == '0' else answer  # 엣지 케이스 고려