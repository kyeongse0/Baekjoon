def solution(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    answer = sum / len(numbers)
    return answer