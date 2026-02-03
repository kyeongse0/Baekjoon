def solution(n, times):
    left, right = 0, max(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        # mid시간으로 심사 가능한 총 인원 계산
        total = 0
        for t in times:
            total += mid // t
            if total >= n:  # 이미 충분하면 더 안 봐도 됨
                break
                
        if total >= n:
            answer = mid  # 이 시간 가능 → 더 작은 시간 시도
            right = mid - 1
        else:
            left = mid + 1
    return answer