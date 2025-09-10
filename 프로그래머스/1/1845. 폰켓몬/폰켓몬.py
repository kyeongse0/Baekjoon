from collections import Counter
def solution(nums):
    x = Counter(nums)       # 종류별 폰켓몬 수 딕셔너리
    length = len(nums) // 2      # 가져갈 수 있는 폰켓몬 개수
    if (len(x.keys()) >= length):
        answer = length
    else:
        answer = len(x.keys())
    return answer