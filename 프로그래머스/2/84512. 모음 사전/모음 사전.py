# 경우의 수
from itertools import product
def solution(word):
    lst = ['A','E','I','O','U']
    words = []
    answer = 0
    for i in range(1,6):
        for j in product(lst, repeat = i):
            words.append("".join(j))
    words.sort()
    for idx, wd in enumerate(words):
        if wd == word:
            answer = idx + 1
        else:
            continue
    return answer