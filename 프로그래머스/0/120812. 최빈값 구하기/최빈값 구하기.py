def solution(array):
    count = dict()
    for num in array:
        count[num] = count.get(num, 0) + 1
    max_count = max(count.values())
    candidates = [num for num, cnt in count.items() if cnt == max_count]
    if len(candidates) >1:
        answer = -1
    else:
        answer = candidates[0]
    return answer