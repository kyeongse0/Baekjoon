def solution(numbers):
    str_nums = list(map(str, numbers))
    # 각 숫자를 3번 반복해 비교 (최대 숫자가 1000이므로 3자리)
    str_nums.sort(key=lambda x: x*3, reverse=True)
    answer = ''.join(str_nums)
    if answer[0] == '0':
        return '0'
    return answer
