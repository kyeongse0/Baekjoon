# 만들 수 있는 모든 숫자를 찾고,    (완전 탐색?)
# 해당 숫자들 중 소수가 몇 개인지 count
from itertools import permutations

def search(lst):    # 소수 찾는 함수
    primes =[]
    is_prime = False
    for i in lst:
        if i < 2:
            continue
        is_prime = True
        for j in range(2, i):
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return len(primes)

def solution(numbers):
    nums = list(numbers)
    made = set()    # 중복 제거용
    for i in range(1, len(nums)+1):
        for j in permutations(nums, i):
            num = int("".join(j))
            made.add(num)
    answer = search(made)
    return answer

