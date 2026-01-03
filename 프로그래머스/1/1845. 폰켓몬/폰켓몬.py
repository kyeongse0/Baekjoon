# 딕셔너리 이용해서 각 숫자당 몇 마리가 있는지 확인하기
def solution(nums):
    cnt = {}
    answer = 0
    for num in nums:
        if num in cnt:
            cnt[num] += 1
        else:
            cnt[num] = 1
    get = len(nums)/2   # 가져갈 수 있는 폰켓몬 수
    if get >= len(cnt.keys()):
        answer = len(cnt.keys())
    else:
        answer = get
    return answer