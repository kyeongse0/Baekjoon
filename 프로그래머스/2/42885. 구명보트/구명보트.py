def solution(people, limit):
    people.sort()  # 오름차순
    answer = 0
    left, right = 0, len(people) - 1
    
    while left <= right:
        if left == right:  # 홀수명일 때 마지막 1명
            answer += 1
            break
        
        if people[left] + people[right] <= limit:
            # 둘 다 태움
            answer += 1
            left += 1
            right -= 1
        else:
            # 무거운 사람만 태움
            answer += 1
            right -= 1
    
    return answer
